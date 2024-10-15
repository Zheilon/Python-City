import os
import random as rd
os.system('cls')

creatrix = False
changer = True
attack = True
PC_WIN = "pc"
PERSON_WIN = "person"

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

        try:

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

        except ValueError:
            print(f"\nNose Permiten Valores Vacios o Caracteres Diferentes!\n")
    
    found = False
    show(triquiMatrix)


#*---------------------| PC ATTACK |---------------------*#

def strategy_Pc_Attack_One(matrix):

    global attack

    validateOne = False
    validateTwo = False

    for z in range(len(matrix)):
        for m in range(len(matrix[0])):

            if z == 0 and m == 0 and matrix[z][m] == "o":
                validateOne = True

            elif z == 2 and m == 0 and matrix[z][m] == "o":
                validateTwo = True

    for z in range(len(matrix)):
        for m in range(len(matrix[0])):
            
            if z == 1 and m == 0 and matrix[z][m] == " " and validateOne and validateTwo:
                matrix[z][m] = "x"
                attack = False
                validateOne = False
                validateTwo = False


def strategy_Pc_Attack_Two(matrix):

    global attack

    validateOne = False
    validateTwo = False

    for z in range(len(matrix)):
        for m in range(len(matrix[0])):

            if z == 0 and m == 1 and matrix[z][m] == "o":
                validateOne = True

            elif z == 2 and m == 1 and matrix[z][m] == "o":
                validateTwo = True

    for z in range(len(matrix)):
        for m in range(len(matrix[0])):
            
            if z == 1 and m == 1 and matrix[z][m] == " " and validateOne and validateTwo:
                matrix[z][m] = "x"
                attack = False
                validateOne = False
                validateTwo = False


def strategy_Pc_Attack_Three(matrix):

    global attack

    validateOne = False
    validateTwo = False

    for z in range(len(matrix)):
        for m in range(len(matrix[0])):

            if z == 0 and m == 2 and matrix[z][m] == "o":
                validateOne = True

            elif z == 2 and m == 2 and matrix[z][m] == "o":
                validateTwo = True

    for z in range(len(matrix)):
        for m in range(len(matrix[0])):
            
            if z == 1 and m == 2 and matrix[z][m] == " " and validateOne and validateTwo:
                matrix[z][m] = "x"
                attack = False
                validateOne = False
                validateTwo = False


def strategy_Pc_Attack_Four(matrix):

    global attack

    validateOne = False
    validateTwo = False

    for z in range(len(matrix)):
        for m in range(len(matrix[0])):

            if z == 2 and m == 0 and matrix[z][m] == "o":
                validateOne = True

            elif z == 2 and m == 2 and matrix[z][m] == "o":
                validateTwo = True

    for z in range(len(matrix)):
        for m in range(len(matrix[0])):
            
            if z == 2 and m == 1 and matrix[z][m] == " " and validateOne and validateTwo:
                matrix[z][m] = "x"
                attack = False
                validateOne = False
                validateTwo = False


def strategy_Pc_Attack_Five(matrix):

    global attack

    validateOne = False
    validateTwo = False

    for z in range(len(matrix)):
        for m in range(len(matrix[0])):

            if z == 1 and m == 0 and matrix[z][m] == "o":
                validateOne = True

            elif z == 1 and m == 2 and matrix[z][m] == "o":
                validateTwo = True

    for z in range(len(matrix)):
        for m in range(len(matrix[0])):
            
            if z == 1 and m == 1 and matrix[z][m] == " " and validateOne and validateTwo:
                matrix[z][m] = "x"
                attack = False
                validateOne = False
                validateTwo = False


def strategy_Pc_Attack_Six(matrix):

    global attack

    validateOne = False
    validateTwo = False

    for z in range(len(matrix)):
        for m in range(len(matrix[0])):

            if z == 0 and m == 0 and matrix[z][m] == "o":
                validateOne = True

            elif z == 0 and m == 2 and matrix[z][m] == "o":
                validateTwo = True

    for z in range(len(matrix)):
        for m in range(len(matrix[0])):
            
            if z == 0 and m == 1 and matrix[z][m] == " " and validateOne and validateTwo:
                matrix[z][m] = "x"
                attack = False
                validateOne = False
                validateTwo = False
     

