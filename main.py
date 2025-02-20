"""

ASISTENTE POR VOZ

"""

import pyttsx3
import speech_recognition as sr
import datetime

def audio_a_texto():
    #Objeto para reconocer el audio:
    r = sr.Recognizer()
    # configurar el microfono
    with sr.Microphone() as source:
        
        # tiempo de espera hasta que activa el micro
        r.pause_threshold - 0.8
        # Mensaje para el usuario para que sepa que ya puede hablar
        print("Ya puedes hablar")
        # variable para guardar el audio
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language="es")

            # mostrar en pantalla el texto
            print("Voz reconocida:", text)
            return text
        except sr.UnknownValueError:
            print("el micro no funciona")
            return "Error"
        except sr.RequestError:
            print("Falla la transcripción del texto")
        except:
            print("Error no identificado")
            return "Error"
        
#audio_a_texto()

def respuesta_maquina(text):

    # Iniciar el motor de pyttsx3

    engine = pyttsx3.init()

    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(text)

    volumen = engine.getProperty("volume")
    engine.setProperty("volume", 1)




    engine.runAndWait()

engine = pyttsx3.init()

# voices = engine.getProperty('voices')

# Buscar la voz Zira (puede variar según el sistema)
# for voice in voices:
#     if "Pablo" in voice.name:
#         engine.setProperty('voice', voice.id)
#         print(f"Voz establecida: {voice.name}")
#         break


# respuesta_maquina("hola como estas")   


# engine = pyttsx3.init()



# # Obtener las voces disponibles
# voices = engine.getProperty('voices')

# # Imprimir la lista de voces
# for voice in voices:
#     print(f"ID: {voice.id}")
#     print(f"Nombre: {voice.name}")
#     print(f"Idioma: {voice.languages}")
#     print("-" * 40)


def decir_dia_semana():
    dia_actual = datetime.date.today()
    print()

    dia_semana = dia_actual.weekday()

    dias_esp = ("lunes", "martes", "miércoles", "jueves", "viernes", "sabado", "domingo")

    respuesta_maquina(f"Hoy es {dias_esp[dia_semana]}")

#decir_dia_semana()


def decir_la_hora():

    hora_actual = datetime.datetime.now()
    hora = f"En este momento son las {hora_actual.hour} horas, {hora_actual.minute} minutos y {hora_actual.second} segundos"
    respuesta_maquina(hora)

#decir_la_hora()


def saludo_inicial():

    hora_actual = datetime.datetime.now().hour
    print(hora_actual)

    # momento del dia

    if 6 < hora_actual < 14:
        momento = "Buenos días"
    elif 14 <= hora_actual < 20:
        momento = "Buenas tardes"
    else:
        momento = "Buenas noches"

    saludo = f"{momento}, soy Axela, tu asistente personal"
    respuesta_maquina(saludo)
    respuesta_maquina("¿En qué te puedo ayudar?")

#saludo_inicial()

# Funcion que lanza las demás

def funcion_principal():

    # Que empiece saludando
    saludo_inicial()

    #bucle infinito para que escuche
    #lo que le vamos a pedir

    activo = True
    while activo:

        peticion = audio_a_texto().lower()
        print(peticion)

        if peticion == "silencio":
            activo = False

funcion_principal()