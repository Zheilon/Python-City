#suma, resta, multi, divi, cualquiera
import os
import math
os.system('cls')
print("!-------* Calculadora *-------!")

while True:
    print("Suma -----------------> ( 1 )")
    print("Resta ----------------> ( 2 )")
    print("Multiplicación -------> ( 3 )")
    print("División -------------> ( 4 )")
    print("Raiz Cuadrada --------> ( 5 )")
    opcion = int(input("Digite la opción: "))
    print()

    one = float(input("Ingrese Primer Dígito: "))
    two = float(input("Ingrese Segundo Dígito: "))
    print()

    if opcion == 1:
        print(f"Suma [ {one} + {two} ] = {one + two}")

    elif opcion == 2:
        print(f"Resta [ {one} - {two} ] = {one - two}")

    elif opcion == 3:
        print(f"Multiplicación [ {one} * {two} ] = {one * two}")

    elif opcion == 4 and one != 0:
        print(f"División [ {one} / {two} ] = {one  / two}")

    elif opcion == 5:
        squrtT = int(input("Ingresa Digito a Operar con Raíz: "))
        print(f"Raiz Cuadrada [ {squrtT} ] = {math.sqrt(squrtT)}")

    else:
        print("No se puede Dividir por Cero")

    confirm = str(input("Continue? S / N: " ))

    if confirm.upper() == 'N':
        break

print()
print("Afuera\n")

    


