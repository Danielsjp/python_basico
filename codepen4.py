# Tenemos esta lista de animales:
animales = ["gato", "perro", "caballo", "paloma", "murcielago", "leon", "mono"]
indicador = False
# Pedir una letra e indicar que animales tienen esa letra
try:
    letra = input("Introduce una letra -> ")
    for i in animales:
        for a in i:
            if a == letra:
                print(i)
                indicador = True
    if not indicador:
        print("Ningún animal contiene esa letra")   
except:
    print("error")