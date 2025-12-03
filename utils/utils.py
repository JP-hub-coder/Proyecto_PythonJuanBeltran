import os

def limpieza():
    input('Presiona Enter para continuar...')
    os.system('cls' if os.name == 'nt' else 'clear')

def findCategoria(datalist, key, valor):
    info = []
    for item in datalist:
        if item.get(key) == valor:
            info.append(item)
    return info

