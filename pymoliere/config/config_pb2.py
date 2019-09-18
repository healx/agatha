# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pymoliere/config/config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pymoliere/config/config.proto',
  package='pymoliere',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1dpymoliere/config/config.proto\x12\tpymoliere\"T\n\tFtpSource\x12%\n\x07\x61\x64\x64ress\x18\x01 \x01(\t:\x14\x66tp.ncbi.nlm.nih.gov\x12 \n\x07workdir\x18\x02 \x01(\t:\x0fpubmed/baseline\"\x9d\x01\n\rClusterConfig\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x12\n\x04port\x18\x02 \x01(\x05:\x04\x38\x37\x38\x36\x12\x1b\n\rlocal_scratch\x18\x03 \x01(\t:\x04/tmp\x12\x16\n\x0eshared_scratch\x18\x04 \x01(\t\x12\x16\n\x07restart\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x1a\n\x0brun_locally\x18\x06 \x01(\x08:\x05\x66\x61lse\"\x84\x01\n\x10TextParserConfig\x12\x18\n\x10scispacy_version\x18\x01 \x01(\t\x12\x18\n\x10scibert_data_dir\x18\x02 \x01(\t\x12\x1c\n\x10min_sentence_len\x18\x03 \x01(\x05:\x02\x31\x30\x12\x1e\n\x10max_sentence_len\x18\x04 \x01(\x05:\x04\x31\x30\x30\x30\"\xba\x01\n\tKnnConfig\x12\x1a\n\rnum_neighbors\x18\x01 \x01(\x05:\x03\x31\x30\x30\x12\x1b\n\rnum_centroids\x18\x02 \x01(\x05:\x04\x34\x30\x39\x36\x12\x15\n\nnum_probes\x18\x03 \x01(\x05:\x01\x38\x12\x1a\n\x0enum_quantizers\x18\x04 \x01(\x05:\x02\x33\x32\x12\x1d\n\x12\x62its_per_quantizer\x18\x05 \x01(\x05:\x01\x38\x12\"\n\x14training_probability\x18\x06 \x01(\x02:\x04\x30.01\"f\n\x0bRedisConfig\x12\x1a\n\x07\x61\x64\x64ress\x18\x01 \x01(\t:\tlocalhost\x12\x12\n\x04port\x18\x02 \x01(\x05:\x04\x36\x33\x37\x39\x12\x11\n\x06\x64\x62_num\x18\x03 \x01(\x05:\x01\x30\x12\x14\n\x05\x63lear\x18\x04 \x01(\x08:\x05\x66\x61lse\"i\n\tLdaConfig\x12\x16\n\nnum_topics\x18\x01 \x01(\x05:\x02\x32\x30\x12\x17\n\x0brandom_seed\x18\x02 \x01(\x05:\x02\x34\x32\x12\x12\n\x06passes\x18\x03 \x01(\x05:\x02\x32\x30\x12\x17\n\nbatch_size\x18\x04 \x01(\x05:\x03\x31\x32\x38\"A\n\x0bMlSysConfig\x12\x16\n\nbatch_size\x18\x01 \x01(\x05:\x02\x33\x32\x12\x1a\n\x0b\x64isable_gpu\x18\x02 \x01(\x08:\x05\x66\x61lse\"s\n\x14\x43onstructDebugConfig\x12\x15\n\x06\x65nable\x18\x01 \x01(\x08:\x05\x66\x61lse\x12!\n\x14\x64ocument_sample_rate\x18\x02 \x01(\x02:\x03\x30.1\x12!\n\x15partition_subset_size\x18\x03 \x01(\x05:\x02\x35\x30\"\xb1\x02\n\x0f\x43onstructConfig\x12)\n\x07\x63luster\x18\x01 \x01(\x0b\x32\x18.pymoliere.ClusterConfig\x12!\n\x03\x66tp\x18\x03 \x01(\x0b\x32\x14.pymoliere.FtpSource\x12+\n\x06parser\x18\x04 \x01(\x0b\x32\x1b.pymoliere.TextParserConfig\x12*\n\x0csentence_knn\x18\x05 \x01(\x0b\x32\x14.pymoliere.KnnConfig\x12\"\n\x02\x64\x62\x18\x06 \x01(\x0b\x32\x16.pymoliere.RedisConfig\x12#\n\x03sys\x18\x07 \x01(\x0b\x32\x16.pymoliere.MlSysConfig\x12.\n\x05\x64\x65\x62ug\x18\x08 \x01(\x0b\x32\x1f.pymoliere.ConstructDebugConfig\"\xa7\x01\n\x0bQueryConfig\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x0e\n\x06target\x18\x02 \x01(\t\x12\"\n\x02\x64\x62\x18\x03 \x01(\x0b\x32\x16.pymoliere.RedisConfig\x12)\n\x1bmax_sentences_per_path_elem\x18\x04 \x01(\x05:\x04\x35\x30\x30\x30\x12)\n\x0btopic_model\x18\x05 \x01(\x0b\x32\x14.pymoliere.LdaConfig')
)




