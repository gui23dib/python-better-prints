from main import *
from colors import *

if __name__ == '__main__':
    class Test:
        def __init__(self):
            self.__namedInstances = True
            self.a = 2
            self.b = 2
            self.c = 3
            self.d = 4
            self.e = 5
        
        def __str__(self):
            return f"{self.a}, {self.b}, {self.c}, {self.d}, {self.e}"

    test = Test()

    lista = [1, 2, 3, 4, 5]
    tupla = ((lista), 2, 5, 12, 23, 35)
    conjunto = {'asd', 2, 3.1323, 'oioi'}
    dicionario = {'a': 1123, 'b': conjunto, 'c': 353, 'd': lista, 'e': 5123}


    betterprint(test, tupla, flush=True, sep='')
    debugprint(conjunto, flush=True, sep='')
    betterprint(dicionario, flush=True, sep='')
    classprint(test, flush=True, sep='')

