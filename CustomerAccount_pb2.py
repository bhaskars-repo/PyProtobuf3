# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CustomerAccount.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='CustomerAccount.proto',
  package='com.polarsparc.protobuf3',
  syntax='proto3',
  serialized_options=_b('B\017CustomerAccount'),
  serialized_pb=_b('\n\x15\x43ustomerAccount.proto\x12\x18\x63om.polarsparc.protobuf3\"b\n\x08\x43ustomer\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t\x12\x10\n\x08\x65mail_id\x18\x03 \x01(\t\x12\x0b\n\x03\x61ge\x18\x04 \x01(\x05\x12\x10\n\x08phone_no\x18\x05 \x03(\t\"\x8a\x01\n\x07\x41\x63\x63ount\x12\x0f\n\x07\x61\x63\x63t_no\x18\x01 \x01(\t\x12\x38\n\tacct_type\x18\x02 \x01(\x0e\x32%.com.polarsparc.protobuf3.AccountType\x12\x34\n\x08\x63ustomer\x18\x03 \x01(\x0b\x32\".com.polarsparc.protobuf3.Customer*7\n\x0b\x41\x63\x63ountType\x12\x0b\n\x07SAVINGS\x10\x00\x12\x0c\n\x08\x43HECKING\x10\x01\x12\r\n\tBROKERAGE\x10\x02\x42\x11\x42\x0f\x43ustomerAccountb\x06proto3')
)

_ACCOUNTTYPE = _descriptor.EnumDescriptor(
  name='AccountType',
  full_name='com.polarsparc.protobuf3.AccountType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SAVINGS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHECKING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BROKERAGE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=292,
  serialized_end=347,
)
_sym_db.RegisterEnumDescriptor(_ACCOUNTTYPE)

AccountType = enum_type_wrapper.EnumTypeWrapper(_ACCOUNTTYPE)
SAVINGS = 0
CHECKING = 1
BROKERAGE = 2



_CUSTOMER = _descriptor.Descriptor(
  name='Customer',
  full_name='com.polarsparc.protobuf3.Customer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_name', full_name='com.polarsparc.protobuf3.Customer.first_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='com.polarsparc.protobuf3.Customer.last_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email_id', full_name='com.polarsparc.protobuf3.Customer.email_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='age', full_name='com.polarsparc.protobuf3.Customer.age', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phone_no', full_name='com.polarsparc.protobuf3.Customer.phone_no', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=51,
  serialized_end=149,
)


_ACCOUNT = _descriptor.Descriptor(
  name='Account',
  full_name='com.polarsparc.protobuf3.Account',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='acct_no', full_name='com.polarsparc.protobuf3.Account.acct_no', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acct_type', full_name='com.polarsparc.protobuf3.Account.acct_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='customer', full_name='com.polarsparc.protobuf3.Account.customer', index=2,
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
  serialized_start=152,
  serialized_end=290,
)

_ACCOUNT.fields_by_name['acct_type'].enum_type = _ACCOUNTTYPE
_ACCOUNT.fields_by_name['customer'].message_type = _CUSTOMER
DESCRIPTOR.message_types_by_name['Customer'] = _CUSTOMER
DESCRIPTOR.message_types_by_name['Account'] = _ACCOUNT
DESCRIPTOR.enum_types_by_name['AccountType'] = _ACCOUNTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Customer = _reflection.GeneratedProtocolMessageType('Customer', (_message.Message,), dict(
  DESCRIPTOR = _CUSTOMER,
  __module__ = 'CustomerAccount_pb2'
  # @@protoc_insertion_point(class_scope:com.polarsparc.protobuf3.Customer)
  ))
_sym_db.RegisterMessage(Customer)

Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNT,
  __module__ = 'CustomerAccount_pb2'
  # @@protoc_insertion_point(class_scope:com.polarsparc.protobuf3.Account)
  ))
_sym_db.RegisterMessage(Account)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)