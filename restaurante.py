"""
Vamos a gestionar restaurantes

Cada uno tiene:

-- nombre:

-- especialidad:

-- turnos: 

    --- ( Puede haber como máximo 3 clientes)
    -- Si se realiza la reserva diremos "Reserva realizada a [nombre_cliente]
    -- y si no "No se ha podido realizar la serva, pruebe en otro turno"

-- clientes:


Del cliente vamos a necesitar (de momento)

sólo el nombre

Ejemplos de uso:

cliente_1 = Cliente("Anna")

restaurante_1 = Restaurante("Can Pizza", "Italiana", [13,14,15,16,21])

"""
class Cliente():
    def __init__(self, nombre: list):
        self.nombre = nombre

class Restaurantes():
    def __init__(self, nombre, especialidad, turnos: tuple):
        self.nombre = nombre
        self.especialidad = especialidad
        self.turnos = turnos
        self.prog = {13:0,14:0,15:0,16:0,21:0}
    def Reserva(self, cliente: Cliente, turno):
        self.cliente = cliente
        self.turno = turno
        if turno in self.turnos:
            if self.prog[turno]<3:
                self.prog[turno] = self.prog[turno] + 1
                print(f"El cliente {cliente.nombre} ha realizado una reserva en el turno {self.turno}")
            else:
                print("No se pueden realizar mas reservas")    
    
    def __str__(self):
        pass

class Cliente():
    def __init__(self, nombre):
        self.nombre = nombre


restaurante_1 = Restaurantes("Can Pizza", "Italiana", [13,14,15,16,21])

restaurante_1.Reserva(Cliente("Anna"), 13)
restaurante_1.Reserva(Cliente("Maria"), 14)
restaurante_1.Reserva(Cliente("Anna"), 13)
restaurante_1.Reserva(Cliente("Anna"), 13)
restaurante_1.Reserva(Cliente("Anna"), 13)
restaurante_1.Reserva(Cliente("Maria"), 14)


 



