from struct import unpack_from, calcsize


class Types:
    char = "c"
    int8 = "b"
    uint8 = "B"
    int16 = "h"
    uint16 = "H"
    int32 = "i"
    uint32 = "I"
    int64 = "q"
    uint64 = "Q"
    float = "f"
    double = "d"


class BinaryReader:
    def __init__(self, stream, offset, order="<"):
        self.stream = stream + b" "
        self.offset = offset
        self.order = order

    def jump(self, offset):
        reader = BinaryReader(self.stream, offset, self.order)
        return reader

    def read(self, pattern):
        size = calcsize(pattern)
        data = unpack_from(self.order + pattern, self.stream, self.offset)
        self.offset += size
        return data[0]


def read_a(reader):
    a1 = [read_b(reader) for _ in range(6)]
    a2 = reader.read(Types.uint64)
    a3 = reader.read(Types.double)
    a4_offset = reader.read(Types.uint32)
    a4_reader = reader.jump(a4_offset)
    a4 = read_c(a4_reader)
    a5 = reader.read(Types.uint16)
    a6 = reader.read(Types.int32)
    a7 = read_f(reader)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7)


def read_b(reader):
    b1 = ''.join([reader.read(Types.char).decode('utf-8') for _ in range(3)])
    b2 = reader.read(Types.uint8)
    b3 = reader.read(Types.uint16)
    return dict(B1=b1, B2=b2, B3=b3)


def read_c(reader):
    c1 = reader.read(Types.int16)
    c2_offset = reader.read(Types.uint16)
    c2_reader = reader.jump(c2_offset)
    c2 = read_d(c2_reader)
    c3 = read_e(reader)
    c4 = reader.read(Types.uint16)
    return dict(C1=c1, C2=c2, C3=c3, C4=c4)


def read_d(reader):
    d1 = reader.read(Types.int32)
    d2 = reader.read(Types.int32)
    return dict(D1=d1, D2=d2)


def read_e(reader):
    e1 = reader.read(Types.double)
    e2 = [reader.read(Types.int64) for _ in range(5)]
    e3 = [reader.read(Types.int8) for _ in range(4)]
    return dict(E1=e1, E2=e2, E3=e3)


def read_f(reader):
    f1 = reader.read(Types.int8)
    f2 = reader.read(Types.int64)
    return dict(F1=f1, F2=f2)


def main(stream):
    return read_a(BinaryReader(stream, 4))
