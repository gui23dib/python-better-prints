from typing import Type, TypeVar

class TypeSpec:
    type: Type
    structchar: (str, str)
    printmask: str

    def __init__(self, type: Type, structchar: str, printmask: str):
        self.type = type
        self.structchar = structchar
        self.printmask = printmask

class TypeClass:
    TUPLE = TypeSpec(type=tuple, structchar=('(', ')'), printmask='%s: %s')
    LIST = TypeSpec(type=list, structchar=('[', ']'), printmask='[%s]: %s')
    SET: TypeSpec(type=set, structchar=('{', '}'), printmask='%s')
    DICT = TypeSpec(type=dict, structchar=('{', '}'), printmask="'%s': %s")