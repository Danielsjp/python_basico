"""

Crea un programa que utilice un diccionario para almacenar información de un inventario de productos.

Hay que guardar 5 productos con sus cantidades.

Después añadiremos dos nuevos productos.

Actualizaremos las cantidades de dos productos cualquiera.

Mostrar ahora todos los productos y sus cantidades


"""

prod = ""
num = 0
a = 1
b = 1
# productos = {"Prod": prod, "Cantidad": num}
lista = []

while a < 4:
    print(a)
    prod = input("Introduce nombre producto")
    num = input("Introduce la cantidad")
    a += 1
    productos = {"Prod": prod, "Cantidad": num}
    lista.append(productos)

print (lista)

producto = "yogur"

for a in lista:
    if "Prod" in a:
        a['Cantidad']
