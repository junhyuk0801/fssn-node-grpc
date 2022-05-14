# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: serverstreaming.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='serverstreaming.proto',
  package='serverstreaming',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15serverstreaming.proto\x12\x0fserverstreaming\"\x1a\n\x07Message\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x17\n\x06Number\x12\r\n\x05value\x18\x01 \x01(\x05\x32]\n\x0fServerStreaming\x12J\n\x11GetServerResponse\x12\x17.serverstreaming.Number\x1a\x18.serverstreaming.Message\"\x00\x30\x01\x62\x06proto3'
)




_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='serverstreaming.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='serverstreaming.Message.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=42,
  serialized_end=68,
)


_NUMBER = _descriptor.Descriptor(
  name='Number',
  full_name='serverstreaming.Number',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='serverstreaming.Number.value', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=70,
  serialized_end=93,
)

DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['Number'] = _NUMBER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'serverstreaming_pb2'
  # @@protoc_insertion_point(class_scope:serverstreaming.Message)
  })
_sym_db.RegisterMessage(Message)

Number = _reflection.GeneratedProtocolMessageType('Number', (_message.Message,), {
  'DESCRIPTOR' : _NUMBER,
  '__module__' : 'serverstreaming_pb2'
  # @@protoc_insertion_point(class_scope:serverstreaming.Number)
  })
_sym_db.RegisterMessage(Number)



_SERVERSTREAMING = _descriptor.ServiceDescriptor(
  name='ServerStreaming',
  full_name='serverstreaming.ServerStreaming',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=95,
  serialized_end=188,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetServerResponse',
    full_name='serverstreaming.ServerStreaming.GetServerResponse',
    index=0,
    containing_service=None,
    input_type=_NUMBER,
    output_type=_MESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVERSTREAMING)

DESCRIPTOR.services_by_name['ServerStreaming'] = _SERVERSTREAMING

# @@protoc_insertion_point(module_scope)
