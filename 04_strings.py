# cadenas de texto
string_1 = 'Hola'
string_2 = "Hola"
string_3 = """hola"""

#nombre = "Daniel"
#apellido = "Sánchez"
#edad = 42

# nombre = input("Cual es tu nombre? ->")
# apellido = input("Cual es tu apellido? ->")
# edad = input("Cual es tu edad? ->" )

# #frase = "Me llamo " + nombre + " " + apellido + " y tengo " + str(edad) + " años"

# frase = "Me llamo " + nombre + " " + apellido + " y tengo " + edad + " años"
# print(frase)

# # esto es mas optimo porque pones menos cosas y es mas claro, siguiendo la filosofia de python.
# print(f"Me llamo {nombre} {apellido} y tengo {edad} años")
# print("Me llamo {} {} y tengo {} años".format(nombre, apellido, edad))

frase2 = "esto es una frase un poco larga"

# Primer caracter del string
print("Imprime primer caracter: ", frase2[0])

# ultimo caracter del string
print("Imprime ultimo caracter: ", frase2[-1])

# imprime los 5 primero
print("Imprime 5 caracteres: ", frase2[0:5])

# imprime los 5 primero
print("Imprime 5 caracteres: ", frase2[-6:])

# imprime de par en par
print("Imprime 5 caracteres: ", frase2[::2])

# imprime invertido
print("Imprime 5 caracteres: ", frase2[::-1])

# imprime largo
print(len(frase2))

# pasa a mayusculas
print(frase2.upper())

# pasa a minusculas
print(frase2.lower())

# pasa a capitize
print(frase2.capitalize())

# cadena = "Hola mundo, esto es un test"
# # Dividir la cadena por el primer espacio y tomar la segunda parte
# palabra_despues_espacio = cadena.split(' ', 1)[1]
# print(palabra_despues_espacio)

#contar caracteres
print("cuenta las as", frase2.count("a"))

#encontrar la posicion de una letra
#devuelve -1 si no existe ese caracter
print("posicion de letra", frase2.find("a"))

# verificar si cumple cierta condicion

print(frase2.startswith("http"))
print(frase2.endswith(".com"))

# verificar si el texto es convertible a numero
# print(int(frase2)) esto no se puede
# pero un string en numero si que se puede
numero = "10" 
print (numero.isnumeric())
#es texto?
print (numero.isalpha())
#es texto con numeros y letras
print (numero.isalnum())

# cambiar caracteres
print(frase2.replace("es", "os"))

numero_de_palabras = len(frase2.split())
print(numero_de_palabras)

#Mini ejercicio

texto = "bUeNoS dIas"

# pasa a minusculas
texto1 = texto.lower()

# pasa a capitize
print(texto1.capitalize())

print("ab" > "ac")

