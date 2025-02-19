# """"
# REPASO LISTAS
# """
# # lista vacía
# lista = []

# lista.append("Anna")

# print(lista) #devuelve: ["Anna"]

# # Las listas son colecciones de datos indexados
# # el índice empieza en 0

# lista[0]

# #hacemos un casting de range a list 

# lista_enteros = list(range(1,21,2))
# print(lista_enteros)

# lista_nombres = ["Pol", "Noa", "Sara", "Pepe"]

# for nombre in lista_nombres:
#     indice = lista_nombres.index(nombre)
#     print(f"{indice}. {nombre}")


# for indice, valor in enumerate(lista_nombres):
#     print(f"{indice}. {valor}")

# # Copia de una lista

# nueva_lista_1 = lista_nombres.copy()
# nueva_lista_2 = lista_nombres[:]

# #Mini ejercicio: Obtener los numeros elevados al cuadrado 

lista_numeros = list(range(0, 11))

# lista2 = []

# for numero in lista_numeros:
#    lista2.append(numero*numero)   
# print(lista2)

# # forma 2 --> List comprehensions
lista_temporal = []
lista_cuadrados = [ x**2 for x in lista_numeros ]

for lista in lista_cuadrados:
    lista_temporal.append(lista)

print(lista_temporal)

# lista_ciudades = ['NY', 'LA', 'BCN']
# ny, la, bcn = lista_ciudades
# print(bcn)


