"""
OPERADORES LÓGICOS
Sirven para poder combinar diversas condiciones
"""

print("yes")
print(True and True)
print(True and False)
print(False and False)

print("or")
print(True or True)
print(True or False)
print(False or False)

print("not")
print(not True)
print(not False)

mayoria_edad = 18
edad = input("Introduce la edad :")
if not edad.isdigit():
    print("Debes introducir un número entero")
elif 0 > int(edad) > 120:
    print("No me lo creo")
else:
    edad = int(edad)
    if edad < mayoria_edad:
        print(f"Aun no puedes votar, te faltan {mayoria_edad - edad} años")