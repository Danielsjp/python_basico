class Animal():
    def __init__(self, especie):
        self.especie = especie
    def __str__(self):
        #return self.especie
        return f"la especie es {self.especie}"

# Esta clase va a tener otras sub clases

class Perro(Animal):
    def sonido(self):
        print("Guau")

class Gato(Animal):
    def sonido(self):
        print("Miau")

Buba = Perro("Dalmata")

Buba.sonido()

# Sardina = Gato()

# Sardina.sonido()

# para ver de que clase parte otra clase
print(Perro.__bases__)

#para ver que subclases tiene una clase
print(Animal.__subclasses__())


tortuga = Animal("Tortuga")

print(tortuga)