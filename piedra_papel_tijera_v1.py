""""
LISTA MEJORAS

Limitar un maximo de partidas
Contar cuantas veces han ganado, perdido y empatado
Preguntar el nombre del usuario

Guardar los resultados del jugador con un ranking, recuento de victorias y derrotas.

"""

# Informar al usuario de las opciones del juego
import random
import os
os.system("cls")

# variables que llevan el conteo de resultados de partidas
ganadas = 0
empatadas = 0
perdidas = 0

# Lista de las opciones
#opciones_juego = ["Piedra", "Papel", "Tijeras"]
opciones_juego = ["💎", "🧻", "✂"]

nombre_usuario = input ("Escribe tu nombre --> ")
print (f"Buena suerte {nombre_usuario}")

while True:
    try:
        numero_partidas = int(input("¿Cuántas partidas quieres jugar(Entre 1 y 5)?\n(entre 1 y 5 , 0 para salir) --> "))
      
        if numero_partidas == 0:
            print(f"Hasta pronto {nombre_usuario}")
            #os.system("exit")
            break
        elif 1 <= numero_partidas <= 5:
            break
        else:
            print("Has de introducir un número entre 1 y 5\n")
    except:
        print("Has de introducir un número entero\n")
        #break

contador_de_partidas = 1

while contador_de_partidas <= numero_partidas:
    contador_de_partidas += 1
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
            print(f"{nombre_usuario}, Habéis empatado")
            empatadas += 1
        elif (opcion_maquina == "1" and opcion_maquina == "3") \
            or (opcion_humano == "2" and opcion_maquina == "1") \
                and (opcion_humano == "3" and opcion_maquina == "1"):
            print("Has ganado!")
            print(resultado_partida)
            ganadas += 1
        else:
            print(f"\t{nombre_usuario} Has perdido!")
            print(resultado_partida)
            perdidas += 1

        resultado_actual = f"""
        Ganadas: {ganadas} | Empates : {empatadas} | Perdidas : {perdidas}

        """
        print(resultado_actual)

print("\nAplicación Finalizada")
# print(f"\nGanadas {ganadas}")
# print(f"\nPerdidas {perdidas}")
# print(f"\nEmpatadas {empatadas}")