def strategy_Pc_Attack_Seven(matrix):

    global attack

    validateOne = False
    validateTwo = False

    for z in range(len(matrix)):
        for m in range(len(matrix[0])):

            if z == 0 and m == 0 and matrix[z][m] == "o":
                validateOne = True

            elif z == 1 and m == 1 and matrix[z][m] == "o":
                validateTwo = True

    for z in range(len(matrix)):
        for m in range(len(matrix[0])):
            
            if z == 2 and m == 2 and matrix[z][m] == " " and validateOne and validateTwo:
                matrix[z][m] = "x"
                attack = False
                validateOne = False
                validateTwo = False


def strategy_Pc_Attack_Eight(matrix):

    global attack

    validateOne = False
    validateTwo = False

    for z in range(len(matrix)):
        for m in range(len(matrix[0])):

            if z == 0 and m == 2 and matrix[z][m] == "o":
                validateOne = True

            elif z == 1 and m == 1 and matrix[z][m] == "o":
                validateTwo = True

    for z in range(len(matrix)):
        for m in range(len(matrix[0])):
            
            if z == 2 and m == 0 and matrix[z][m] == " " and validateOne and validateTwo:
                matrix[z][m] = "x"
                attack = False
                validateOne = False
                validateTwo = False


def strategy_Pc_Attack_Nine(matrix):

    global attack

    validateOne = False
    validateTwo = False

    for z in range(len(matrix)):
        for m in range(len(matrix[0])):

            if z == 2 and m == 0 and matrix[z][m] == "o":
                validateOne = True

            elif z == 1 and m == 1 and matrix[z][m] == "o":
                validateTwo = True

    for z in range(len(matrix)):
        for m in range(len(matrix[0])):
            
            if z == 0 and m == 2 and matrix[z][m] == " " and validateOne and validateTwo:
                matrix[z][m] = "x"
                attack = False
                validateOne = False
                validateTwo = False


def triquiLogicPc(matrix):

    global attack

    strategy_Pc_Attack_One(matrix)

    strategy_Pc_Attack_Two(matrix)

    strategy_Pc_Attack_Three(matrix)

    strategy_Pc_Attack_Four(matrix)

    strategy_Pc_Attack_Five(matrix)

    strategy_Pc_Attack_Six(matrix)

    strategy_Pc_Attack_Seven(matrix) #! Conflict

    strategy_Pc_Attack_Eight(matrix) #! Conflict

    strategy_Pc_Attack_Nine(matrix) #! Conflict

    b = True
    while b:

        if attack:

            valueRow = rd.randint(1, 3)
            valueColumn = rd.randint(1, 3)

            for musthang in range(len(matrix)):
                for aventador in range(len(matrix[0])):
                    
                    if musthang == valueRow - 1 and aventador == valueColumn - 1 and matrix[musthang][aventador] == " ":
                        matrix[musthang][aventador] = "x"
                        b = False
                        break

                    elif musthang == valueRow - 1 and aventador == valueColumn - 1 and matrix[musthang][aventador] != " ":
                        break

        else:
            attack = True
            break

    show(triquiMatrix)


#*---------------------| PERSON STRATEGIES |---------------------*#

def strategy_One_Person():

    win = 0

    for mazda in range(len(triquiMatrix)):
        for caiman in range(len(triquiMatrix[0])):

            if mazda == 0 and caiman == 0 and triquiMatrix[mazda][caiman] == "o":
                win += 1

            elif mazda == 1 and caiman == 0 and triquiMatrix[mazda][caiman] == "o":
                win += 1

            elif mazda == 2 and caiman == 0 and triquiMatrix[mazda][caiman] == "o":
                win += 1

    return win

def strategy_Two_Person():
    
    win = 0

    for mazda in range(len(triquiMatrix)):
        for caiman in range(len(triquiMatrix[0])):

            if mazda == 0 and caiman == 1 and triquiMatrix[mazda][caiman] == "o":
                win += 1

            elif mazda == 1 and caiman == 1 and triquiMatrix[mazda][caiman] == "o":
                win += 1

            elif mazda == 2 and caiman == 1 and triquiMatrix[mazda][caiman] == "o":
                win += 1

    return win

