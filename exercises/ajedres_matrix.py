import os
os.system('cls')

creatrix = False


#!Problema Pricipal: Listas con mismo ID!
#*Solución: Crear objetos con ID's distintos!

initMatrix = []

def createMatrix():

    x = int(input("   Ingresa Número de [ Filas ]: "))
    y = int(input("   Ingresa Número de [ Columnas ]: "))
    print()

    for z in range(x):
        intro = []
        for x in range(y):
            intro.append("w")
        initMatrix.append(intro)

def logic():

    for audi in range(len(initMatrix)):
        for lamborguini in range(len(initMatrix[0])):

            if audi % 2 == 0:
                initMatrix[audi][lamborguini] = "0" if lamborguini % 2 == 0 else "1"

            else:
                initMatrix[audi][lamborguini] = "1" if lamborguini % 2 == 0 else "0"
logic()   


def show():

    for z in range(len(initMatrix)):
        print(end=f"\nF{z + 1}. ")

        for w in range(len(initMatrix[0])):

            if w % 2 == 0:
                print(end=f"| {initMatrix[z][w]} |")

            elif w == len(initMatrix[z]) - 1:
                print(end=f" {initMatrix[z][w]} |")

            elif w % 2 == 1:
                print(end=f" {initMatrix[z][w]} ")

        if z == len(initMatrix) - 1:
            print()
show()


def positicionMatrix(): 

    print("\nBuscar Posición Matricial!")

        
    x = int(input("\nIngresa Posición [FILA]: "))
    y = int(input("Ingresa Posición [COLUMNA]: "))

    if x <= len(initMatrix) and y <= len(initMatrix[0]):
        for camaro in range(len(initMatrix)):
            for astonMartin in range(len(initMatrix[0])):

                value = initMatrix[camaro][astonMartin]
                initMatrix[camaro][astonMartin] = value if camaro == (x - 1) and astonMartin == (y - 1) else "-"
        show()
        print(f"[{x}, {y}]")   
    
    else:
        print("\nIngresa Rangos Permitidos!")

    logic()

def triquiGame():

    pass

        


print("-- Eventos con la Matriz --\n")
while True:

    if creatrix:
        print("1). Juego Triqui\n2). Consulatar Posición Matricial\n3). Mostrar Matriz\n4). Salir")
        selection = int(input("Elige Opción: "))
        print()

        if selection == 1:
            #! TRIQUI GAME
            print("Juego Triqui! - Persona vs Computadora.\n")
            pass

        elif selection == 2:
            positicionMatrix()
            show()
            print()

        elif selection == 3:
            show()
            print()
        
        elif selection == 4:
            break

    else:
        print(" -- Crear Matriz --")

        createMatrix()
        logic()
        creatrix = True

print("Saliendo...")