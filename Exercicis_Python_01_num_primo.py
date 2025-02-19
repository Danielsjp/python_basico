"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 1

Un número primo es aquel que sólo es divisible por sí mismo o uno.

Pediremos al usuario un número entero.
Si escribe algo que no sea un número entero la aplicación debe responder: 
    "Has de introducir un número entero".
Daremos hasta tres oportunidades para que nos facilite un dato correcto.
Pero si pasadas esas tres oportunidades sigue sin escribir un entero 
la aplicación finalizará mostrando este mensaje:
    "No has podido introducir un número entero en tres oportunidades
    Puedes volverlo a intentar de nuevo ejecutando otra vez esta aplicación.
    ".
Si escribe un número entero puede pasar que
-- sea un número primo; en ese caso la respuesta de la aplicación será:
    "El número X es primo".
-- no sea un número primo; en ese caso la respuesta de la aplicación será:
    "El número X no es primo".

. 
"""

#Inicializamos una variable en True que luego utilizaremos
condicion = True
#Empezamos un bucle que se repite 3 veces
for intento in range(3):
    #Englobamos en un try que al pedir la variable sea int, si no falla.
    try:
        #solicitamos al usuario introducir datos
        numero = int(input("introduce ->"))
        #comparamos si el numero es mayor que 1 que entre en el bucle
        if numero > 1:
            #por cada "numi" dentro del rango hasta el numero introducido verificamos que sea primo
            for numi in range (2,numero):
                   if numero%numi==0:
                          condicion = False
        if condicion:
             print("es primo")
        else:
             print("no es primo")     
    except ValueError:
        print("dasds")    
else:
    print("has sobresado el numero de veces")