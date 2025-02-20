"""

Vamos a crear una clase llamada Persona.

tendrá estos atributos:

-- nombre

-- apellido

-- ciudad

Crear el constructor y el método que muestra la informacion de la clase (print(objeto))

También habrá una clase hija llamada Cliente.

Tendrá además los atributos: 

-- dni
-- compras

Cuando se muestr el objeto debe aparecer todos los atributos.

Hay que crear un método que tenga esta salida:

El cliente fulanito ha comprado xx.xx €

"""

class Persona():
    def __init__(self, nombre: str, apellido: str, ciudad: str):
        self.nombre = nombre
        self.apellido = apellido
        self.ciudad = ciudad
    def __str__(self):
        #return self.especie
        print(f"{self.nombre} - {self.apellido} - {self.ciudad}")
    
        
Pepita = Persona("Pepita", "Sanchez", "Barcelona")       

class Cliente(Persona):
    def __init__(self, nombre, apellido, ciudad, dni, compras):
        # self.nombre = nombre
        # self.apellido = apellido
        # self.ciudad = ciudad
        super().__init__(nombre, apellido, ciudad)
        self.dni = dni
        self.compras = compras
    def __str__(self):
        super().__str__()
        return (f"{self.dni} - {self.compras}")
    def compras_realizadas(self):
        return f"El cliente {self.nombre} ha comprado {self.compras} €"

        
Pepita2 = Cliente("Ramon", "Garcia", "Valencia", "1234", 300)

print(Pepita2)

print(Pepita2.compras_realizadas())



