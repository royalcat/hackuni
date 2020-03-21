# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\ntest.proto\"\x12\n\x03\x45nt\x12\x0b\n\x03mes\x18\x01 \x01(\t\"\x03\n\x01O2!\n\x0bTestService\x12\x12\n\x04ping\x12\x04.Ent\x1a\x02.O\"\x00\x62\x06proto3'
)




_ENT = _descriptor.Descriptor(
  name='Ent',
  full_name='Ent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mes', full_name='Ent.mes', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=32,
)


_O = _descriptor.Descriptor(
  name='O',
  full_name='O',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=37,
)

DESCRIPTOR.message_types_by_name['Ent'] = _ENT
DESCRIPTOR.message_types_by_name['O'] = _O
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Ent = _reflection.GeneratedProtocolMessageType('Ent', (_message.Message,), {
  'DESCRIPTOR' : _ENT,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:Ent)
  })
_sym_db.RegisterMessage(Ent)

O = _reflection.GeneratedProtocolMessageType('O', (_message.Message,), {
  'DESCRIPTOR' : _O,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:O)
  })
_sym_db.RegisterMessage(O)



_TESTSERVICE = _descriptor.ServiceDescriptor(
  name='TestService',
  full_name='TestService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=39,
  serialized_end=72,
  methods=[
  _descriptor.MethodDescriptor(
    name='ping',
    full_name='TestService.ping',
    index=0,
    containing_service=None,
    input_type=_ENT,
    output_type=_O,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TESTSERVICE)

DESCRIPTOR.services_by_name['TestService'] = _TESTSERVICE

# @@protoc_insertion_point(module_scope)