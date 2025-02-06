# El usuario introduce un número entero, como máximo 100
# ese número es el límite
# Desde 0 hasta el número introducido (los dos incluidos), vamos a listar todos los números
# Pero...
# -- Si el número es multiplo de 3, escribiremos 3 - FIZZ
# -- Si el número es multiplo de 5, escribiremos 5 - BUZZ
# -- Si el número es multiplo de 3 y de 5, escribiremos 3 - FIZZ-BUZZ
# -- En los demás casos sólo el número
# -- Si el usuario escribe más de 100 o menos de 0, diremos "El número es incorrecto"

try:
    entero = int(input("Introduce un numero entero"))
    if entero >= 0 and entero <= 100:
        for i in range(0,entero+1):
            # if i == 0:
            #     print(0)
            if i % 3 == 0 and i % 5 == 0 :
                print(f"{i} FIZZ-BUZ")
            elif i % 5 == 0 :
                print(f"{i} BUZZ")
            elif i % 3 == 0 :
                print(f"{i} FIZZ")
            else:
                print(i)
    else:
        print("el número es incorrecto")
except:
    print("error")