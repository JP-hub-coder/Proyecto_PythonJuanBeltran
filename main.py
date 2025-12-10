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
    opcion = ValidarOpcion()
    match opcion:
        case 1:
            limpieza()
            print("=============================================")
            print("Registrar Nuevo Gasto")
            print("=============================================")            
            print("Ingrese la información del gasto:\n")
            # {}= diccionario
            Gastos_a_Añadir = {
                "Valor": ValidarMonto(),
                "Categoria": input("- Categoría (ej. comida, transporte, entretenimiento, otros)\n(en minúscula): ").lower().strip(),
                "Descripcion": ValidarCantidadDescripcion(),     
                "Fecha":ValidarFecha() 
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
            listar = Validarlistar()
            match listar:
                case 1:
                    limpieza()
                    TEMPLATE = "{:<12}{:<22}{:<17}{:>}"
                    TEMPLATE_TITLE = "{:^6}{:^22}{:^23}{:^}"
                    gastos = readFile(GASTOS_FILE_PATH)
                    ImprimirResultados("R E G I S T R O  D E  G A S T O S", gastos)
                case 2: 
                    print("==========================")
                    print("¿Que categoría desea ver?")
                    print("1. Comida")
                    print("2. Transporte")
                    print("3. Entretenimiento")
                    print("4. Otros")
                    print("5. SALIR")
                    print("==========================")
                    Categoria = ValidarCategoria()

                    match Categoria:
                        case 1:
                            limpieza()
                            GastoComida = "comida"
                            gastos = readFile(GASTOS_FILE_PATH)
                            info = findCategoria(gastos, "Categoria" , GastoComida)
                            ImprimirResultados("C O M I D A", info)
                        case 2: 
                            limpieza()
                            GastoTransporte = "transporte"
                            gastos = readFile(GASTOS_FILE_PATH)
                            info = findCategoria(gastos, "Categoria" , GastoTransporte)
                            ImprimirResultados("T R A N S P O R T E",info)
                        case 3:
                            limpieza()
                            GastoEntretenimiento = "entretenimiento"
                            gastos = readFile(GASTOS_FILE_PATH)
                            info = findCategoria(gastos, "Categoria" , GastoEntretenimiento)
                            ImprimirResultados("E N T R E T E N I M I E N T O", info)
                        case 4: 
                            limpieza()
                            GastoOtros = "otros"
                            gastos = readFile(GASTOS_FILE_PATH)
                            info = findCategoria(gastos, "Categoria" , GastoOtros)
                            ImprimirResultados("O T R O S", info)
                case 3:
                    FechaInicio = ValidarFechaInicio()
                    FechaFin = ValidarFechaFin()
                    fechas = readFile(GASTOS_FILE_PATH)
                    info = findFecha(fechas, "Fecha", FechaInicio)
                    info += findFecha(fechas, "Fecha", FechaFin)
                    ImprimirReporteFecha(FechaInicio, FechaFin, info)
                case 4:
                    print("Volviendo al menú...")
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
            TotalGastos = ValidarTotalGastos()
            match TotalGastos:
                case 1:
                    gastos = readFile(GASTOS_FILE_PATH)
                    totalDiario(gastos)
                case 2: 
                    gastos = readFile(GASTOS_FILE_PATH)
                    totalSemanal(gastos)
                case 3:
                    gastos = readFile(GASTOS_FILE_PATH)
                    totalMensual(gastos)
                case 4:
                    print("Saliendo...")

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
            ReporteGastos = ValidarReporteGastos()
            match ReporteGastos:
                case 1:
                    gastos = readFile(GASTOS_FILE_PATH)
                    reporteDiario(gastos)
                case 2:
                    gastos = readFile(GASTOS_FILE_PATH)
                    reporteSemanal(gastos)
                case 3:
                    gastos = readFile(GASTOS_FILE_PATH)
                    reporteMensual(gastos)
                case 4:
                    print("saliendo...")
                                                
        case 5:
            print("==================================================")
            salir = input("Quiere salir del programa? (S/N)\n")

            if salir == "S":
                print("Gracias por usar el sistema <3")
                break
            elif salir == "N":
                print("Volviendo")