def strategy_Three_Person():
    
    win = 0

    for mazda in range(len(triquiMatrix)):
        for caiman in range(len(triquiMatrix[0])):

            if mazda == 0 and caiman == 2 and triquiMatrix[mazda][caiman] == "o":
                win += 1

            elif mazda == 1 and caiman == 2 and triquiMatrix[mazda][caiman] == "o":
                win += 1

            elif mazda == 2 and caiman == 2 and triquiMatrix[mazda][caiman] == "o":
                win += 1

    return win

def strategy_Four_Person():
    
    win = 0

    for mazda in range(len(triquiMatrix)):
        for caiman in range(len(triquiMatrix[0])):

            if mazda == 0 and caiman == 0 and triquiMatrix[mazda][caiman] == "o":
                win += 1

            elif mazda == 0 and caiman == 1 and triquiMatrix[mazda][caiman] == "o":
                win += 1

            elif mazda == 0 and caiman == 2 and triquiMatrix[mazda][caiman] == "o":
                win += 1

    return win

def strategy_Five_Person():
    
    win = 0

    for mazda in range(len(triquiMatrix)):
        for caiman in range(len(triquiMatrix[0])):

            if mazda == 1 and caiman == 0 and triquiMatrix[mazda][caiman] == "o":
                win += 1

            elif mazda == 1 and caiman == 1 and triquiMatrix[mazda][caiman] == "o":
                win += 1

            elif mazda == 1 and caiman == 2 and triquiMatrix[mazda][caiman] == "o":
                win += 1

    return win

def strategy_Six_Person():
    
    win = 0

    for mazda in range(len(triquiMatrix)):
        for caiman in range(len(triquiMatrix[0])):

            if mazda == 2 and caiman == 0 and triquiMatrix[mazda][caiman] == "o":
                win += 1

            elif mazda == 2 and caiman == 1 and triquiMatrix[mazda][caiman] == "o":
                win += 1

            elif mazda == 2 and caiman == 2 and triquiMatrix[mazda][caiman] == "o":
                win += 1

    return win

def strategy_Seven_Person():
    
    win = 0

    for mazda in range(len(triquiMatrix)):
        for caiman in range(len(triquiMatrix[0])):

            if mazda == 0 and caiman == 0 and triquiMatrix[mazda][caiman] == "o":
                win += 1

            elif mazda == 1 and caiman == 1 and triquiMatrix[mazda][caiman] == "o":
                win += 1

            elif mazda == 2 and caiman == 2 and triquiMatrix[mazda][caiman] == "o":
                win += 1

    return win

def strategy_Eight_Person():
    
    win = 0

    for mazda in range(len(triquiMatrix)):
        for caiman in range(len(triquiMatrix[0])):

            if mazda == 0 and caiman == 2 and triquiMatrix[mazda][caiman] == "o":
                win += 1

            elif mazda == 1 and caiman == 1 and triquiMatrix[mazda][caiman] == "o":
                win += 1

            elif mazda == 2 and caiman == 0 and triquiMatrix[mazda][caiman] == "o":
                win += 1

    return win


#*---------------------| PC STRATEGIES |---------------------*#

def strategy_One_Pc():

    win = 0

    for mazda in range(len(triquiMatrix)):
        for caiman in range(len(triquiMatrix[0])):

            if mazda == 0 and caiman == 0 and triquiMatrix[mazda][caiman] == "x":
                win += 1

            elif mazda == 1 and caiman == 0 and triquiMatrix[mazda][caiman] == "x":
                win += 1

            elif mazda == 2 and caiman == 0 and triquiMatrix[mazda][caiman] == "x":
                win += 1

    return win

def strategy_Two_Pc():

    win = 0

    for mazda in range(len(triquiMatrix)):
        for caiman in range(len(triquiMatrix[0])):

            if mazda == 0 and caiman == 1 and triquiMatrix[mazda][caiman] == "x":
                win += 1

            elif mazda == 1 and caiman == 1 and triquiMatrix[mazda][caiman] == "x":
                win += 1

            elif mazda == 2 and caiman == 1 and triquiMatrix[mazda][caiman] == "x":
                win += 1

    return win

def strategy_Three_Pc():

    win = 0

    for mazda in range(len(triquiMatrix)):
        for caiman in range(len(triquiMatrix[0])):

            if mazda == 0 and caiman == 2 and triquiMatrix[mazda][caiman] == "x":
                win += 1

            elif mazda == 1 and caiman == 2 and triquiMatrix[mazda][caiman] == "x":
                win += 1

            elif mazda == 2 and caiman == 2 and triquiMatrix[mazda][caiman] == "x":
                win += 1

    return win

