import os
from datetime import datetime, timedelta

def limpieza():
    input('Presiona Enter para continuar...')  
    os.system('cls' if os.name == 'nt' else 'clear') #funcion limpiar

def ValidarOpcion(op_minima,op_maxima):
    while True:
        try:    
            opcion = int(input(": "))
            if opcion < op_minima or opcion > op_maxima:
                print("Valor inválido, ingrese nuevamente")

            return opcion
        except ValueError:
            print("Valor inválido, ingrese nuevamente...")

def ValidarMonto(): #Valida que el monto sea un numero
    while True:
        try:
            monto = int(input("- Monto del gasto: "))
            return monto
        except ValueError:
            print("Monto inválido, digite nuevamente...")

def ValidarCantidadDescripcion(): # valida la cantidad de letras de la descripcion
    while True:
        descripcion = input("- Descripción (opcional, si no: N/A)\n (máximo 18 caracteres): ")
        if len(descripcion) <= 18:
            return descripcion
        else:
            print("Excede la cantidad máxima de caracteres, digite nuevamente")

def ValidarFecha(): #valida que la fecha de inicio sea en el formato que se dió
    while True:
        try:
            Fecha = input("-Ingrese la fecha de hoy(DD/MM/AAAA): ")
            datetime.strptime(Fecha, "%d/%m/%Y")
            return Fecha
        except ValueError:
            print("Formato inválido, ingrese nuevamente...")

def Validarlistar(op_minima,op_maxima):
    while True:
        try:    
            listar = int(input(": "))
            if listar < op_minima or listar > op_maxima:
                print("Valor inválido, ingrese nuevamente")
            return listar
        except ValueError:
            print("Valor inválido, ingrese nuevamente...")

def ValidarCategoria(op_minima,op_maxima):
    while True:
        try:    
            Categoría = int(input(": "))
            if Categoría < op_minima or Categoría > op_maxima:
                print("Valor inválido, ingrese nuevamente")
            return Categoría
        except ValueError:
            print("Valor inválido, ingrese nuevamente...")

def findCategoria(datalist, key, valor): # encuentra la categoria
    info = []
    for item in datalist:
        if item.get(key) == valor:
            info.append(item)
    return info

def ImprimirResultados(title,info): # imprime los resultados
    TEMPLATE = "{:<12}{:<22}{:<17}{:>}"
    TEMPLATE_TITLE = "{:^6}{:^22}{:^17}{:^23}"
    print(f"== {title} ==")
    print(TEMPLATE_TITLE.format("VALOR","CATEGORÍA","FECHA","DESCRIPCIÓN"))
    for gasto in info:    
        print(TEMPLATE.format(gasto["Valor"],gasto["Categoria"],gasto["Fecha"],gasto["Descripcion"]))

def ValidarFechaInicio(): #valida que la fecha de inicio sea en el formato que se dió
    while True:
        try:
            FechaInicio = input("Ingrese la fecha inicio(DD/MM/AAAA): ")
            datetime.strptime(FechaInicio, "%d/%m/%Y")
            return FechaInicio
        except ValueError:
            print("Formato inválido, ingrese nuevamente...")

def ValidarFechaFin(): #valida que la fecha fin sea en el formato que se dió
    while True:
        try:
            FechaFin = input("Ingrese la fecha fin(DD/MM/AAAA): ")
            datetime.strptime(FechaFin, "%d/%m/%Y")
            return FechaFin
        except ValueError:
            print("Formato inválido, ingrese nuevamente...")

def findFecha(datalist, key, valor): # encuentra la fecha en el archivo
    info = []
    for item in datalist:
        if item.get(key) == valor:
            info.append(item)
    return info

def ImprimirReporteFecha(FechaInicio, FechaFin, info): #imprime el reporte de la fecha
    TEMPLATE = "{:<12}{:<22}{:<17}{:>}"
    TEMPLATE_TITLE = "{:^6}{:^22}{:^17}{:^23}"
    print(f"== {FechaInicio} - {FechaFin} ==")
    print(TEMPLATE_TITLE.format("VALOR","CATEGORÍA","FECHA","DESCRIPCIÓN"))
    for gasto in info:    
        print(TEMPLATE.format(gasto["Valor"],gasto["Categoria"],gasto["Fecha"],gasto["Descripcion"]))

