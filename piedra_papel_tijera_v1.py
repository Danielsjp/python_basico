""""
LISTA MEJORAS

Limitar un maximo de partidas
Contar cuantas veces han ganado, perdido y empatado
Preguntar el nombre del usuario

Guardar los resultados del jugador con un ranking

"""

# Informar al usuario de las opciones del juego
import random
# Lista de las opciones
opciones_juego = ["Piedra", "Papel", "Tijeras"]
opciones_juego = ["💎", "🧻", "✂"]

menu = f"""

PIEDRA - PAPEL - TIJERA
=======================

1. {opciones_juego[0]}
2. {opciones_juego[1]}
3. {opciones_juego[2]}

Any Key. Salir


"""

print(menu)

opcion_humano = input("Elige tu opción --> ").strip()

if opcion_humano not in ["1","2","3"]:
    
    print("juego finalizado, !Hasta pronto!")

else:
    print("Quieres jugar")    

    opcion_maquina = str(random.randint(1,3))
    
    resultado_partida = f"""
        Has elegido {opciones_juego[int(opcion_humano)-1]}
        La máquina ha elegido {opciones_juego[int(opcion_maquina)-1]}
    """

    if opcion_humano == opcion_maquina:
        print("Empate")
    elif (opcion_maquina == "1" and opcion_maquina == "3") \
        or (opcion_humano == "2" and opcion_maquina == "1") \
            and (opcion_humano == "3" and opcion_maquina == "1"):
        print("Has ganado!")
        print(resultado_partida)
    else:
        print("Has perdido!")
        print(resultado_partida)