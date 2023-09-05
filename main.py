from Lista_Pieza import Lista_Pieza

manejador_tablero=Lista_Pieza()

def menu_principal():
    print("--------------------------------------------------")
    print("Guatematel – Colorealo                            ")
    print("--------------------------------------------------")
    print("1. Crear Tablero                                  ")
    print("2. Mostrar Datos Del Estudiante                   ")
    print("3. Salir                                          ")
    print("--------------------------------------------------")
    opcion = input("Ingrese Una Opción: ")
    if opcion == "1":
        crear_tablero()
    elif  opcion == "2":
        mostrar_datos_estudiante()
    elif opcion == "3":
        salir()
    else:
        print("--------------------------------------------------")
        print("Opción No Válida")
        menu_principal()

def crear_tablero():
    print("--------------------------------------------------")
    print("CREAR TABLERO                                     ")
    print("--------------------------------------------------")
    print("Creación De Filas Y Columnas Del Tablero.         ")
    print("-----------------------------------------")
    print("")
    m_fila=input("Ingrese el número de filas(M): ")
    n_columna=input("Ingrese el número de columnas(N): ")
    manejador_tablero.inicializar_tablero(int(m_fila),int(n_columna))
    print("")
    print("-----------------------------------------")
    print("Agregar Una Pieza Al Tablero             ")
    print("-----------------------------------------")
    print("")
    manejador_tablero.m_filas=int(m_fila)
    manejador_tablero.n_columnas=int(n_columna)
    nueva_pieza=True
    while nueva_pieza:
        print("Colores Disponibles:")
        print("Azul")
        print("Rojo")
        print("Verde")
        print("Purpura")
        print("Naranja")
        print("")
        letra=input("Ingrese el color de la pieza: ")
        if letra=="Azul":
            color="|A|"
            fila=input("Ingrese el número de fila de la pieza: ")
            columna=input("Ingrese el número de columna de la pieza: ")
            manejador_tablero.actualizar_tablero(int(fila),int(columna),color)
        elif letra=="Rojo":
            color="|R|"
            fila=input("Ingrese el número de fila de la pieza: ")
            columna=input("Ingrese el número de columna de la pieza: ")
            manejador_tablero.actualizar_tablero(int(fila),int(columna),color)
        elif letra=="Verde":
            color="|V|"
            fila=input("Ingrese el número de fila de la pieza: ")
            columna=input("Ingrese el número de columna de la pieza: ")
            manejador_tablero.actualizar_tablero(int(fila),int(columna),color)
        elif letra=="Purpura":
            color="|P|"
            fila=input("Ingrese el número de fila de la pieza: ")
            columna=input("Ingrese el número de columna de la pieza: ")
            manejador_tablero.actualizar_tablero(int(fila),int(columna),color)
        elif letra=="Naranja":
            color="|N|"
            fila=input("Ingrese el número de fila de la pieza: ")
            columna=input("Ingrese el número de columna de la pieza: ")
            manejador_tablero.actualizar_tablero(int(fila),int(columna),color)
        print("")
        manejador_tablero.imprimir_tablero()

        print("¿Desea Agregar Otra Pieza al Tablero?")
        print("1. Sí")
        print("2. No")
        respuesta=input("Ingrese una Opción: ")
        if respuesta=="2":
            nueva_pieza=False
        else:
            print("-------------------------------")
            print("")

    print("--------------------------------------------------")
    manejador_tablero.graficar()
    print("--------------------------------------")         
    print("¿Desea realizar otra operación?")
    print("1. Sí")
    print("2. No")
    print("--------------------------------------")
    opcion = input("Ingrese Una Opción: ")
    if opcion=="1":
        menu_principal()
    elif opcion=="2":
        salir()  
    else:
        print("--------------------------------------------------")
        print("Opción No Válida")
        menu_principal()
    print("--------------------------------------------------")

def mostrar_datos_estudiante():
    print("--------------------------------------------------")
    print("Carlos Manuel Lima y Lima                         ")
    print("202201524                                         ")
    print("Introducción a la Programación y Computación 2    ")
    print("Ingeniería en Ciencias y Sistemas                 ")
    print("Cuarto Semestre, 2023                            ")
    print("--------------------------------------------------")
    print("--------------------------------------")         
    print("¿Desea realizar otra operación?")
    print("1. Sí")
    print("2. No")
    print("--------------------------------------")
    opcion = input("Ingrese Una Opción: ")
    if opcion=="1":
        menu_principal()
    elif opcion=="2":
        salir()  
    else:
        print("--------------------------------------------------")
        print("Opción No Válida")
        menu_principal()
    print("--------------------------------------------------")

def salir():
    print("Gracias por utilizar el programa.                 ")
    print("--------------------------------------------------")

if __name__=="__main__":
    print("--------------------------------------------------")
    print("Práctica 1 – Tablero                              ")
    menu_principal()  