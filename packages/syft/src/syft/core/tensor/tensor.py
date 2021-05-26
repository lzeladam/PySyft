# future
from __future__ import annotations

# third party
from google.protobuf.reflection import GeneratedProtocolMessageType
import numpy as np
import torch as th

# syft relative
from ...core.common.serde.serializable import Serializable
from ...lib.util import full_name_with_name
from ...proto.core.tensor.tensor_pb2 import Tensor as Tensor_PB
from ..common.serde.deserialize import _deserialize as deserialize
from ..common.serde.serializable import bind_protobuf
from ..common.serde.serialize import _serialize as serialize
from .ancestors import AutogradTensorAncestor
from .ancestors import PhiTensorAncestor
from .passthrough import HANDLED_FUNCTIONS
from .passthrough import PassthroughTensor


@bind_protobuf
class Tensor(
    PassthroughTensor, AutogradTensorAncestor, PhiTensorAncestor, Serializable
):
    def __init__(self, child):
        """data must be a list of numpy array"""

        if isinstance(child, list):
            child = np.array(child)

        if isinstance(child, th.Tensor):
            child = child.numpy()

        if not isinstance(child, PassthroughTensor) and not isinstance(
            child, np.ndarray
        ):
            raise Exception("Data must be list or nd.array")

        super().__init__(child=child)

    def new_with_child(self, child) -> Tensor:
        return Tensor(child)

    def __array_function__(self, func, types, args, kwargs):
        #         args, kwargs = inputs2child(*args, **kwargs)

        # Note: this allows subclasses that don't override
        # __array_function__ to handle PassthroughTensor objects.
        if not all(issubclass(t, self.__class__) for t in types):
            return NotImplemented

        if func in HANDLED_FUNCTIONS[self.__class__]:
            return HANDLED_FUNCTIONS[self.__class__][func](*args, **kwargs)
        else:
            return self.__class__(func(*args, **kwargs))

    def _object2proto(self) -> Tensor_PB:
        print("Serializing Tensor")
        print(f"Child {type(self.child)}")
        arrays = []
        tensors = []
        if isinstance(self.child, np.ndarray):
            use_tensors = False
            arrays = [serialize(self.child)]
        else:
            use_tensors = True
            tensors = [serialize(self.child)]

        return Tensor_PB(
            obj_type=full_name_with_name(klass=type(self)),
            use_tensors=use_tensors,
            arrays=arrays,
            tensors=tensors,
        )

    @staticmethod
    def _proto2object(proto: Tensor_PB) -> Tensor:
        use_tensors = proto.use_tensors
        child = []
        if use_tensors:
            child = [deserialize(tensor) for tensor in proto.tensors]
        else:
            child = [deserialize(array) for array in proto.arrays]

        child = child[0]
        print("Deserializing Tensor")
        print(f"Child {type(child)}")
        return Tensor(child)

    @staticmethod
    def get_protobuf_schema() -> GeneratedProtocolMessageType:
        return Tensor_PB