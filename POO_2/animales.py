class Animal():
    pass


# Esta clase va a tener otras sub clases

class Perro(Animal):
    def sonido(self):
        print("Guau")

class Gato(Animal):
    def sonido(self):
        print("Miau")

Buba = Perro()

Buba.sonido()

Sardina = Gato()

Sardina.sonido()

# para ver de que clase parte otra clase
print(Perro.__bases__)

#para ver que subclases tiene una clase
print(Animal.__subclasses__())