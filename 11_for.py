# """
# for
# """

# nombres = ["Pol", "Pau", "Luis", "Juan", "Pablo", "paco"]
# numeros = [25, 30, 35, 40, 45, 28, 24, 76, 89, 234]

# # for nombre in nombres:
# #     print(nombre)

# # mostrar los que empiezan por P
# check = 'P'

# # nombres2 = [nombres.lower() for item in nombres]
# # for nombre in nombres:
# #     if nombre.lower().startswith(check.lower()):
# #         print(nombre.capitalize())

# # for nombre2 in nombres:
# #     if nombre2[0] == "P" or nombre2[0] == "p":
# #         print(nombres[0])
# #         print(nombre2)



# # for nombre in nombres:
# #     print(nombre)

# # mostrar los que empiezan por P
# check = 'P'

# # nombres2 = [nombres.lower() for item in nombres]
# # for nombre in nombres:
# #     if nombre.lower().startswith(check.lower()):
# #         print(nombre.capitalize())

# # for nombre2 in nombres:
# #     if nombre2[0] == "P" or nombre2[0] == "p":
# #         print(nombres[0])
# #         print(nombre2)

# suma = 0
# for numero in numeros:
#     #if str(numero).startswith("2"):
#         # print(numero, end=" ")
#     suma += numero
#     media = suma / len(numeros)
# print(suma)
# print (media)

# suma2 = 0
# puntero = 0
# for numero in numeros:
#     if str(numero).startswith("2"):
#         # print(numero, end=" ")
#         puntero += 1
#         suma2 += numero
#         media2 = suma2 / puntero

# print(suma2)
# print (media2)
# print(puntero)

nombres = ["Pol", "Pau", "Luis", "Juan", "Pablo", "paco"]
# check = "Luis"

# for nombre in nombres:
#     if nombre.lower() == check.lower():
#         print(nombre)
#         break
# else:
#     print("No encontrado")
#print(nombres.index(check))

nombres_con_o = []
for nombre in nombres:
    indice = nombres.index(nombre)
    if "o" in nombre.lower():
        print(f"{nombre} esta en la posicion {indice+1}")
        nombres_con_o.append(nombre)

print(nombres_con_o)

print(list(range(10)))

for num in range(10):
    print(num+1)
# for num in ran

for index in range(len(nombres)):
    print(f"{index} {nombres[index]}")

