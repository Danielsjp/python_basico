"""
RESUMEN SIMPLIFICADO DE LO ESENCIAL

"""

# variables
# es un contenedor de un elemento
# es un identificador para ubicar un elemento guardado en memoria

# las variables siempre se declaran antes de ser utilizadas
# también deben ser iniciadas ( no confundir con declarar... ) 

int = 1
float = 1.0
string = "hola"
boolean = True #False

#aunque sean vacios hay que indicar valores

string = ""
int = 0
lista = []

# operadores
# --- de tipo matemático :

1 + 1
1 - 1
1 / 1
1 * 1

# --- de comparación :
# siempre devuelven un valor booleano
# tb podemos comparar string

1 == 1
1 != 1
1 > 1
1 < 1
print ("Hola">"hola")

int = 5
# int = int  + 5
int += 5 # esto es mas optimo

suma_strings = "hola" + "adios"
multi_string = "hola"*3

# casteo de datos

int(5)
str(6)

# estructuras de control
# condiciones
# if
# if / else / 
# if / elif

# añadir un elemento al final
lista.append(6)
# quitar un elemento final
lista.pop(6)
# quitar pol... ejecutar tantas veces como exista pol
lista.remove("Pol")
# 
lista.insert(1, "hola")
#eliminar por posicion concreta
del lista[4]

lista_1 = [0, 1, 2]
lista_2 = [2, 3, 4]

lista_1.extend(lista_2)
lista_1 = lista_1 + lista_2
lista_1 += lista_2

a = 22

a  = 