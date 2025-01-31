"""
MATCH = switch de JS o JAVA
"""
# mes = "Febrero"
# match mes:
#     case "Enero": 
#         print("Iré a NY")
#     case "Febrero":
#         print("Iré a BCN")
#     case "Marzo" | "Abril" | "Mayo":
#         print("Iré a Londres")
#     case _:
#         print("No sé a donde iré")

try:
    num1 = input("Insert Num 1 ->")
    num2 = input("Insert Num 2 ->")
    Ope  = input("""
                 ¿Que operación quieres hacer? opciones: suma,
                 resta,
                 multi,
                 division,
                 exp,
                 div_ent,
                 modulo ->
                 """)
    # print(num1.isdigit())
    # print(num1.isdecimal())
    # print(num1.isnumeric())
    # print(num1.isalpha())
    # if not num1.isdigit(): (negamos)
    if num1.isnumeric() and num2.isnumeric():
        match Ope:
            case "suma":
                suma = float(num1) + float(num2)
                print(f"{num1} + {num2} = {round(suma, 2)}")
            case "resta":
                resta = float(num1) - float(num2)
                print(f"{num1} - {num2} = {round(resta,2)}")
            case "multi":
                multi = float(num1) * float(num2)
                print(f"{num1} * {num2} = {round(multi,2)}")
            case "division":
                # if float(num2)> 0:
                division = float(num1) / float(num2)
                print(f"{num1} / {num2} = {round(division,2)}")
                # else:
                #     print("NO se puede dividir por cero")
            case "exp":
                exp = float(num1) ** float(num2)
                print(f"{num1} ** {num2} = {round(exp,2)}")
            case "div_ent":
                if float(num2)> 0:
                    division = int(num1) // int(num2)
                    print(f"{num1} // {num2} = {division}")
                else:
                    print("NO se puede dividir por cero")
            case "modulo":
                modulo = float(num1) % float(num2)
                print(f"{num1} % {num2} = {round(modulo,2)}")
            case _:
                print("Eso no es una operacion valida")
    else:
        print("No son numeros")
except ZeroDivisionError:
    print("error de division")
except:
    print("Algo ha fallado")
else:
    print("se levanta si no se ejecuta la excepción")
finally:
    print("Se ejecuta siempre")

