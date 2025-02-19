#tabla de multiplicar
try:
    numero_A = int(input("Introduce un número del 1 al 10 ->"))
    for numero_B in range(1,10+1):
        multi=numero_A*numero_B
        print(f"{numero_A}*{numero_B}={multi}")
except:
    print("error")