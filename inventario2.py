"""

Crea un programa que utilice un diccionario para almacenar información de un inventario de productos.

Hay que guardar 5 productos con sus cantidades.

Después añadiremos dos nuevos productos.

Actualizaremos las cantidades de dos productos cualquiera.

Mostrar ahora todos los productos y sus cantidades

"""

inventario = {"manzanas":10, "peras":15, "kiwi": 9, "limones": 4, "naranjas": 7}

#añadir 2 productos

inventario["piñas"] = 3
inventario["tomates"] = 5

print(inventario)

# Modificar la cantidad con una nueva

inventario["naranjas"] = 4

#incrementar la cantidad

inventario["kiwi"] += 5

print(inventario)

# pop clvae quita del diccionaro la clave indicada

fruta = inventario.pop("peras")

print(fruta)
print(inventario)

for producto in sorted(inventario):
    print(f"producto {producto}")

# for producto in sorted(inventario, reverse = True):
#     print(f"producto {producto}")