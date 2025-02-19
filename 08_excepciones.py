"""
EXCEPCIONES
Son errores que se producen durante la ejecución del programa
y lo interrumpen
"""
import os
os.system("cls")



try:
    num = float(input("Escribe un numero ...."))
    # print(1/0)
    # print("Despues de la división por cero")
#catch en otros lenguajes
except ValueError:
    print("has de introducir un numero")
except ZeroDivisionError:
    print("No se puede divir por cero")
except:
    #error generico
    print("ha ocurrido un error al dividir por cero")

print("El programa continua ....")