"""

ASISTENTE POR VOZ

"""

import pyttsx3
import speech_recognition as sr

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
        except sr.UnknownValueError:
            print("el micro no funciona")
            return "Error"
        except sr.RequestError:
            print("Falla la transcripción del texto")
        except:
            print("Error no identificado")
            return "Error"
        
audio_a_texto()
