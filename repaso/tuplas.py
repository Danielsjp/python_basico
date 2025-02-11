"""
REPASO LISTAS
Es una coleccion INMUTABLE  de datos
"""

mi_tupla = (3,)
print(type(mi_tupla))

tupla = ("Anna", "Pou", 20)

print(tupla)
print(tupla[0])
#tupla[0] = "Marta" # esto falla porque no se puede reasignar
# para modificar el contenido... pamos la tupla a lista...
lista_temporal = list(tupla)
print(lista_temporal)
lista_temporal[0] = "Marta"
tupla = tuple(lista_temporal)
print(tupla)
print(tupla[1:3])

for item in tupla:
    print(item)