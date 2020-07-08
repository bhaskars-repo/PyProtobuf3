# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Account2.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Customer2_pb2 as Customer2__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Account2.proto',
  package='com.polarsparc.protobuf3.modular',
  syntax='proto3',
  serialized_options=_b('B\013AccountInfoP\001'),
  serialized_pb=_b('\n\x0e\x41\x63\x63ount2.proto\x12 com.polarsparc.protobuf3.modular\x1a\x0f\x43ustomer2.proto\"\x9d\x01\n\x08\x41\x63\x63ount2\x12\x0f\n\x07\x61\x63\x63t_no\x18\x01 \x01(\t\x12\x41\n\tacct_type\x18\x02 \x01(\x0e\x32..com.polarsparc.protobuf3.modular.AccountType2\x12=\n\x08\x63ustomer\x18\x03 \x01(\x0b\x32+.com.polarsparc.protobuf3.modular.Customer2*Q\n\x0c\x41\x63\x63ountType2\x12\x0e\n\nAT_UNKNOWN\x10\x00\x12\x0e\n\nAT_SAVINGS\x10\x01\x12\x0f\n\x0b\x41T_CHECKING\x10\x02\x12\x10\n\x0c\x41T_BROKERAGE\x10\x03\x42\x0f\x42\x0b\x41\x63\x63ountInfoP\x01\x62\x06proto3')
  ,
  dependencies=[Customer2__pb2.DESCRIPTOR,])

_ACCOUNTTYPE2 = _descriptor.EnumDescriptor(
  name='AccountType2',
  full_name='com.polarsparc.protobuf3.modular.AccountType2',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AT_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AT_SAVINGS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AT_CHECKING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AT_BROKERAGE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=229,
  serialized_end=310,
)
_sym_db.RegisterEnumDescriptor(_ACCOUNTTYPE2)

AccountType2 = enum_type_wrapper.EnumTypeWrapper(_ACCOUNTTYPE2)
AT_UNKNOWN = 0
AT_SAVINGS = 1
AT_CHECKING = 2
AT_BROKERAGE = 3



_ACCOUNT2 = _descriptor.Descriptor(
  name='Account2',
  full_name='com.polarsparc.protobuf3.modular.Account2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='acct_no', full_name='com.polarsparc.protobuf3.modular.Account2.acct_no', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acct_type', full_name='com.polarsparc.protobuf3.modular.Account2.acct_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='customer', full_name='com.polarsparc.protobuf3.modular.Account2.customer', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=227,
)

_ACCOUNT2.fields_by_name['acct_type'].enum_type = _ACCOUNTTYPE2
_ACCOUNT2.fields_by_name['customer'].message_type = Customer2__pb2._CUSTOMER2
DESCRIPTOR.message_types_by_name['Account2'] = _ACCOUNT2
DESCRIPTOR.enum_types_by_name['AccountType2'] = _ACCOUNTTYPE2
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Account2 = _reflection.GeneratedProtocolMessageType('Account2', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNT2,
  __module__ = 'Account2_pb2'
  # @@protoc_insertion_point(class_scope:com.polarsparc.protobuf3.modular.Account2)
  ))
_sym_db.RegisterMessage(Account2)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