_FTPSOURCE = _descriptor.Descriptor(
  name='FtpSource',
  full_name='pymoliere.FtpSource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='pymoliere.FtpSource.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("ftp.ncbi.nlm.nih.gov").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workdir', full_name='pymoliere.FtpSource.workdir', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("pubmed/baseline").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=128,
)


_CLUSTERCONFIG = _descriptor.Descriptor(
  name='ClusterConfig',
  full_name='pymoliere.ClusterConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='pymoliere.ClusterConfig.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='pymoliere.ClusterConfig.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=8786,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='local_scratch', full_name='pymoliere.ClusterConfig.local_scratch', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("/tmp").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shared_scratch', full_name='pymoliere.ClusterConfig.shared_scratch', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='restart', full_name='pymoliere.ClusterConfig.restart', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='run_locally', full_name='pymoliere.ClusterConfig.run_locally', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=131,
  serialized_end=288,
)


_TEXTPARSERCONFIG = _descriptor.Descriptor(
  name='TextParserConfig',
  full_name='pymoliere.TextParserConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scispacy_version', full_name='pymoliere.TextParserConfig.scispacy_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scibert_data_dir', full_name='pymoliere.TextParserConfig.scibert_data_dir', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_sentence_len', full_name='pymoliere.TextParserConfig.min_sentence_len', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=10,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_sentence_len', full_name='pymoliere.TextParserConfig.max_sentence_len', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=291,
  serialized_end=423,
)


_KNNCONFIG = _descriptor.Descriptor(
  name='KnnConfig',
  full_name='pymoliere.KnnConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_neighbors', full_name='pymoliere.KnnConfig.num_neighbors', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=100,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_centroids', full_name='pymoliere.KnnConfig.num_centroids', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=4096,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_probes', full_name='pymoliere.KnnConfig.num_probes', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=8,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_quantizers', full_name='pymoliere.KnnConfig.num_quantizers', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=32,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bits_per_quantizer', full_name='pymoliere.KnnConfig.bits_per_quantizer', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=8,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='training_probability', full_name='pymoliere.KnnConfig.training_probability', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.01),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=426,
  serialized_end=612,
)


_REDISCONFIG = _descriptor.Descriptor(
  name='RedisConfig',
  full_name='pymoliere.RedisConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='pymoliere.RedisConfig.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("localhost").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='pymoliere.RedisConfig.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=6379,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='db_num', full_name='pymoliere.RedisConfig.db_num', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clear', full_name='pymoliere.RedisConfig.clear', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=614,
  serialized_end=716,
)


_LDACONFIG = _descriptor.Descriptor(
  name='LdaConfig',
  full_name='pymoliere.LdaConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_topics', full_name='pymoliere.LdaConfig.num_topics', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=20,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='random_seed', full_name='pymoliere.LdaConfig.random_seed', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=42,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='passes', full_name='pymoliere.LdaConfig.passes', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=20,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='pymoliere.LdaConfig.batch_size', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=128,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=718,
  serialized_end=823,
)


