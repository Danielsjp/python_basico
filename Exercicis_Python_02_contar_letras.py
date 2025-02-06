"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 2a

Mostraremos el texto: "Contar letras en un texto"

Pediremos al usuario un texto, así:
"Por favor, introduzca un texto "
Puede contener números y caracteres con tilde.

A continuación mostraremos las letras que contiene y cuantas son,
ordenadas por número de apariciones. En caso de empate, en orden alfabético. 
Ignoraremos los números, los espacios y los signos de puntuación 
(punto, coma, punto y coma, exclamación, etc.)
Consideremos mayúsculas y minúsculas como la misma letra.

Por ejemplo:
"Por favor, introduzca un texto " ¿Amar?
La respuesta sería: 
"El texto contiene las letras:
a, 2 veces
m, 1 vez
r, 1 vez
"

Por ejemplo:
"Por favor, introduzca un texto " Python forever and ever
La respuesta sería: 
"El texto contiene las letras:
e, 4 veces
r, 3 veces
o, 2 veces
n, 2 veces
a, 1 vez
f, 1 vez
h, 1 vez
p, 1 vez
v, 1 vez
y, 1 vez
"

Ejercicio 2b

Mostraremos el texto: "Contar palabras en un texto"
Lo mismo que el ejercicio anterior, pero con palabras en lugar de letras.
. 
"""




# print("Contar letras en un texto")
# letras = input("Por favor, introduzca un texto ")
# letras = letras.split(" ")
# newlist = "".join(letras)
# duplicadas = []
# repes = []
# junto = []
# for letra in newlist:
#     #repes = newlist.count(letra)
#     if letra not in duplicadas:
#         duplicadas.append(letra)
#         repes.append(newlist.count(letra))
# duplicadas.sort()
# print(duplicadas)
# print(repes)

# for valor1, valor2 in zip(duplicadas, repes):
#     print(f"{valor1}, {valor2}")

# duplicadas = []
# repeticiones = []
# print("Contar letras en un texto")
# letras = input("Por favor, introduzca un texto ")
# letras = letras.split(" ")
# for palabra in letras:
#     if palabra not in duplicadas:
#         repeticiones.append(duplicadas.count(palabra))
#         duplicadas.append(palabra)
        
# duplicadas.sort()

# for valor1, valor2 in zip(duplicadas, repeticiones):
#     print(f"{valor1}, {valor2}")

