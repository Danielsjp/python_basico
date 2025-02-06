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

tiempo = int(input("Introduzca una cantidad de segundos"))

minutos = tiempo / 60
horas = int(tiempo / 60 / 60)
horas_minutos = tiempo / 60 / 60

# print(minutos)
# print(horas)
# print(horas_minutos)


if tiempo >= 60:
    segundos2 = minutos - round(minutos)
    print(f"{tiempo}segundos son {round(minutos)} minutos y {round(segundos2*100)} segundos")

elif tiempo < 60:
    print(f"{tiempo} segundos son menos de 1 minuto")



# elif segundos >= 60:
#     minutos = segundos / 60
#     minutos2 = round(minutos, 0)
#     
#     print(f"{segundos} son {minutos2} minutos y {segundos2*10} segundos")

# elif segundos > 3600:
#     horas = segundos / 3600
#     horas2 = round(horas, 0)
#     minutos2 = round(horas - horas2,2)
#     print(f"{segundos} son {horas2} horas y {minutos2*10} minutos")