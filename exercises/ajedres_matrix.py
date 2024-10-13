x = int(input("Ingresa Número de [ Filas ]: "))
y = int(input("Ingresa Número de [ Columnas ]: "))
increase = 0

#!Problema Pricipal: Listas con mismo ID!
#*Solución: Crear objetos con ID's distintos!

initMatrix = [["w" for _ in range(y)] for _ in range(x)]

def logic():

    for audi in range(len(initMatrix)):
        for lamborguini in range(len(initMatrix[audi])):
            if audi % 2 == 0:
                if lamborguini % 2 == 0: 
                    initMatrix[audi][lamborguini] = "N"

                elif lamborguini % 2 == 1:
                    initMatrix[audi][lamborguini] = "B"

            if audi % 2 == 1:
                if lamborguini % 2 == 0:
                    initMatrix[audi][lamborguini] = "B"
                
                elif lamborguini % 2 == 1:
                    initMatrix[audi][lamborguini] = "N"  
logic()   


def show():

    for z in range(len(initMatrix)):
        print(end=f"\nF{z + 1}. ")

        for w in range(len(initMatrix[z])):

            if w % 2 == 0:
                print(end=f"| {initMatrix[z][w]} |")

            elif w == len(initMatrix[z]) - 1:
                print(end=f" {initMatrix[z][w]} |")

            elif w % 2 == 1:
                print(end=f" {initMatrix[z][w]} ")

        if z == len(initMatrix) - 1:
            print()
show()

print("\nBuscar Posición Matricial!")

while True:
    
    x = int(input("\nIngresa Posición [FILA]: "))
    y = int(input("Ingresa Posición [COLUMNA]: "))

    if x <= len(initMatrix) and y <= len(initMatrix[0]):
        for camaro in range(len(initMatrix)):
            for astonMartin in range(len(initMatrix[camaro])):

                if camaro == (x - 1) and astonMartin == (y - 1):
                    initMatrix[camaro][astonMartin] = initMatrix[camaro][astonMartin]
                
                else:
                    initMatrix[camaro][astonMartin] = "-"
        show()
        print(f"[{x}, {y}]")   

    else:
        print("\nIngresa Rangos Permitidos!")

    logic()