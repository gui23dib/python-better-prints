from typing import Optional, Type, TypeVar
from colors import Colors

class TypeSpec:
    typename: type
    structchar: (str, str)
    printmask: str

    def __init__(self, typename: type, structchar: str, printmask: str):
        self.typename = typename
        self.structchar = structchar
        self.printmask = printmask

class TypeClass:
    TUPLE: TypeSpec = TypeSpec(typename=tuple, structchar=('(', ')'), printmask='%s: %s')
    LIST: TypeSpec = TypeSpec(typename=list, structchar=('[', ']'), printmask='[%s]: %s')
    SET: TypeSpec = TypeSpec(typename=set, structchar=('{', '}'), printmask='%s')
    DICT: TypeSpec = TypeSpec(typename=dict, structchar=('{', '}'), printmask="'%s': %s")

set_nl = lambda sep: "\n" if '\n' not in sep else ""

class BetterPrint:
    __debugMode: bool = True
    __detailedPrint: bool = False
    __namedInstances: bool = False

    __indentlevel: int = 0
    indentchar: str = "  "
    colorScheme: Colors 

    def __init__(self, *, ColorScheme: Optional[Colors] = None):
        self.__debugMode = True
        self.colorScheme = ColorScheme or Colors

    def toggleNamedInstances(self, isNamedInstances: Optional[bool] = None):
        self.__namedInstances = isNamedInstances or not self.__namedInstances
        print(f"{self.colorScheme.WARNING}Named instances is now {self.__namedInstances}{self.colorScheme.ENDC}")

    def toggleDetailedPrint(self, isDetailedPrintMode: Optional[bool] = None):
        self.__detailedPrint = isDetailedPrintMode or not self.__detailedPrint
        print(f"{self.colorScheme.WARNING}Detailed print mode is now {self.__detailedPrint}{self.colorScheme.ENDC}")

    def toggleDebugMode(self, isDebugMode: Optional[bool] = None):
        self.__debugMode = isDebugMode or not self.__debugMode
        print(f"{self.colorScheme.WARNING}Debug mode is now {self.__debugMode}{self.colorScheme.ENDC}")

    def debug_print(self, *objects, sep=' ', end='\n', flush=False):
        if self.__debugMode == True:
            for obj in objects:
                self.typedprint(TypeClass.SET ,obj, end=sep)
            print(end=end, flush=flush)

    # def betterprint(self, *objects, sep='', end='\n', flush=False):
    #     for obj in objects:
    #         self.typedprint(obj, end=sep)
    #     print(end=end, flush=flush)

    def styledprint(self, *objects, sep='', end='\n', flush=False, style=None):
        for obj in objects:
            if style:
                print(f"{style}{obj}{self.colorScheme.ENDC}", end=sep)
            else:
                print(f"{obj}", end=sep)
        print(end=end, flush=flush)

    def typedprint(self, *objects, sep='', end='\n', flush=False):
        for obj in objects:
            if obj.__class__.__module__ != 'builtins': # check if the object is a user-defined class
                # print(f"INSTANCE {type(obj)}: {obj}", end=sep)
                pass
            elif type(obj) == list:
                self.listprint(obj, end=sep)
            elif type(obj) == tuple:
                self.typespecificprint(TypeClass.TUPLE, obj, end=sep)
            elif type(obj) == set:
                self.typespecificprint(TypeClass.SET, obj, end=sep)
            elif type(obj) == dict:
                self.dictprint(obj, end=sep)
            else:
                print(f"{obj}", end=sep)

        print(end=end, flush=flush)

    def typespecificprint(
        self,
        typeval: TypeSpec = TypeClass.LIST, 
        *obj, 
        sep: str = '\n', #TODO: Change this to a default value of '\n' if the type is a list
        end: str = '\n', 
        flush: bool = False
    ) -> None:
        if True: #type(obj) == typeval.typename:
            ident = self.indentchar * self.__indentlevel
            self.__indentlevel += 1

            if self.__namedInstances: self.styledprint(
                ident, f"Instance of TESTE:", 
                style=self.colorScheme.BOLD
            )

            self.styledprint(
                ident, f"{typeval.structchar[0]}", 
                style=self.colorScheme.BOLD
            )
            for i in obj: 
                for j in i:
                    if type(j) in [list, tuple, set, dict]:
                        self.typespecificprint(TypeClass.TUPLE, j, sep=sep, end=sep)
                    else: self.styledprint(ident, f"{self.indentchar}{j},", end=sep)
            self.styledprint(
                ident, f"{set_nl(sep)}", 
                f"{typeval.structchar[0]}", 
                style=self.colorScheme.BOLD, 
                end=end, 
                flush=flush
            )
        
        else:
            pass

    def listprint(self, obj, sep='\n', end='\n', flush=False):
        if type(obj) == list:
            if self.__namedInstances: self.styledprint("Instance of list:", style=self.colorScheme.BOLD)
            self.styledprint("[", style=self.colorScheme.BOLD)
            for i in range(len(obj)):
                self.styledprint(f"  [{i}]: {self.typedprint(obj[i])},", end=sep)
            self.styledprint(f"{set_nl(sep)}]", style=self.colorScheme.BOLD, end=end, flush=flush)
        else:
            pass

    def tupleprint(self, obj, sep='\n', end='\n', flush=False):
        if type(obj) == tuple:
            if self.__namedInstances: self.styledprint("Instance of tuple:", style=self.colorScheme.BOLD)
            self.styledprint("(", style=self.colorScheme.BOLD)
            for i in range(len(obj)):
                self.typedprint(f"  {i}: {obj[i]},", end=sep)
            
            self.styledprint(f"{set_nl(sep)})", style=self.colorScheme.BOLD, end=end, flush=flush)
        else:
            pass

    def setprint(self, obj, sep='\n', end='\n', flush=False):
        if type(obj) == set:
            self.styledprint("Instance of set:", style=self.colorScheme.BOLD)
            self.styledprint("{", style=self.colorScheme.BOLD)
            for i in obj:
                self.styledprint(f" {self.typedprint(i) or ''},", end=sep)
            self.styledprint(f"{set_nl(sep)}", "}", style=self.colorScheme.BOLD, end=end, flush=flush)
        else:
            pass

    def dictprint(self, obj, sep='\n', end='\n', flush=False):
        if type(obj) == dict:
            if self.__namedInstances: self.styledprint("Instance of dict:", style=self.colorScheme.BOLD)
            self.styledprint("{", style=self.colorScheme.BOLD)
            for key, value in obj.items():
                self.typedprint(f"  '{key}': {value},", end=sep)
            self.styledprint(f"{set_nl(sep)}", "}", style=self.colorScheme.BOLD, end=end, flush=flush)
        else:
            pass