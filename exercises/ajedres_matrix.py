initMatrix = []
listPar = []
listInPar = []

x = int(input("Ingresa Número de [ Filas ]: "))
y = int(input("Ingresa Número de [ Columnas ]: "))

#*--- + --- + --- + ---\ LÓGICA \--- + --- + --- + ---*#
for z in range(x):
    if z % 2 == 0:
        initMatrix.append(listPar)
    elif z % 2 == 1:
        initMatrix.append(listInPar)

for z in range(y):
    if z % 2 == 0:
        listPar.append("N")
        listInPar.append("B")
    elif z % 2 == 1:
        listPar.append("B")
        listInPar.append("N")
    
#*--- + --- + --- + ---\ PRINT \--- + --- + --- + ---*#
print(f"\n[ {x} x {y} ]")
for z in range(len(initMatrix)):
    print()

    for w in range(len(initMatrix[z])):
        if w % 2 == 0:
            print(end=f"| {initMatrix[z][w]} |")

        elif w == len(initMatrix[z]) - 1:
            print(end=f" {initMatrix[z][w]} |")

        elif w % 2 == 1:
            print(end=f" {initMatrix[z][w]} ")

