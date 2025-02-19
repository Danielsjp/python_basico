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
        case "+":
            suma = num1 + num2
            print(f"{num1} + {num2} = {round(suma,2)}")
        case "-":
            resta = num1 - num2
            print(f"{num1} - {num2} = {round(resta,2)}")
        case "*":
            multi = num1 * num2
            print(f"{num1} * {num2} = {round(multi,2)}")
        case "/":
            # if float(num2)> 0:
            division = num1 / num2
            print(f"{num1} / {num2} = {round(division,2)}")
            # else:
            #     print("NO se puede dividir por cero")
        case "**":
            exp = num1 ** num2
            print(f"{num1} ** {num2} = {round(exp,2)}")
        case "//":
            if num2> 0:
                division = int(num1) // int(num2)
                print(f"{num1} // {num2} = {division}")
            else:
                print("NO se puede dividir por cero")
        case "%":
            modulo = num1 % num2
            print(f"{num1} % {num2} = {round(modulo,2)}")
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

