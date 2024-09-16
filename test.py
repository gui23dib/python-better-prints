import betterprints as bp

if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]
    tupla = ((lista), 2, 5, 12, 23, 35)
    conjunto = {'asd', 2, 3.1323, 'oioi'}
    dicionario = {'a': 1123, 'b': conjunto, 'c': 353, 'd': lista, 'e': 5123}

    bp.betterprintsconfig.toggleNamedInstances()

    bp.debugprint(conjunto, flush=True, sep='')
    bp.betterprint(dicionario, flush=True, sep='')
