
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

while b < 3:
    print(b)
    prod = input("Introduce nombre producto")
    num = input("Introduce la cantidad")
    for x in productos.keys():
        #print(x)
        # for x, y in a.items():
        #  if x == prod:
        #     productos.update() = {"Prod":x, "Cantidad": num}

    # dic_1["pais"] = "Grecia"
        b += 1
    # dic_actualizacion = {"ciudad" : "Paris", "edad": 50}

    # dic_1.update(dic_actualizacion) #añade y actualiza
    
   

#print(lista)    





    

        
       


#print(lista)