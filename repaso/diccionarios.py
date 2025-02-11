"""
DICCIONARIOS
El acceeso al dato se produce mediante un identificador
llamado "clave". Así: "clave" : "valor"
La clave puede ser un string, un número,  una tupla, ....
{} < -- llaves
"""

dic_1 = {} #diccionario vacio
lista_1 = [] #lista vacia
# tupla_vacia = (,) ... no se puede hacer...

#las listas llevan un booleana implicito
if not lista_1:
    print("La lista está vacia")

dic_1 = {"nombre": "maria", "apellido": "Sánchez","Edad":23} #diccionario vacio

print(dic_1["nombre"])

clave = "dirección"

print(dic_1.get(clave, f"la clave {clave} no existe en el diccionario")) # mensaje personalizado del none

for propiedad in dic_1.keys():
    print(propiedad)


for propiedad in dic_1.values():
    print(propiedad)

for clave, valor in dic_1.items():
    print(f"{clave} : {valor}")

#Añadir un par clave-valor

dic_1["pais"] = "Grecia"

print(dic_1)

dic_actualizacion = {"ciudad" : "Paris", "edad": 50}

dic_1.update(dic_actualizacion) #añade y actualiza

print(dic_1)
