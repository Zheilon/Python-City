#suma, resta, multi, divi, cualquiera   
import os
import math
os.system('cls')
print("!-------* Calculadora *-------!")
print()

while True:
    print("Suma -----------------> ( 1 )")
    print("Resta ----------------> ( 2 )")
    print("Multiplicación -------> ( 3 )")
    print("División -------------> ( 4 )")
    print("Raiz Cuadrada --------> ( 5 )")
    opcion = int(input("Digite la opción: "))
    print()

    try:
        if opcion == 1:
            print("------------*-< Suma >-*------------")
            one = float(input("Ingrese Primer Dígito: "))
            two = float(input("Ingrese Segundo Dígito: "))
            print(f"Suma [ {one} + {two} ] = {one + two}")

        elif opcion == 2:
            print("------------*-< Resta >-*------------")
            one = float(input("Ingrese Primer Dígito: "))
            two = float(input("Ingrese Segundo Dígito: "))
            print(f"Resta [ {one} - {two} ] = {one - two}")

        elif opcion == 3:
            print("------------*-< Multiplicación >-*------------")
            one = float(input("Ingrese Primer Dígito: "))
            two = float(input("Ingrese Segundo Dígito: "))
            print(f"Multiplicación [ {one} * {two} ] = {one * two}")

        elif opcion == 4:
            print("------------*-< División >-*------------")
            one = float(input("Ingrese Primer Dígito: "))
            two = float(input("Ingrese Segundo Dígito: "))
            print(f"División [ {one} / {two} ] = {one  / two}")
            print()

        elif opcion == 5:
            print("------------*-< Raiz Cuadrada >-*------------")
            squrtT = int(input("Ingresa Digito a Operar con Raíz: "))

            if squrtT > 0:
                print(f"Raiz Cuadrada [ {squrtT} ] = {math.sqrt(squrtT)}")
              
            try: 
                math.sqrt(squrtT)
            except Exception as ex:
                print(f"{ex}: El radicando no puede ser Negativo!")

    except Exception as z:
        print(f"{z}")
        
    print()

    confirm = str(input("Continue? S / N: " ))

    if confirm.upper() == 'N':
        break

    os.system('cls')

print()
print("Afuera\n")