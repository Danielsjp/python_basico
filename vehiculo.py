'''
Crea una clase llamada Vehiculo.

En su constructor incluye marca, modelo y año de construcción.

Dos métodos también:
-- arrancar, con el mensaje "El vehículo XX modelo YY ha arrancado"
-- detener, con el mensaje "El vehículo XX modelo YY se ha detenido"

Luego, dos clases hijas: Coche y Moto

La clase Coche tiene dos atributos propio: numero de puertas y AC (verdadero o falso).
y también un método propio: abrir_maletero, que
devuelve este mensaje: "El maletero del [marca] [modelo] está abierto"

La clase Moto tiene un método propio: revisar_seguridad, devuelve este mensaje:
"Si circulas en motocicleta debes llevar casco"
'''

class Vehiculo():
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
    def __str__(self):
        pass
    def arrancar(self):
        return f"El vehiculo {self.marca} modelo {self.modelo} ha arrancado"
    def detener(self):
        return f"El vehiculo {self.marca} modelo {self.modelo} se ha detenido"
    
class Coche(Vehiculo):
    def __init__(self, marca, modelo, anio, puertas, AC: bool):
        super().__init__(marca, modelo, anio)
        self.puertas = puertas
        self.AC = AC
    def __str__(self):
        pass
    def abrir_maletero(self):
        return f"El maletero del {self.marca} - {self.modelo} esta abierto"

class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, AC: bool):
        super().__init__(marca, modelo, anio)
        #self.puertas = puertas
        self.AC = AC
    def __str__(self):
        pass
    def revisar_seguridad(self):
        return f"Si circulas en motocicleta debes llevar casco"
    

vehiculo = Vehiculo("Opel", "Corsa", 1990)
print(vehiculo.arrancar())
coche = Coche("FERRARI", "Gacela", 2019, 4, True)
print(coche.abrir_maletero())
moto = Moto("yamaha", "nmax", 2019, True)
print(moto.revisar_seguridad())