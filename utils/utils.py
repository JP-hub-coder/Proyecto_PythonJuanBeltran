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

def totalSemanal(lista):
    hoy = datetime.now()
    hace_7_dias = hoy - timedelta(days=7)

    total = 0

    for gasto in lista:
        fecha_gasto = datetime.strptime(gasto["Fecha"], "%d/%m/%Y")
        if fecha_gasto >= hace_7_dias:
            total += gasto["Valor"]

    print(f"Total gastado en los últimos 7 días: ${total}")

def totalDiario(lista):
    hoy = datetime.now().strftime("%d/%m/%Y")
    total = 0

    for gasto in lista:
        if gasto["Fecha"] == hoy:
            total += gasto["Valor"]

    print(f"Total gastado HOY ({hoy}): ${total}")

def totalMensual(lista):
    hoy = datetime.now()
    mesActual = hoy.month
    añoActual = hoy.year

    total = 0

    for gasto in lista:
        fechaGasto = datetime.strptime(gasto["Fecha"], "%d/%m/%Y")

        if fechaGasto.month == mesActual and fechaGasto.year == añoActual:
            total += gasto["Valor"]

    print(f"Total gastado este mes: ${total}")
