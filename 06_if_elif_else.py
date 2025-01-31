"""
IF / ELIF / ELSE
"""
#condicion binaria o si o no
llueve = False

if llueve:
    print("Cogeré el paraguas")
else:
    print("Iré a Pasear")

print ("hola que tal")

#condicion 

Lunes = False # Los lunes como pizza
Jueves = True # jueves, paella
#el resto de dias bocadillo

# if Lunes:
#     print("toca pizza")
# elif Jueves:
#     print("toca paella")
# else:
#     print("toca bocadillo")

# edad = int(input("cual es tu edad?"))

# ojo con poner todo IF si hay una conducion que se cumple siempre mostrara todos los mensajes, no queremos eso !!!
# el pass es cuando no sabemos que poner para que podamos sigar trabajando

# if (0<= edad <12):
#     print("eres un niño")
# elif (edad<18):
#     print("eres un adolescente")
# elif (edad<=30):
#     print("eres joven")
# elif (edad<35):
#     pass
# else:
#     print("tu puedes con todo")

# if (edad<0) or (edad>120):
#     print("No me lo creo")
# elif (edad<18):
#     años = 18 - edad 
#     print(f"Aun no puedes votar, te faltan {años} años")
# else:
#     años = edad - 18
#     print(f"Ya puedes votar desde hace {años} años")
import os

def clear_console():
    # Check the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/MacOS
        os.system('clear')

# Example usage:
clear_console()

print("###############################")
print("#WELCOME TO THE CALCULATOR 1.0#")
print("###############################")
print("")

num1 = input("Insert Num 1 ->")
num2 = input("Insert Num 2 ->")
Ope  = input("¿Que operación quieres hacer? opciones: suma,resta,multi,division,exp,div_ent,modulo ->")

# print(num1.isdigit())
# print(num1.isdecimal())
# print(num1.isnumeric())
# print(num1.isalpha())
# if not num1.isdigit(): (negamos)

if num1.isnumeric() and num2.isnumeric():
    if  Ope == "suma":
        suma = float(num1) + float(num2)
        print(f"{num1} + {num2} = {round(suma, 2)}")
    elif Ope == "resta":
        resta = float(num1) - float(num2)
        print(f"{num1} - {num2} = {round(resta,2)}")
    elif Ope == "multi":
        multi = float(num1) * float(num2)
        print(f"{num1} * {num2} = {round(multi,2)}")
    elif Ope == "division":
        if float(num2)> 0:
            division = float(num1) / float(num2)
            print(f"{num1} / {num2} = {round(division,2)}")
        else:
            print("NO se puede dividir por cero")
    elif Ope == "exp":
        exp = float(num1) ** float(num2)
        print(f"{num1} ** {num2} = {round(exp,2)}")
    elif Ope == "div_ent":
        if float(num2)> 0:
            division = int(num1) // int(num2)
            print(f"{num1} // {num2} = {division}")
        else:
            print("NO se puede dividir por cero")
    elif Ope == "modulo":
        modulo = float(num1) % float(num2)
        print(f"{num1} % {num2} = {round(modulo,2)}")
    else:
        print("Eso no es una operacion valida")
else:
    print("no son numeros!")

