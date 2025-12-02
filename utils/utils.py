import os

def limpieza():
    input('Presiona Enter para continuar...')
    os.system('cls' if os.name == 'nt' else 'clear')

def findCategoria(datalist, key, valor):
    info = {}
    for i in range(len(datalist)):
        if datalist[i].get(key) == valor:
            info["Categoria"] = datalist [i]
            break
    return info