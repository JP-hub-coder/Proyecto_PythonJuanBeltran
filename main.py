gastos = []
from utils.utils import *
from utils.jsonFileHandler import *
GASTOS_FILE_PATH = "./Database/Gastos.json"
while True :
    limpieza()
    print("===========================================")
    print("         Simulador de Gasto Diario         ")
    print("===========================================")
    print("Seleccione una opción:\n")
    print("1. Registrar nuevo gasto")
    print("2. Listar gastos")
    print("3. Calcular total de gastos")
    print("4. Generar reporte de datos")
    print("5. SALIR")
    print("===========================================")
    opcion = int(input("=> "))
    match opcion:
        case 1:
            print("=============================================")
            print("Registrar Nuevo Gasto")
            print("=============================================")            
            print("Ingrese la información del gasto:\n")
            Gastos_a_Añadir = {
                "Valor": int(input("- Monto del gasto: ")),
                "Categoria": input("- Categoría (ej. comida, transporte, entretenimiento, otros): "),
                "Descripcion": input("- Descripción (opcional, si no: N/A):\n"),     
                "Fecha": input("-Ingrese la fecha de hoy(DD/MM/AAAA): ") 
                      }
            print("=============================================")    
            GuardarOCancelar = input("Ingrese 'S' para guardar o 'C' para cancelar\n =>").lower()
            if GuardarOCancelar == "s":
                fileGastos = readFile(GASTOS_FILE_PATH)
                fileGastos.append(Gastos_a_Añadir)
                saveFile(GASTOS_FILE_PATH,fileGastos)
                print("Gasto guardado correctamente")
            elif GuardarOCancelar == "c":
                break

        case 2:
            print("=============================================")
            print("                Listar Gastos                ")
            print("=============================================")
            print("Seleccione una opción para filtrar los gastos:\n")
            print("1. Ver todos los gastos")
            print("2. Filtrar por categoría")
            print("3. Filtrar por rango de fechas")
            print("4. Regresar al menú principal")
            print("=============================================")
            listar = int(input(": "))
            match listar:
                case 1:
                    TEMPLATE = "{:<12}{:<22}{:<17}{:>}"
                    TEMPLATE_TITLE = "{:^6}{:^22}{:^23}{:^}"

                    limpieza()
                    gastos = readFile(GASTOS_FILE_PATH)
                    print("=== G A S T O S  R E G I S T R A D O S ===")
                    print(TEMPLATE_TITLE.format("VALOR","CATEGORÍA","DESCRIPCIÓN","FECHA"))
                    for gasto in gastos :
                        print(TEMPLATE.format(gasto['Valor'],gasto['Categoria'],gasto['Descripcion'],gasto['Fecha']))
                case 2: 
                    print("==========================")
                    print("¿Que categoría desea ver?")
                    print("1. Comida")
                    print("2. Transporte")
                    print("3. Entretenimiento")
                    print("4. Otros")
                    print("5. SALIR")
                    print("==========================")
                    Categoría = int(input(": "))
                    match Categoría:
                        case 1:
                            limpieza()
                            GastoComida = "comida"
                            gastos = readFile(GASTOS_FILE_PATH)
                            info = findCategoria(gastos, "Categoria" , GastoComida)

                            TEMPLATE = "{:<12}{:<22}{:<17}{:>}"
                            TEMPLATE_TITLE = "{:^6}{:^22}{:^23}{:^}"
                            for gasto in info:
                                print("== C O M I D A S ==")
                                print(TEMPLATE_TITLE.format("VALOR","CATEGORÍA","DESCRIPCIÓN","FECHA"))
                                print(TEMPLATE.format(gasto['Valor'],gasto['Categoria'],gasto['Descripcion'],gasto['Fecha']))
                        case 2: 
                            print("Transporte:")
                        case 3:
                            print("Entretenimiento: ")
                        case 4: 
                            print("Otros:")
                case 3: 
                    input("Ingrese la fecha a filtrar(DD/MM/AAAA): ")
                    print("Filtrado: ")
                case 4:
                    break

        case 3:
            print("=============================================")
            print("          Calcular Total de Gastos           ")
            print("=============================================")
            print("Seleccione el periodo de cálculo:\n")
            print("1. Calcular total diario")
            print("2. Calcular total semanal")
            print("3. Calcular total mensual")
            print("4. Regresar al menú principal")
            print("=============================================")
            TotalGastos = int(input(":"))
            match TotalGastos:
                case 1:
                    print("Total del dia de hoy:")
                case 2: 
                    print("Total de la semana:")
                case 3:
                    print("Total del mes")
                case 4:
                    print("Saliendo...")
                    break

        case 4:
            print("=============================================")
            print("Generar Reporte de Gastos")
            print("=============================================")
            print("Seleccione el tipo de reporte:\n")
            print("1. Reporte diario")
            print("2. Reporte semanal")
            print("3. Reporte mensual")
            print("4. Regresar al menú principal")
            print("=============================================")
            ReporteGastos = int(input(":"))
            match ReporteGastos:
                case 1:
                    print("Reporte diario:")
                case 2:
                    print("Reporter semanal: ")
                case 3:
                    print("Reporte mensual: ")
                case 4:
                    print("saliendo...")
                    break                            
        case 5:
            print("==================================================")
            salir = input("Quiere salir del programa? (S/N)\n")

            if salir == "S":
                print("Gracias por usar el sistema <3")
                break
            elif salir == "N":
                print("volviendo")
