# automatically generated by the FlatBuffers compiler, do not modify

# namespace: CrossParser

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ClientVec(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ClientVec()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsClientVec(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ClientVec
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ClientVec
    def ClientVec(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from CrossParser.Client import Client
            obj = Client()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ClientVec
    def ClientVecLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ClientVec
    def ClientVecIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def ClientVecStart(builder):
    builder.StartObject(1)

def Start(builder):
    ClientVecStart(builder)

def ClientVecAddClientVec(builder, clientVec):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(clientVec), 0)

def AddClientVec(builder, clientVec):
    ClientVecAddClientVec(builder, clientVec)

def ClientVecStartClientVecVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartClientVecVector(builder, numElems: int) -> int:
    return ClientVecStartClientVecVector(builder, numElems)

def ClientVecEnd(builder):
    return builder.EndObject()

def End(builder):
    return ClientVecEnd(builder)