def strategy_Four_Pc():
    
    win = 0

    for mazda in range(len(triquiMatrix)):
        for caiman in range(len(triquiMatrix[0])):

            if mazda == 0 and caiman == 0 and triquiMatrix[mazda][caiman] == "x":
                win += 1

            elif mazda == 0 and caiman == 1 and triquiMatrix[mazda][caiman] == "x":
                win += 1

            elif mazda == 0 and caiman == 2 and triquiMatrix[mazda][caiman] == "x":
                win += 1

    return win

def strategy_Five_Pc():
    
    win = 0

    for mazda in range(len(triquiMatrix)):
        for caiman in range(len(triquiMatrix[0])):

            if mazda == 1 and caiman == 0 and triquiMatrix[mazda][caiman] == "x":
                win += 1

            elif mazda == 1 and caiman == 1 and triquiMatrix[mazda][caiman] == "x":
                win += 1

            elif mazda == 1 and caiman == 2 and triquiMatrix[mazda][caiman] == "x":
                win += 1

    return win

def strategy_Six_Pc():
    
    win = 0

    for mazda in range(len(triquiMatrix)):
        for caiman in range(len(triquiMatrix[0])):

            if mazda == 2 and caiman == 0 and triquiMatrix[mazda][caiman] == "x":
                win += 1

            elif mazda == 2 and caiman == 1 and triquiMatrix[mazda][caiman] == "x":
                win += 1

            elif mazda == 2 and caiman == 2 and triquiMatrix[mazda][caiman] == "x":
                win += 1

    return win

def strategy_Seven_Pc():
    
    win = 0

    for mazda in range(len(triquiMatrix)):
        for caiman in range(len(triquiMatrix[0])):

            if mazda == 0 and caiman == 0 and triquiMatrix[mazda][caiman] == "x":
                win += 1

            elif mazda == 1 and caiman == 1 and triquiMatrix[mazda][caiman] == "x":
                win += 1

            elif mazda == 2 and caiman == 2 and triquiMatrix[mazda][caiman] == "x":
                win += 1

    return win

def strategy_Eight_Pc():
    
    win = 0

    for mazda in range(len(triquiMatrix)):
        for caiman in range(len(triquiMatrix[0])):

            if mazda == 0 and caiman == 2 and triquiMatrix[mazda][caiman] == "x":
                win += 1

            elif mazda == 1 and caiman == 1 and triquiMatrix[mazda][caiman] == "x":
                win += 1

            elif mazda == 2 and caiman == 0 and triquiMatrix[mazda][caiman] == "x":
                win += 1

    return win


def confirmCount_Number():

    if strategy_One_Person() == 3:
        return 3
    
    elif strategy_One_Pc() == 3:
        return 3
    
    elif strategy_Two_Person() == 3:
        return 3
    
    elif strategy_Two_Pc() == 3:
        return 3
    
    elif strategy_Three_Person() == 3:
        return 3
    
    elif strategy_Three_Pc() == 3:
        return 3
    
    elif strategy_Four_Person() == 3:
        return 3
    
    elif strategy_Four_Pc() == 3:
        return 3
    
    elif strategy_Five_Person() == 3:
        return 3
    
    elif strategy_Five_Pc() == 3:
        return 3
    
    elif strategy_Six_Person() == 3:
        return 3
    
    elif strategy_Six_Pc() == 3:
        return 3
    
    elif strategy_Seven_Person() == 3:
        return 3
    
    elif strategy_Seven_Pc() == 3:
        return 3
    
    elif strategy_Eight_Person() == 3:
        return 3
    
    elif strategy_Eight_Pc() == 3:
        return 3
    
    else:
        return 0
    
    listStrategies = [strategy_One_Person, strategy_One_Pc, 
                      strategy_Two_Person, strategy_Two_Pc, 
                      strategy_Three_Person, strategy_Three_Pc, 
                      strategy_Four_Person, strategy_Four_Pc, 
                      strategy_Five_Person, strategy_Five_Pc, 
                      strategy_Six_Person, strategy_Six_Pc, 
                      strategy_Seven_Person, strategy_Seven_Pc, 
                      strategy_Eight_Person, strategy_Eight_Pc]
    

