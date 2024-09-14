from functions import *

if __name__ == '__main__':
    class Test:
        def __init__(self):
            self.a = 1
            self.b = 2
            self.c = 3
            self.d = 4
            self.e = 5

    test = Test()

    lista = [1, 2, 3, 4, 5]
    tupla = (2, 5, 12, 23, 35)
    tupla2 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    tupla3 = ((tupla), 2)
    conjunto = {tupla3,'asd', 2, 3.1323, 'oioi', tupla}
    conjunto2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    dicionario = {'a': 1123, 'b': conjunto, 'c': 353, 'd': lista, 'e': 5123}

    # dprint(lista, flush=True, sep='\n')
    # dprint(tupla, flush=True, sep='\n')
    dprint(conjunto2, flush=True, sep='')
    # dprint(dicionario, flush=True, sep='\n')

    #(*objects, sep=' ', end='\n', file=None, flush=False)