"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 4
Mostraremos el mensaje: "Conversor de segundos"
A continuación pediremos al usuario una cantidad de segundos.

Le responderemos:
- Si son menos de 60 segundos, mostrará "X segundos son menos de 1 minuto"
- Si es igual o superior a 60 segundos le diremos:
    "X segundos son Y minutos y Z segundos"

Y así para las siguientes unidades de tiempo. Por tanto, si la cantidad de segundos 
supera la hora, le diremos cuantas horas, minutos y segundos son. 
Lo mismo si supera un día o una semana. 

. 
"""

print("Conversor de segundos")
seconds = int(input("Introduzca una cantidad de segundos"))
seconds = seconds % (24 * 3600)
hour = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60


if segundos < 60:
    print(f"{segundos} son menos de 1 minuto")

elif segundos >= 60:
    minutos = segundos / 60
    minutos2 = round(minutos, 0)
    segundos2 = round(minutos - minutos2,2)
    print(f"{segundos} son {minutos2} minutos y {segundos2*10} segundos")

elif segundos > 3600:
    horas = segundos / 3600
    horas2 = round(horas, 0)
    minutos2 = round(horas - horas2,2)
    print(f"{segundos} son {horas2} horas y {minutos2*10} minutos")