def confirmCount_Text():

    if strategy_One_Person() == 3:
        return PERSON_WIN
    
    elif strategy_One_Pc() == 3:
        return PC_WIN
    
    elif strategy_Two_Person() == 3:
        return PERSON_WIN
    
    elif strategy_Two_Pc() == 3:
        return PC_WIN
    
    elif strategy_Three_Person() == 3:
        return PERSON_WIN
    
    elif strategy_Three_Pc() == 3:
        return PC_WIN
    
    elif strategy_Four_Person() == 3:
        return PERSON_WIN
    
    elif strategy_Four_Pc() == 3:
        return PC_WIN
    
    elif strategy_Five_Person() == 3:
        return PERSON_WIN
    
    elif strategy_Five_Pc() == 3:
        return PC_WIN
    
    elif strategy_Six_Person() == 3:
        return PERSON_WIN
    
    elif strategy_Six_Pc() == 3:
        return PC_WIN
    
    elif strategy_Seven_Person() == 3:
        return PERSON_WIN
    
    elif strategy_Seven_Pc() == 3:
        return PC_WIN
    
    elif strategy_Eight_Person() == 3:
        return PERSON_WIN
    
    elif strategy_Eight_Pc() == 3:
        return PC_WIN
    
    

def isNull():

    isfill = 0

    for audi in range(len(triquiMatrix)):
        for mercedez in range(len(triquiMatrix[0])):

            if audi == 0 and mercedez == 0 and (triquiMatrix[audi][mercedez] == "x" or triquiMatrix[audi][mercedez] == "o"):
                isfill += 1

            elif audi == 0 and mercedez == 1 and (triquiMatrix[audi][mercedez] == "x" or triquiMatrix[audi][mercedez] == "o"):
                isfill += 1

            elif audi == 0 and mercedez == 2 and (triquiMatrix[audi][mercedez] == "x" or triquiMatrix[audi][mercedez] == "o"):
                isfill += 1

            elif audi == 1 and mercedez == 0 and (triquiMatrix[audi][mercedez] == "x" or triquiMatrix[audi][mercedez] == "o"):
                isfill += 1

            elif audi == 1 and mercedez == 1 and (triquiMatrix[audi][mercedez] == "x" or triquiMatrix[audi][mercedez] == "o"):
                isfill += 1

            elif audi == 1 and mercedez == 2 and (triquiMatrix[audi][mercedez] == "x" or triquiMatrix[audi][mercedez] == "o"):
                isfill += 1

            elif audi == 2 and mercedez == 0 and (triquiMatrix[audi][mercedez] == "x" or triquiMatrix[audi][mercedez] == "o"):
                isfill += 1

            elif audi == 2 and mercedez == 1 and (triquiMatrix[audi][mercedez] == "x" or triquiMatrix[audi][mercedez] == "o"):
                isfill += 1

            elif audi == 2 and mercedez == 2 and (triquiMatrix[audi][mercedez] == "x" or triquiMatrix[audi][mercedez] == "o"):
                isfill += 1

    if confirmCount_Number() == 0 and isfill == 9:
        return True
    
    else:
        return False



def turn(bool: bool, increase: int):

    while True:

        increase += 1

        win = confirmCount_Number()

        if bool and win != 3:

            print(f"\nTurno [ {increase} ] Persona!")

            triquiLogicPerson(triquiMatrix)

            bool = False

        elif win != 3:

            print(f"\nTurno [ {increase} ] Computadora!")

            triquiLogicPc(triquiMatrix)
            
            bool = True

        if win == 3:
            break       

        if isNull():
            break



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

    if isNull():
        print("\nNadie Gana!")

    else:
        print('\n¡Gana Persona!' if confirmCount_Text() == "person" else '\n¡Gana Pc!')
        triquiMatrix.clear()
            

        
print("-- Eventos con la Matriz --\n")
while True:

    if creatrix == False:

        print("\n1). Juego Triqui\n2). Crear Matriz\n3). Consulatar Posición Matricial\n4). Mostrar Matriz\n5). Salir")
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

        print("\n1). Juego Triqui\n2). Consulatar Posición Matricial\n3). Mostrar Matriz\n4). Salir")
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