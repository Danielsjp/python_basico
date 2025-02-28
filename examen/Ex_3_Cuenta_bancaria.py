"""

Programación orientada a objetos: Gestión de cuentas bancarias.

El programa debe:

    Definir la clase Cliente, con los atributos nombre, apellido y edad.

    Definir la clase Banco, con el atributo nombre.
    Incluiremos un método "crear_cuenta" para añadir cuentas.
    Incluiremos un método "eliminar_cuenta" para quitarla del banco.
    Incluiremos el método "mostrar_cuentas" para obtener los datos
    de las diferentes cuentas y el total ingresado en el banco. Ejemplo:
    
    Banco Pasta Bank
    ==============================
    Cuenta | Titular | Saldo
    159142 | María   | 500.0€
    295310 | Joan    | 4000€
    Total depósitos: 4500.0€
    ==============================


    Definir la clase CuentaBancaria con los atributos titular y saldo.
    Al crear la cuenta bancaria el saldo será 0.
    Incluiremos un número de cuenta mediante un número aleatorio entre
    100000 y 999999.

    Incluir un método ingresar_dinero(...) que permita añadir dinero a la cuenta.
    Deben ser cantidades positivas mayores que cero. En caso contrario mostrar el aviso.
    El mensaje de salida será:
    "Se han depositado [cantidad]€ en la cuenta de [nombre_del_cliente]"

    Incluir un método retirar_dinero(...) que permita retirar dinero de la cuenta, 
    si hay suficiente saldo para ello. En caso contrario, 
    mostrar un mensaje de saldo insuficiente.
    Ejemplo de mensaje: 
    "Se han retirado [cantidad]€ de la cuenta de [nombre_del_cliente]. 
    Saldo actual: [saldo]€"
    Hay que verificar que la cantidad a retirar sea positiva mayor que cero.

    Incluir un método mostrar_saldo_cliente(...) que muestre el saldo actual.
    Así:
    Cuenta | Titular | Saldo
    159142 | María   | 500.0€
    
     
    Crear al menos 5 cuentas bancarias y utilizar todos 
    los métodos de cada una.

    Nota: no hace falta crear inputs para la entrada de datos.
    Se pueden utilizar directamente los métodos.
"""

#limpiamos la pantalla
import os
os.system('cls')

# Importamos la librería random para generar números aleatorios que usaremos para el número de cuenta
import random

# Clase Cliente
class Cliente:
    # Inicializamos el cliente con nombre, apellido y edad
  
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
      
        
        
    #definimos def __str__() con el mensaje por si queremos imprimir el objeto
    
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.edad} años)"

# Clase CuentaBancaria
class CuentaBancaria:
    # Inicializamos la cuenta con un número de cuenta aleatorio y saldo 0
    def __init__(self, titular: Cliente):
        # Generamos un número de cuenta aleatorio entre 100000 y 999999
        self.numero_cuenta = random.randint(100000, 999999)
        self.titular = titular
        self.saldo = 0.0

    def ingresar_dinero(self, cantidad):
        # Comprobamos que la cantidad a ingresar sea mayor que cero
        if cantidad > 0:
            # Añadimos la cantidad al saldo
            self.saldo += cantidad
            print(f"Se han depositado {cantidad}€ en la cuenta de {self.titular.nombre}")
        else:
            print("La cantidad a ingresar debe ser mayor que cero.")

    def retirar_dinero(self, cantidad):
        # Comprobamos que la cantidad a retirar sea mayor que cero
        if cantidad > 0:
            # Comprobamos que hay saldo suficiente para retirar la cantidad
            if self.saldo >= cantidad:
                self.saldo -= cantidad
                print(f"Se han retirado {cantidad}€ de la cuenta de {self.titular.nombre}. Saldo actual: {self.saldo}€")
            else:
                print(f"Saldo insuficiente en la cuenta de {self.titular.nombre}. Saldo actual: {self.saldo}€")
        else:
            print("La cantidad a retirar debe ser mayor que cero.")

    def mostrar_saldo_cliente(self):
        # Mostramos el saldo del cliente
        print(f"Cuenta | Titular: {self.titular.nombre} | Saldo: {self.saldo}€")
    
    def __str__(self):
        return f"Cuenta de {self.titular.nombre} {self.titular.apellido} con número {self.numero_cuenta} y saldo {self.saldo}€"
    
