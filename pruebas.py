# respuesta = input("Indique los números y la operación a realizar.\nEjemplo : 10, 5, +\n").split(", ")
# try:
#     num1 = float(respuesta[0])
#     num2 = float(respuesta[1])
#     Ope  = respuesta[2]
#     # print(num1.isdigit())
#     # print(num1.isdecimal())
#     # print(num1.isnumeric())
#     # print(num1.isalpha())
#     # if not num1.isdigit(): (negamos)10
#     match Ope:
#         case "+" |"-"|"*"|"/"|"//"|"%"|"**":
#             operacion = eval(f"{num1}{Ope}{num2}")
#             print(f"{num1} {Ope} {num2} = {operacion}")
#         case _:
#             print("Eso no es una operacion valida")
# except ZeroDivisionError:
#     print("error de division")
# except:
#     print("Algo ha fallado")
# else:
#     print("se levanta si no se ejecuta la excepción")
# finally:
#     print("Se ejecuta siempre")


# nombre = "daniel"

# for letra in nombre:
#     letra += letra

# diccionario = {
# "nombre": "Daniel",
# "Edad": 20
# }

# for key in diccionario:
# print(key)

# for value in diccionario.values():
# print(value)

# for x,y in diccionario.items():
# print(x)
# print(y)

# Diccionario vacío
# person_data = {"name": "", "age": ""}

# # Bucle para pedir los datos
# for key in person_data:
#     # Solicitar nombre o edad según la clave
#     person_data[key] = input(f"Introduce {key}: ")

# # Mostrar el diccionario con los datos ingresados
# print(person_data)


lista = []



while True:
   
    name = input("Dime el name")
    year = input("Dime el year")
    diccionario = {"Nombre":name, "Edad":year}
    lista.append(diccionario)
    print(lista)