# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/lib/python/complex.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from syft.proto.core.common import (
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/lib/python/complex.proto",
    package="syft.lib.python",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1eproto/lib/python/complex.proto\x12\x0fsyft.lib.python\x1a%proto/core/common/common_object.proto"H\n\x07\x43omplex\x12\x0c\n\x04real\x18\x01 \x01(\x02\x12\x0c\n\x04imag\x18\x02 \x01(\x02\x12!\n\x02id\x18\x03 \x01(\x0b\x32\x15.syft.core.common.UIDb\x06proto3',
    dependencies=[
        proto_dot_core_dot_common_dot_common__object__pb2.DESCRIPTOR,
    ],
)


_COMPLEX = _descriptor.Descriptor(
    name="Complex",
    full_name="syft.lib.python.Complex",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="real",
            full_name="syft.lib.python.Complex.real",
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="imag",
            full_name="syft.lib.python.Complex.imag",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="id",
            full_name="syft.lib.python.Complex.id",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=90,
    serialized_end=162,
)

_COMPLEX.fields_by_name[
    "id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
DESCRIPTOR.message_types_by_name["Complex"] = _COMPLEX
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Complex = _reflection.GeneratedProtocolMessageType(
    "Complex",
    (_message.Message,),
    {
        "DESCRIPTOR": _COMPLEX,
        "__module__": "proto.lib.python.complex_pb2"
        # @@protoc_insertion_point(class_scope:syft.lib.python.Complex)
    },
)
_sym_db.RegisterMessage(Complex)


# @@protoc_insertion_point(module_scope)