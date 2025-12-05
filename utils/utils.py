import os
from datetime import datetime, timedelta

def limpieza():
    input('Presiona Enter para continuar...')
    os.system('cls' if os.name == 'nt' else 'clear')

def findCategoria(datalist, key, valor):
    info = []
    for item in datalist:
        if item.get(key) == valor:
            info.append(item)
    return info

def findFecha(datalist, key, valor):
    info = []
    for item in datalist:
        if item.get(key) == valor:
            info.append(item)
    return info

def totalSemanal(datalist):
    hoy = datetime.now()
    hace_7_dias = hoy - timedelta(days=7)

    total = 0

    for gasto in datalist:
        fechaGasto = datetime.strptime(gasto["Fecha"], "%d/%m/%Y")
        if fechaGasto >= hace_7_dias:
            total += gasto["Valor"]

    print(f"Total gastado en los últimos 7 días: ${total}")

def totalDiario(datalist):
    hoy = datetime.now().strftime("%d/%m/%Y")
    total = 0

    for gasto in datalist:
        if gasto["Fecha"] == hoy:
            total += gasto["Valor"]

    print(f"Total gastado hoy ({hoy}): ${total}")

def totalMensual(datalist):
    hoy = datetime.now()
    mesActual = hoy.month
    añoActual = hoy.year

    total = 0

    for gasto in datalist:
        fechaGasto = datetime.strptime(gasto["Fecha"], "%d/%m/%Y")

        if fechaGasto.month == mesActual and fechaGasto.year == añoActual:
            total += gasto["Valor"]

    print(f"Total gastado este mes: ${total}")

def reporteDiario(datalist):
    hoy = datetime.now().strftime("%d/%m/%Y")
    total = 0


    print("== R E P O R T E  D I A R I O ==")
    print(f"{hoy}")
    TEMPLATE = "{:<12}{:<22}{:<17}{:>}"
    TEMPLATE_TITLE = "{:^6}{:^22}{:^23}{:^}"
    print(TEMPLATE_TITLE.format("VALOR", "CATEGORÍA", "DESCRIPCIÓN", "FECHA"))

    for gasto in datalist:
        if gasto["Fecha"] == hoy:
            print(TEMPLATE.format(gasto["Valor"], gasto["Categoria"], gasto["Descripcion"], gasto["Fecha"]))
            total += gasto["Valor"]

def reporteSemanal(datalist):
    hoy = datetime.now()
    hace7dias = hoy - timedelta(days=7)
    total = 0

    print("== R E P O R T E  S E M A N A L ==")
    TEMPLATE = "{:<12}{:<22}{:<17}{:>}"
    TEMPLATE_TITLE = "{:^6}{:^22}{:^23}{:^}"
    print(TEMPLATE_TITLE.format("VALOR", "CATEGORÍA", "DESCRIPCIÓN", "FECHA"))

    for gasto in datalist:
        fechaGasto = datetime.strptime(gasto["Fecha"], "%d/%m/%Y")
        if fechaGasto >= hace7dias:
            print(TEMPLATE.format(gasto["Valor"], gasto["Categoria"], gasto["Descripcion"], gasto["Fecha"]))
            total += gasto["Valor"]

def reporteMensual(datalist):
    hoy = datetime.now()
    mesActual = hoy.month
    total = 0

    print("== R E P O R T E  M E N S U A L ==")
    TEMPLATE = "{:<12}{:<22}{:<17}{:>}"
    TEMPLATE_TITLE = "{:^6}{:^22}{:^23}{:^}"
    print(TEMPLATE_TITLE.format("VALOR", "CATEGORÍA", "DESCRIPCIÓN", "FECHA"))
    for gasto in datalist:
        fechaGasto = datetime.strptime(gasto["Fecha"], "%d/%m/%Y")

        if fechaGasto.month == mesActual:
            print(TEMPLATE.format(gasto["Valor"], gasto["Categoria"], gasto["Descripcion"], gasto["Fecha"]))
            total += gasto["Valor"]