def ValidarTotalGastos(op_minima,op_maxima):
    while True:
        try:    
            TotalGastos = int(input(": "))
            if TotalGastos < op_minima or TotalGastos > op_maxima:
                print("Valor inválido, ingrese nuevamente")
            return TotalGastos
        except ValueError:
            print("Valor inválido, ingrese nuevamente...")        
    
def totalDiario(datalist): # calcula el total de Valor del dia
    hoy = datetime.now().strftime("%d/%m/%Y")
    total = 0

    for gasto in datalist:
        if gasto["Fecha"] == hoy:
            total += gasto["Valor"]

    print(f"Total gastado hoy ({hoy}): ${total}")
    
def totalSemanal(datalist): # calcula el total de Valor de la semana
    hoy = datetime.now()
    hace_7_dias = hoy - timedelta(days=7)

    total = 0

    for gasto in datalist:
        fecha_gasto = datetime.strptime(gasto["Fecha"], "%d/%m/%Y")
        if fecha_gasto >= hace_7_dias:
            total += gasto["Valor"]

    print(f"Total gastado en los últimos 7 días: ${total}")

def totalMensual(datalist): # calcula el total de Valor del mes 
    hoy = datetime.now()
    mesActual = hoy.month

    total = 0

    for gasto in datalist:
        fechaGasto = datetime.strptime(gasto["Fecha"], "%d/%m/%Y")

        if fechaGasto.month == mesActual:
            total += gasto["Valor"]

    print(f"Total gastado este mes: ${total}")

def ValidarReporteGastos(op_minima,op_maxima):
    while True:
        try:    
            ReporteGastos = int(input(": "))
            if ReporteGastos < op_minima or ReporteGastos > op_maxima:
                print("Valor inválido, ingrese nuevamente")
            return ReporteGastos
        except ValueError:
            print("Valor inválido, ingrese nuevamente...")

def reporteDiario(datalist):
    hoy = datetime.now().strftime("%d/%m/%Y")
    total = 0


    print("== R E P O R T E  D I A R I O ==")
    print(f"{hoy}")
    TEMPLATE = "{:<12}{:<22}{:<17}{:>}"
    TEMPLATE_TITLE = "{:^6}{:^22}{:^23}{:^}"
    print(TEMPLATE_TITLE.format("VALOR", "CATEGORÍA", "FECHA", "DESCRIPCIÓN"))

    for gasto in datalist:
        if gasto["Fecha"] == hoy:
            print(TEMPLATE.format(gasto["Valor"], gasto["Categoria"], gasto["Fecha"], gasto["Descripcion"]))
            total += gasto["Valor"]

def reporteSemanal(datalist):
    hoy = datetime.now()
    hace7dias = hoy - timedelta(days=7)
    total = 0

    print("== R E P O R T E  S E M A N A L ==")
    TEMPLATE = "{:<12}{:<22}{:<17}{:>}"
    TEMPLATE_TITLE = "{:^6}{:^22}{:^23}{:^}"
    print(TEMPLATE_TITLE.format("VALOR", "CATEGORÍA", "FECHA", "DESCRIPCIÓN"))

    for gasto in datalist:
        fechaGasto = datetime.strptime(gasto["Fecha"], "%d/%m/%Y")
        if fechaGasto >= hace7dias:
            print(TEMPLATE.format(gasto["Valor"], gasto["Categoria"], gasto["Fecha"], gasto["Descripcion"]))
            total += gasto["Valor"]

def reporteMensual(datalist):
    hoy = datetime.now()
    mesActual = hoy.month
    total = 0

    print("== R E P O R T E  M E N S U A L ==")
    TEMPLATE = "{:<12}{:<22}{:<17}{:>}"
    TEMPLATE_TITLE = "{:^6}{:^22}{:^23}{:^}"
    print(TEMPLATE_TITLE.format("VALOR", "CATEGORÍA", "FECHA", "DESCRIPCIÓN"))
    for gasto in datalist:
        fechaGasto = datetime.strptime(gasto["Fecha"], "%d/%m/%Y")

        if fechaGasto.month == mesActual:
            print(TEMPLATE.format(gasto["Valor"], gasto["Categoria"], gasto["Fecha"], gasto["Descripcion"]))
            total += gasto["Valor"]

def filtrarcategoria_y_fecha(datalist,key,valor,):
    lista = []
    for item in datalist:
        if item.get(key) == valor:
            lista.append(item)
    return lista
    