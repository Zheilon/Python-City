rangeAge = int(input("Ingrese Rango de edad: "))

if rangeAge < 0:
    print("Pre-Infancia.")

elif rangeAge >= 0 and rangeAge <= 5:
    print("Primera Infancia.")

elif rangeAge >= 6 and rangeAge <= 11:
    print("Infancia.")

elif rangeAge >= 12 and rangeAge <= 18:
    print("Adolecencia.")

elif rangeAge >= 27 and rangeAge <= 59:
    print("Adultez.")

elif rangeAge >= 60:
    print("Adulto Mayor.")
