# Informar al usuario de las opciones del juego
import random

menu = """

PIEDRA - PAPEL - TIJERA
=======================

1. Piedra
2. Papel
3. Tijera

Any Key. Salir



"""

print(menu)

opcion_humano = input("Elige tu opción --> ").strip()

if opcion_humano not in ["1","2","3"]:
    
    print("juego finalizado, !Hasta pronto!")

else:
    print("Quieres jugar")    

    opcion_maquina = str(random.randint(1,3))

    if opcion_humano == opcion_maquina:
        print("Empate")
    elif (opcion_maquina == "1" and opcion_maquina == "3") \
        or (opcion_humano == "2" and opcion_maquina == "1") \
            and (opcion_humano == "3" and opcion_maquina == "1"):
        print("Has ganado!")
    else:
        print("Has perdido!")