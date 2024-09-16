from functions import *
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
    tupla = (2, 5, 12, 23, 35)
    tupla2 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    tupla3 = ((lista), 2, test)
    conjunto = {'asd', 2, 3.1323, 'oioi', tupla}
    conjunto2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    dicionario = {'a': 1123, 'b': conjunto, 'c': 353, 'd': lista, 'e': 5123}



    #debugprint(test, flush=True, sep='\n')
    # debugprint(lista, flush=True, sep='\n')
    # debugprint(lista, tupla, conjunto, dicionario, "teste", 12312, flush=True, sep='')
    # debugprint(tupla, flush=True, sep='\n')
    # debugprint(tupla3, flush=True, sep='\n')

    #debugprint(conjunto, flush=True)
    #debugprint(dicionario, flush=True, sep='\n')

    # print("teste", "teste")
    # styledprint("Teste", "Teste2", "Teste3", style=Colors.FAIL, flush=True)
    # styledprint(lista, style=Colors.OKGREEN, flush=True)

    betterprint(test, tupla3, flush=True, sep='')

