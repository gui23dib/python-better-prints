from typing import Optional, Type, TypeVar
from colors import Colors
from typeclasses import TypeSpec, TypeClass, TypeDict

class BetterPrint:
    __debugMode: bool = True
    __detailedPrint: bool = False
    __namedInstances: bool = False
    namedInstancesLevel: int = 0
    valueSeparatorCharacter = ','

    __indentlevel: int = 0
    indentchar: str = "  "
    colorScheme: Colors 

    def __init__(self, *, ColorScheme: Optional[Colors] = None):
        self.__debugMode = True
        self.colorScheme = ColorScheme or Colors
        self.typedicts = TypeDict

    def toggleNamedInstances(self, isNamedInstances: Optional[bool] = None):
        self.__namedInstances = isNamedInstances or not self.__namedInstances
        print(f"{self.colorScheme.WARNING}Named instances is now {self.__namedInstances}{self.colorScheme.ENDC}")

    def toggleDetailedPrint(self, isDetailedPrintMode: Optional[bool] = None):
        self.__detailedPrint = isDetailedPrintMode or not self.__detailedPrint
        print(f"{self.colorScheme.WARNING}Detailed print mode is now {self.__detailedPrint}{self.colorScheme.ENDC}")

    def toggleDebugMode(self, isDebugMode: Optional[bool] = None):
        self.__debugMode = isDebugMode or not self.__debugMode
        print(f"{self.colorScheme.WARNING}Debug mode is now {self.__debugMode}{self.colorScheme.ENDC}")

    def better_print(self, *objects, sep=' ', end='\n', flush=False):
        for obj in objects:
            self.typedprint(obj, end=sep)
        print(end=end, flush=flush)

    def debug_print(self, *objects, sep=' ', end='\n', flush=False):
        if self.__debugMode == True:
            self.better_print(*objects, sep=sep, end=end, flush=flush)

    def styledprint(
        self, 
        *objects, 
        sep='', 
        end='\n', 
        flush=False, 
        style: Colors = None
    ):
        for obj in objects:
            if style:
                print(f"{style}{obj}{self.colorScheme.ENDC}", end=sep)
            else:
                print(f"{obj}", end=sep)
        print(end=end, flush=flush)

    def typedprint(self, *objects, sep='', end='\n', flush=False):
        for obj in objects:
            if obj.__class__.__module__ != 'builtins': # check if the object is a user-defined class
                print("NOT BUILTIN") # todo: implement this not builtin class print
                pass
            else: self.typespecificprint(self.typedicts.get(type(obj)), obj, end=sep, sep='\n')
        print(end=end, flush=flush)

    def typespecificprint(
        self,
        typeval: TypeSpec = None, 
        *obj, 
        sep: str = '',
        end: str = '\n', 
        flush: bool = False,
        style: Colors = None
    ) -> None:
        sep += '\n' if '\n' not in sep else ''
        ident = self.indentchar * self.__indentlevel

        if(typeval == None): 
            for i in obj:
                self.styledprint(
                    ident, f"{i}{self.valueSeparatorCharacter}",  
                    style=style or self.colorScheme.OKCYAN
                )
        else:
            self.__indentlevel += 1

            if self.__namedInstances and (self.namedInstancesLevel + 1) >= self.__indentlevel: 
                self.styledprint(
                    ident, f"Instance of {typeval.typename}:", 
                    style=style or self.colorScheme.UNDERLINE,
                )

            self.styledprint(
                ident, f"{typeval.structchar[0]}", 
                style=style or self.colorScheme.BOLD
            )
            for i in obj: 
                objtype = type(i)
                if objtype == dict:
                    for key, value in i.items():
                        self.typespecificprint(None, ident, f"'{key}': {value}", sep=sep, end=end, style=style)
                        # if self.typedicts.get(type(value)) != None:
                        #     self.typespecificprint(None, self.typedicts.get(type(value)), ident, value, sep=sep, end=end)

                # elif type(i) in [str, int, float, bool]: 
                #     self.styledprint(ident, f"{self.indentchar}{i},", end=sep, style=style)
                else:
                    if objtype in [list, tuple, set]:
                        for j in i:
                            self.typespecificprint(self.typedicts.get(type(j)), j, sep=sep, end=sep, style=style)
                    else:
                        self.typespecificprint(self.typedicts.get(objtype), i, sep=sep, end=sep, style=style)
            self.styledprint(
                f"{ident}{typeval.structchar[1]}", 
                style=style or self.colorScheme.BOLD, 
                sep=sep,
                end=end, 
                flush=flush
            )
            
            self.__indentlevel -= 1