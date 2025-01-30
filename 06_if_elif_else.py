"""
IF / ELIF / ELSE
"""
#condicion binaria o si o no
llueve = False

if llueve:
    print("Cogeré el paraguas")
else:
    print("Iré a Pasear")

print ("hola que tal")

#condicion 

Lunes = False # Los lunes como pizza
Jueves = True # jueves, paella
#el resto de dias bocadillo

# if Lunes:
#     print("toca pizza")
# elif Jueves:
#     print("toca paella")
# else:
#     print("toca bocadillo")

# edad = int(input("cual es tu edad?"))

# ojo con poner todo IF si hay una conducion que se cumple siempre mostrara todos los mensajes, no queremos eso !!!
# el pass es cuando no sabemos que poner para que podamos sigar trabajando

# if (0<= edad <12):
#     print("eres un niño")
# elif (edad<18):
#     print("eres un adolescente")
# elif (edad<=30):
#     print("eres joven")
# elif (edad<35):
#     pass
# else:
#     print("tu puedes con todo")

# if (edad<0) or (edad>120):
#     print("No me lo creo")
# elif (edad<18):
#     años = 18 - edad 
#     print(f"Aun no puedes votar, te faltan {años} años")
# else:
#     años = edad - 18
#     print(f"Ya puedes votar desde hace {años} años")

num1 = int(input("Num 1 ->"))
num2 = int(input("Num 2 ->"))
Ope = input("Que operación quieres hacer? opciones: suma,resta,multi,division,exp,div_ent,modulo ->")

if num1.is_integer and num2.is_integer:
    if Ope == "suma":
        suma = num1 + num2
        print(f"{num1} + {num2}={suma}")
    elif Ope == "resta":
        resta = num1 - num2
        print(f"{num1} - {num2}={resta}")
    elif Ope == "multi":
        multi = num1 * num2
        print(f"{num1} * {num2}={multi}")
    elif Ope == "division":
        division = num1 / num2
        print(f"{num1} / {num2}={division}")
    elif Ope == "exp":
        exp = num1 ** num2
        print(f"{num1} ** {num2}={exp}")
    elif Ope == "div_ent":
        pass
    elif Ope == "modulo":
        modulo = num1 % num2
        print(f"{num1} % {num2}={modulo}")
    else:
        print("Eso no es una operacion valida")
else:
    print("no son numeros")