_MLSYSCONFIG = _descriptor.Descriptor(
  name='MlSysConfig',
  full_name='pymoliere.MlSysConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='pymoliere.MlSysConfig.batch_size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=32,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disable_gpu', full_name='pymoliere.MlSysConfig.disable_gpu', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=825,
  serialized_end=890,
)


_CONSTRUCTDEBUGCONFIG = _descriptor.Descriptor(
  name='ConstructDebugConfig',
  full_name='pymoliere.ConstructDebugConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enable', full_name='pymoliere.ConstructDebugConfig.enable', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='document_sample_rate', full_name='pymoliere.ConstructDebugConfig.document_sample_rate', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partition_subset_size', full_name='pymoliere.ConstructDebugConfig.partition_subset_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=50,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=892,
  serialized_end=1007,
)


_CONSTRUCTCONFIG = _descriptor.Descriptor(
  name='ConstructConfig',
  full_name='pymoliere.ConstructConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster', full_name='pymoliere.ConstructConfig.cluster', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ftp', full_name='pymoliere.ConstructConfig.ftp', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parser', full_name='pymoliere.ConstructConfig.parser', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sentence_knn', full_name='pymoliere.ConstructConfig.sentence_knn', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='db', full_name='pymoliere.ConstructConfig.db', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sys', full_name='pymoliere.ConstructConfig.sys', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='debug', full_name='pymoliere.ConstructConfig.debug', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1010,
  serialized_end=1315,
)


_QUERYCONFIG = _descriptor.Descriptor(
  name='QueryConfig',
  full_name='pymoliere.QueryConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='pymoliere.QueryConfig.source', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target', full_name='pymoliere.QueryConfig.target', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='db', full_name='pymoliere.QueryConfig.db', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_sentences_per_path_elem', full_name='pymoliere.QueryConfig.max_sentences_per_path_elem', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=5000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='topic_model', full_name='pymoliere.QueryConfig.topic_model', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1318,
  serialized_end=1485,
)

_CONSTRUCTCONFIG.fields_by_name['cluster'].message_type = _CLUSTERCONFIG
_CONSTRUCTCONFIG.fields_by_name['ftp'].message_type = _FTPSOURCE
_CONSTRUCTCONFIG.fields_by_name['parser'].message_type = _TEXTPARSERCONFIG
_CONSTRUCTCONFIG.fields_by_name['sentence_knn'].message_type = _KNNCONFIG
_CONSTRUCTCONFIG.fields_by_name['db'].message_type = _REDISCONFIG
_CONSTRUCTCONFIG.fields_by_name['sys'].message_type = _MLSYSCONFIG
_CONSTRUCTCONFIG.fields_by_name['debug'].message_type = _CONSTRUCTDEBUGCONFIG
_QUERYCONFIG.fields_by_name['db'].message_type = _REDISCONFIG
_QUERYCONFIG.fields_by_name['topic_model'].message_type = _LDACONFIG
DESCRIPTOR.message_types_by_name['FtpSource'] = _FTPSOURCE
DESCRIPTOR.message_types_by_name['ClusterConfig'] = _CLUSTERCONFIG
DESCRIPTOR.message_types_by_name['TextParserConfig'] = _TEXTPARSERCONFIG
DESCRIPTOR.message_types_by_name['KnnConfig'] = _KNNCONFIG
DESCRIPTOR.message_types_by_name['RedisConfig'] = _REDISCONFIG
DESCRIPTOR.message_types_by_name['LdaConfig'] = _LDACONFIG
DESCRIPTOR.message_types_by_name['MlSysConfig'] = _MLSYSCONFIG
DESCRIPTOR.message_types_by_name['ConstructDebugConfig'] = _CONSTRUCTDEBUGCONFIG
DESCRIPTOR.message_types_by_name['ConstructConfig'] = _CONSTRUCTCONFIG
DESCRIPTOR.message_types_by_name['QueryConfig'] = _QUERYCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FtpSource = _reflection.GeneratedProtocolMessageType('FtpSource', (_message.Message,), {
  'DESCRIPTOR' : _FTPSOURCE,
  '__module__' : 'pymoliere.config.config_pb2'
  # @@protoc_insertion_point(class_scope:pymoliere.FtpSource)
  })
