import os
import random as rd
os.system('cls')

creatrix = False
changer = True

#!Problema Pricipal: Listas con mismo ID!
#*Solución: Crear objetos con ID's distintos!

initMatrix = []
triquiMatrix = []

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


def show(matrix):

    for z in range(len(matrix)):
        print(end=f"\nF{z + 1}. ")

        for w in range(len(matrix[0])):

            if w % 2 == 0:
                print(end=f"| {matrix[z][w]} |")

            elif w == len(matrix[z]) - 1:
                print(end=f" {matrix[z][w]} |")

            elif w % 2 == 1:
                print(end=f" {matrix[z][w]} ")

        if z == len(matrix) - 1:
            print()


def positicionMatrix(): 

    print("\nBuscar Posición Matricial!")

        
    x = int(input("\nIngresa Posición [FILA]: "))
    y = int(input("Ingresa Posición [COLUMNA]: "))

    if x <= len(initMatrix) and y <= len(initMatrix[0]):
        for camaro in range(len(initMatrix)):
            for astonMartin in range(len(initMatrix[0])):

                value = initMatrix[camaro][astonMartin]
                initMatrix[camaro][astonMartin] = value if camaro == (x - 1) and astonMartin == (y - 1) else "-"
        show(initMatrix)
        print(f"[{x}, {y}]")   
    
    else:
        print("\nIngresa Rangos Permitidos!")

    logic()



def createTriqui():

    for z in range(3):
        intro = []
        for x in range(3):
            intro.append(" ")
        triquiMatrix.append(intro)


def triquiLogicPerson(matrix):

    b = True
    found = False

    while b:

        row = int(input("Ingresa la Posición [FILA]: "))
        column = int(input("Ingresa la posición [COLUMNA]: "))

        for audi in range(len(matrix)):
            for toyota in range(len(matrix[0])):

                if row <= len(matrix) and column <= len(matrix[0]):

                    if audi == row - 1 and toyota == column - 1 and matrix[audi][toyota] == " ":
                        matrix[audi][toyota] = "o"
                        b = False

                    elif audi == row - 1 and toyota == column - 1 and matrix[audi][toyota] != " ":
                        print("\nEspacio Ocupado")
                        show(triquiMatrix)

                elif row >= len(matrix) or column >= len(matrix[0]):
                        print("\nRangos no Permitidos!\n")
                        found = True
                        break
            if found:
                break

    found = False
    show(triquiMatrix)


def triquiLogicPc(matrix):

    found = False
    b = True
    while b:

        valueRow = rd.randint(1, 3)
        valueColumn = rd.randint(1, 3)

        for musthang in range(len(matrix)):
            for aventador in range(len(matrix[0])):
                
                if musthang == valueRow - 1 and aventador == valueColumn - 1 and matrix[musthang][aventador] == " ":
                    matrix[musthang][aventador] = "x"
                    b = False

                elif musthang == valueRow - 1 and aventador == valueColumn - 1 and matrix[musthang][aventador] != " ":
                    found = True
                    break

            if found:
                break

    found = False
    show(triquiMatrix)


def turn(bool: bool, increase: int):

    while True:
        increase += 1

        if bool:
            print(f"\nTurno [ {increase} ] Persona!")
        
            triquiLogicPerson(triquiMatrix)

            bool = False

        else:
            print(f"\nTurno [ {increase} ] Computadora!")

            triquiLogicPc(triquiMatrix)
            
            bool = True


def triquiGame(bool: bool):

    increase = 1

    print("Sorteo de Turno Inicial: ")
    print("Cara -> 1 / Cruz -> 0")

    person = int(input("Selecciona: "))
    numberS = rd.randint(0, 1)

    createTriqui()
    show(triquiMatrix)
    print()

    if numberS == person and bool:

        print(f"Comienza Persona! Turno [ {increase} ]")

        triquiLogicPerson(triquiMatrix)

        turn(bool=False, increase=increase)

    else:
        print(f"Comienza Computadora! Turno [ {increase} ]")

        triquiLogicPc(triquiMatrix)

        turn(bool=True, increase=increase)
            

        
print("-- Eventos con la Matriz --\n")
while True:

    if creatrix == False:

        print("1). Juego Triqui\n2). Crear Matriz\n3). Consulatar Posición Matricial\n4). Mostrar Matriz\n5). Salir")
        selection = int(input("Elige Opción: "))
        print()

        if selection == 1:
            os.system('cls')
            print("Juego Triqui! - Persona vs Computadora.\n")
            triquiGame(changer)

        elif selection == 2:
            print(" -- Crear Matriz --")
            createMatrix()
            logic()
            creatrix = True

        elif selection == 3:
            positicionMatrix()
            show(initMatrix)
            print()

        elif selection == 4:
            show(initMatrix)
            print()
        
        elif selection == 5:
            break

    else:

        print("1). Juego Triqui\n2). Consulatar Posición Matricial\n3). Mostrar Matriz\n4). Salir")
        selection = int(input("Elige Opción: "))
        print()

        if selection == 1:
            os.system('cls')
            print("Juego Triqui! - Persona vs Computadora.\n")
            triquiGame(changer)

        elif selection == 2:
            positicionMatrix()
            show(initMatrix)
            print()

        elif selection == 3:
            show(initMatrix)
            print()
        
        elif selection == 4:
            break


print("Saliendo...")