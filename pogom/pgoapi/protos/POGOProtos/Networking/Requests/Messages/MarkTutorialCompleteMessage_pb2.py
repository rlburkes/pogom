# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Networking/Requests/Messages/MarkTutorialCompleteMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Enums import TutorialState_pb2 as POGOProtos_dot_Enums_dot_TutorialState__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Networking/Requests/Messages/MarkTutorialCompleteMessage.proto',
  package='POGOProtos.Networking.Requests.Messages',
  syntax='proto3',
  serialized_pb=_b('\nIPOGOProtos/Networking/Requests/Messages/MarkTutorialCompleteMessage.proto\x12\'POGOProtos.Networking.Requests.Messages\x1a$POGOProtos/Enums/TutorialState.proto\"\x9b\x01\n\x1bMarkTutorialCompleteMessage\x12<\n\x13tutorials_completed\x18\x01 \x03(\x0e\x32\x1f.POGOProtos.Enums.TutorialState\x12\x1d\n\x15send_marketing_emails\x18\x02 \x01(\x08\x12\x1f\n\x17send_push_notifications\x18\x03 \x01(\x08\x62\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Enums_dot_TutorialState__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MARKTUTORIALCOMPLETEMESSAGE = _descriptor.Descriptor(
  name='MarkTutorialCompleteMessage',
  full_name='POGOProtos.Networking.Requests.Messages.MarkTutorialCompleteMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tutorials_completed', full_name='POGOProtos.Networking.Requests.Messages.MarkTutorialCompleteMessage.tutorials_completed', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='send_marketing_emails', full_name='POGOProtos.Networking.Requests.Messages.MarkTutorialCompleteMessage.send_marketing_emails', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='send_push_notifications', full_name='POGOProtos.Networking.Requests.Messages.MarkTutorialCompleteMessage.send_push_notifications', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=312,
)

_MARKTUTORIALCOMPLETEMESSAGE.fields_by_name['tutorials_completed'].enum_type = POGOProtos_dot_Enums_dot_TutorialState__pb2._TUTORIALSTATE
DESCRIPTOR.message_types_by_name['MarkTutorialCompleteMessage'] = _MARKTUTORIALCOMPLETEMESSAGE

MarkTutorialCompleteMessage = _reflection.GeneratedProtocolMessageType('MarkTutorialCompleteMessage', (_message.Message,), dict(
  DESCRIPTOR = _MARKTUTORIALCOMPLETEMESSAGE,
  __module__ = 'POGOProtos.Networking.Requests.Messages.MarkTutorialCompleteMessage_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Requests.Messages.MarkTutorialCompleteMessage)
  ))
_sym_db.RegisterMessage(MarkTutorialCompleteMessage)


# @@protoc_insertion_point(module_scope)