_sym_db.RegisterMessage(FtpSource)

ClusterConfig = _reflection.GeneratedProtocolMessageType('ClusterConfig', (_message.Message,), {
  'DESCRIPTOR' : _CLUSTERCONFIG,
  '__module__' : 'pymoliere.config.config_pb2'
  # @@protoc_insertion_point(class_scope:pymoliere.ClusterConfig)
  })
_sym_db.RegisterMessage(ClusterConfig)

TextParserConfig = _reflection.GeneratedProtocolMessageType('TextParserConfig', (_message.Message,), {
  'DESCRIPTOR' : _TEXTPARSERCONFIG,
  '__module__' : 'pymoliere.config.config_pb2'
  # @@protoc_insertion_point(class_scope:pymoliere.TextParserConfig)
  })
_sym_db.RegisterMessage(TextParserConfig)

KnnConfig = _reflection.GeneratedProtocolMessageType('KnnConfig', (_message.Message,), {
  'DESCRIPTOR' : _KNNCONFIG,
  '__module__' : 'pymoliere.config.config_pb2'
  # @@protoc_insertion_point(class_scope:pymoliere.KnnConfig)
  })
_sym_db.RegisterMessage(KnnConfig)

RedisConfig = _reflection.GeneratedProtocolMessageType('RedisConfig', (_message.Message,), {
  'DESCRIPTOR' : _REDISCONFIG,
  '__module__' : 'pymoliere.config.config_pb2'
  # @@protoc_insertion_point(class_scope:pymoliere.RedisConfig)
  })
_sym_db.RegisterMessage(RedisConfig)

LdaConfig = _reflection.GeneratedProtocolMessageType('LdaConfig', (_message.Message,), {
  'DESCRIPTOR' : _LDACONFIG,
  '__module__' : 'pymoliere.config.config_pb2'
  # @@protoc_insertion_point(class_scope:pymoliere.LdaConfig)
  })
_sym_db.RegisterMessage(LdaConfig)

MlSysConfig = _reflection.GeneratedProtocolMessageType('MlSysConfig', (_message.Message,), {
  'DESCRIPTOR' : _MLSYSCONFIG,
  '__module__' : 'pymoliere.config.config_pb2'
  # @@protoc_insertion_point(class_scope:pymoliere.MlSysConfig)
  })
_sym_db.RegisterMessage(MlSysConfig)

ConstructDebugConfig = _reflection.GeneratedProtocolMessageType('ConstructDebugConfig', (_message.Message,), {
  'DESCRIPTOR' : _CONSTRUCTDEBUGCONFIG,
  '__module__' : 'pymoliere.config.config_pb2'
  # @@protoc_insertion_point(class_scope:pymoliere.ConstructDebugConfig)
  })
_sym_db.RegisterMessage(ConstructDebugConfig)

ConstructConfig = _reflection.GeneratedProtocolMessageType('ConstructConfig', (_message.Message,), {
  'DESCRIPTOR' : _CONSTRUCTCONFIG,
  '__module__' : 'pymoliere.config.config_pb2'
  # @@protoc_insertion_point(class_scope:pymoliere.ConstructConfig)
  })
_sym_db.RegisterMessage(ConstructConfig)

QueryConfig = _reflection.GeneratedProtocolMessageType('QueryConfig', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCONFIG,
  '__module__' : 'pymoliere.config.config_pb2'
  # @@protoc_insertion_point(class_scope:pymoliere.QueryConfig)
  })
_sym_db.RegisterMessage(QueryConfig)


# @@protoc_insertion_point(module_scope)
