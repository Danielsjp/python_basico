respuesta = input("Indique los números y la operación a realizar.\nEjemplo : 10, 5, +\n").split(", ")
try:
    num1 = float(respuesta[0])
    num2 = float(respuesta[1])
    Ope  = respuesta[2]
    # print(num1.isdigit())
    # print(num1.isdecimal())
    # print(num1.isnumeric())
    # print(num1.isalpha())
    # if not num1.isdigit(): (negamos)10
    match Ope:
        case "+" |"-"|"*"|"/"|"//"|"%"|"**":
            operacion = eval(f"{num1}{Ope}{num2}")
            print(f"{num1} {Ope} {num2} = {operacion}")
        case _:
            print("Eso no es una operacion valida")
except ZeroDivisionError:
    print("error de division")
except:
    print("Algo ha fallado")
else:
    print("se levanta si no se ejecuta la excepción")
finally:
    print("Se ejecuta siempre")

