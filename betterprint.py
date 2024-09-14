from typing import Optional
from colors import Colors

set_nl = lambda sep: "\n" if '\n' not in sep else ""

class BetterPrint:
    __debugMode: bool = True
    __detailedPrint: bool = False
    colorScheme: Colors 

    def __init__(self, *, ColorScheme: Optional[Colors] = None):
        self.__debugMode = True
        self.colorScheme = ColorScheme or Colors

    def toggleDetailedPrint(self, isDetailedPrintMode: Optional[bool] = None):
        self.__detailedPrint = isDetailedPrintMode or not self.__detailedPrint
        print(f"{self.colorScheme.WARNING}Detailed print mode is now {self.__detailedPrint}{self.colorScheme.ENDC}")

    def toggleDebugMode(self, isDebugMode: Optional[bool] = None):
        self.__debugMode = isDebugMode or not self.__debugMode
        print(f"{self.colorScheme.WARNING}Debug mode is now {self.__debugMode}{self.colorScheme.ENDC}")

    def debug_print(self, *objects, sep=' ', end='\n', flush=False):
        if self.__debugMode == True:
            for obj in objects:
                self.betterprint(obj, end=sep)
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
                print(f"INSTANCE {type(obj)}: {obj}", end=sep)
            elif type(obj) == list:
                self.listprint(obj, end=sep)
            elif type(obj) == tuple:
                self.tupleprint(obj, end=sep)
            elif type(obj) == set:
                self.setprint(obj, end=sep)
            elif type(obj) == dict:
                self.dictprint(obj, end=sep)
            else:
                print(f"{obj}", end=sep)

        print(end=end, flush=flush)


    def listprint(self, obj, sep='\n', end='\n', flush=False):
        if type(obj) == list:
            self.styledprint("Instance of list:", style=self.colorScheme.BOLD)
            self.styledprint("[", style=self.colorScheme.BOLD)
            for i in range(len(obj)):
                self.typedprint(f"  [{i}]: {obj[i]},", end=sep)
            self.styledprint(f"{set_nl(sep)}]", style=self.colorScheme.BOLD, end=end, flush=flush)
        else:
            pass

    def tupleprint(self, obj, sep='\n', end='\n', flush=False):
        if type(obj) == tuple:
            self.styledprint("Instance of tuple:", style=self.colorScheme.BOLD)
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
                self.typedprint(f"  {i},", end=sep)
            self.styledprint(f"{set_nl(sep)}", "}", style=self.colorScheme.BOLD, end=end, flush=flush)
        else:
            pass

    def dictprint(self, obj, sep='\n', end='\n', flush=False):
        if type(obj) == dict:
            self.styledprint("Instance of dict:", style=self.colorScheme.BOLD)
            self.styledprint("{", style=self.colorScheme.BOLD)
            for key, value in obj.items():
                self.typedprint(f"  '{key}': {value},", end=sep)
            self.styledprint(f"{set_nl(sep)}", "}", style=self.colorScheme.BOLD, end=end, flush=flush)
        else:
            pass