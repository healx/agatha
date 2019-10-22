from pymoliere.config import (
    config_pb2 as cpb,
    proto_util,
)
from pathlib import Path
from pymoliere.construct import file_util
import torch
import dask
from dask.distributed import Client
from pymoliere.construct.dask_checkpoint import checkpoint
from pymoliere.util.misc_util import Record
from typing import Iterable
import numpy as np
from pymoliere.ml.util import BERT_EMB_DIM
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from random import randint


class SequentialEmbeddingPredictor(torch.nn.Module):
  def __init__(self, hidden_size=512):
    super(SequentialEmbeddingPredictor, self).__init__()
    # Input: batch, len(seq), BERT_EMB_DIM
    # Output: batch, BERT_EMB_DIM

    self.hidden_size = hidden_size
    self.num_layers=2
    self.gru = torch.nn.GRU(
        input_size=BERT_EMB_DIM,
        hidden_size=hidden_size,
        num_layers=self.num_layers,
        batch_first=True,
        dropout=0.25,
    )
    self.out = torch.nn.Linear(hidden_size, BERT_EMB_DIM)

  def init_hidden(self, batch_size):
    arbitrary_weight=next(self.parameters()).data
    return Variable(
        arbitrary_weight
        .new(batch_size,self.num_layers, self.hidden_size)
        .zero_()
    )

  def forward(self, x, hidden):
    x, hidden = self.gru(x, hidden)
    x = self.out(x)
    return x, hidden


def group_sentences_into_sequential_abstract_embeddings(
    records: Iterable[np.ndarray]
)->Iterable[Record]:
  abstracts = {}
  for record in records:
    pmid_version = f"{record['pmid']}:{record['version']}"
    embedding = record["embedding"]
    sent_idx = record["sent_idx"]
    if pmid_version not in abstracts:
      abstracts[pmid_version] = {}
    abstracts[pmid_version][sent_idx] = embedding

  data = []
  for _, idx2emb in abstracts.items():
    # Don't want just 1-sentence abstracts
    if len(idx2emb) > 1:
      # Sort by idx, merge embeddings
      mat = np.vstack(list(map(
        lambda idx_emb:idx_emb[1],
        sorted(idx2emb.items())
      )))
      # for r in range(1, mat.shape[0]-1):
        # # 0-r-1, r
        # data.append((
          # torch.FloatTensor(mat[:r, :]),
          # torch.FloatTensor(mat[r, :]),
        # ))
      data.append(mat)
  return data

if __name__ == "__main__":
  config = cpb.SequentialEmbeddingPredictorConfig()
  # Creates a parser with arguments corresponding to all of the provided fields.
  # Copy any command-line specified args to the config
  proto_util.parse_args_to_config_proto(config)
  print("Running pymoliere sentence_classifier with the following parameters:")
  print(config)

  # Potential cluster
  if config.cluster.run_locally or config.cluster.address == "localhost":
    print("Running on local machine!")
  else:
    cluster_address = f"{config.cluster.address}:{config.cluster.port}"
    print("Configuring Dask, attaching to cluster")
    print(f"\t- {cluster_address}")
    dask_client = Client(address=cluster_address)
  if config.cluster.restart:
    print("\t- Restarting cluster...")
    dask_client.restart()

  # Prep scratches
  shared_scratch = Path(config.shared_scratch)
  # Used to load the sentence embedding data produced by pymoliere.construct
  default_ckpt_dir = (
      shared_scratch
      .joinpath("dask_checkpoints")
  )
  model_path = (
      shared_scratch
      .joinpath("models")
      .joinpath("sequential_embedding_predictor")
      .joinpath("model.pt")
  )
  # Need to make sure model_path is writable
  model_path.parent.mkdir(parents=True, exist_ok=True)

  # We're going to store model-specific checkpoints separately
  data_ckpt_dir = (
      shared_scratch
      .joinpath("models")
      .joinpath("sequential_embedding_predictor")
      .joinpath("dask_checkpoints")
  )
  data_ckpt_dir.mkdir(parents=True, exist_ok=True)


  # All data, this is the checkpoint we depend on
  sentences_with_embedding = file_util.load(
      default_ckpt_dir.joinpath("sentences_with_embedding")
  )
  # Gets all data, returns a list of 2d arrays (sentences x embedding)
  all_data = sentences_with_embedding.map_partitions(
      group_sentences_into_sequential_abstract_embeddings
  )
  print("Checkpoint: all_data")
  checkpoint(
      all_data,
      name="all_data",
      checkpoint_dir=data_ckpt_dir,
  )


  # Training data is ready, time to go!
  print("Prepping model")
  if torch.cuda.is_available() and not config.sys.disable_gpu:
    device = torch.device("cuda")
  else:
    device = torch.device("cpu")

  model = SequentialEmbeddingPredictor()

  print("Model -> Device")
  model.to(device)

  loss_fn = torch.nn.MSELoss()
  optimizer = torch.optim.Adam(
      filter(lambda x: x.requires_grad, model.parameters()),
      lr=0.002,
  )

  print("Loading")
  data = file_util.load_to_memory(data_ckpt_dir.joinpath("all_data"))
  training, validation = train_test_split(
      data,
      test_size=config.validation_set_ratio,
  )

  def splits(data):
    a = []; b = []
    for mat in data:
      r = randint(1, mat.shape[0]-1)
      a.append(mat[:r, :])
      b.append(mat[r, :])
    return a, b


  for epoch in config.sys.num_epochs:
    shuffle(training)
    shuffle(validation)
    training_data, training_labels = splits(training)
    validation_data, validation_labels = splits(validation)

    train_model.train_model(
        training_data=training_data,
        training_labels=training_labels,
        validation_data=validation_data,
        validation_labels=validation_labels,
        model=model,
        device=device,
        loss_fn=loss_fn,
        optimizer=optimizer,
        #num_epochs=config.sys.num_epochs,
        batch_size=config.sys.batch_size,
        input_is_sequences=True,
        show_plots=False,
    )

  print("Saving model")
  torch.save(model.state_dict(), model_path)