id = 0
# Clase Banco
class Banco:
    # Inicializamos el banco con un nombre y una lista de cuentas vacía
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = []
        
    def crear_cuenta(self, cuenta):
        # como hago para que una variable cada vez que sea crea una cuenta se incremente en 1 pero que no se reinicie
        # Variable para llevar la cuenta de los registros de cuentas
        #global nos permite modificar la variable id que esta fuera de la funcion
        global id
        # Incrementamos el registro de cuenta
        id += 1
        # Si el registro de cuenta es cada 1000, se imprime un mensaje de premio
        # if registro_de_cuenta % 1000 == 0:
        #print(f"el cliente:{cuenta.titular.nombre} ¡Has ganado un premio!")
        if id % 1000 == 0:
            print(f"el cliente:{cuenta.titular.nombre} ¡Has ganado un premio!")
           
        # Añadimos la cuenta a la lista de cuentas del banco
        self.cuentas.append(cuenta)
        # Mostramos un mensaje de cuenta creada
        print(f"Cuenta creada para {cuenta.titular.nombre} con el número de cuenta {cuenta.numero_cuenta}.")

    # Método1 para eliminar una cuenta del banco
    def eliminar_cuenta(self, numero_cuenta):
        cuenta_a_eliminar = None
        # Buscamos la cuenta con el número de cuenta dado
        for cuenta in self.cuentas:
            # Si encontramos la cuenta, la guardamos en la variable cuenta_a_eliminar
            if cuenta.numero_cuenta == numero_cuenta:
                cuenta_a_eliminar = cuenta
                break

        if cuenta_a_eliminar:
            # Eliminamos la cuenta de la lista de cuentas
            self.cuentas.remove(cuenta_a_eliminar)
            print(f"Cuenta con el número {numero_cuenta} eliminada del banco.")
            #agrergamos el nombre del titular de la cuenta eliminada
            print(f"Perteneciente al cliente {cuenta_a_eliminar.titular.nombre}\n")
        else:
            print("No se encontró una cuenta con ese número.")

    #metodo 2 opcional para eliminar una cuenta del banco por el objeto
    def eliminar_cuenta_by_objeto(self, cuenta: CuentaBancaria):
        if cuenta in self.cuentas:
            self.cuentas.remove(cuenta)
            print(f"Cuenta con el número {cuenta.numero_cuenta} eliminada del banco de la forma más sencilla.")
            #agregamos el nombre del titular de la cuenta eliminada 
            print(f"Perteneciente al cliente {cuenta.titular.nombre}\n") 

    def mostrar_cuentas(self):
        # si existen cuentas en el banco
        if self.cuentas:
            print(f"\nBienvenido a Banco {self.nombre}")
            print("===============================")
            print("Cuenta | Titular | Saldo")
            total_saldo = 0
            #imprimimos las cuentas y el saldo total
            for cuenta in self.cuentas:
                #por si el nombre es compuesto y largo lo acortamos
                if len(cuenta.titular.nombre) > 6:
                    nombre_corto = cuenta.titular.nombre[:6].strip()
                    #imprimimos el nombre corto y los puntos suspensivos
                    print(f"{cuenta.numero_cuenta} | {nombre_corto}...  | {cuenta.saldo}€")
                else:
                    print(f"{cuenta.numero_cuenta} | {cuenta.titular.nombre} | {cuenta.saldo}€")
                total_saldo += cuenta.saldo
           
            print("===============================\n")
            print(f"Total depósitos: {total_saldo}€\n")
        else:
            print("No hay cuentas en el banco.")

    #hacemos un return divertido para agradar al profesor 
    def __str__(self):
        return f"Banco {self.nombre} un banco donde el cliente es lo primero y el dinero... ¡también! por eso cada 1000 cuentas creadas ¡Ganas un premio!"

# Crear instancias de clientes
cliente1 = Cliente("María Dolores Santisima", "González", 30)
cliente2 = Cliente("Joan", "Pérez", 45)
cliente3 = Cliente("Ana", "Sánchez", 25)
cliente4 = Cliente("Luis", "Martínez", 38)
cliente5 = Cliente("Pedro", "López", 50)

# Crear el banco
banco = Banco("Stucom Bank💸")

# Crear cuentas bancarias para los clientes
cuenta1 = CuentaBancaria(cliente1)
cuenta2 = CuentaBancaria(cliente2)
cuenta3 = CuentaBancaria(cliente3)
cuenta4 = CuentaBancaria(cliente4)
cuenta5 = CuentaBancaria(cliente5)

# Añadir cuentas al banco
banco.crear_cuenta(cuenta1)
banco.crear_cuenta(cuenta2)
banco.crear_cuenta(cuenta3)
banco.crear_cuenta(cuenta4)
banco.crear_cuenta(cuenta5)

# Realizar algunas operaciones
cuenta1.ingresar_dinero(500)
cuenta2.ingresar_dinero(4000)
cuenta3.ingresar_dinero(1500)

cuenta1.retirar_dinero(200)
cuenta2.retirar_dinero(1000)

cuenta4.ingresar_dinero(1200)

# Mostrar los saldos de los clientes
cuenta1.mostrar_saldo_cliente()
cuenta2.mostrar_saldo_cliente()
cuenta3.mostrar_saldo_cliente()
cuenta4.mostrar_saldo_cliente()
cuenta5.mostrar_saldo_cliente()

# Mostrar todas las cuentas en el banco
banco.mostrar_cuentas()

banco.eliminar_cuenta(cuenta5.numero_cuenta)

#una forma mas facil es eliminar la cuenta por el objeto
banco.eliminar_cuenta_by_objeto(cuenta4)

# Mostrar las cuentas después de la eliminación
banco.mostrar_cuentas()

#mostramos los strings de los objetos
print(cliente1)
print(cuenta1)
print(banco)
print("\n")

