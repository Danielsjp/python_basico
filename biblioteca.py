"""
Programación Orientada a Objetos: Biblioteca

El programa debe crear las siguientes clases con sus métodos:

    Clase Lector, que se construirá con nombre y apellido

    Clase Libro, que se construirá con nombre_autor, apellido_autor,
    y título

    Clase Biblioteca, que se construirá con nombre y dirección
    Esta clase dispondrá de los siguientes métodos:
    - agregar_lector: agrega un lector a la biblioteca
    - mostrar lectores
    - agregar_libro: agrega un libro a la biblioteca,
        indicando los ejemplare disponibles
    - buscar_libro: busca un libro en la biblioteca, 
        indicando si lo tiene o no
    - mostrar libros de la biblioteca


"""
from collections import Counter

class Lector():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

groucho = Lector("Groucho", "Marx")

daniel = Lector("Daniel", "Sanchez")

class Libro():
    def __init__(self, nombre_autor, apellido_autor, titulo):
        self.nombre_autor = nombre_autor
        self.apellido_autor = apellido_autor
        self.titulo = titulo

el_quijote = Libro("Miguel de Cervantes", "Saavedra", "El quijote")    
firmin = Libro("Pepito", "Rodriguez", "Firmin")

class Biblioteca():
    
    def __init__(self, nombre, dirección):
        self.nombre = nombre
        self.dirección = dirección
        self.lista_lectores = []
        self.lista_libros = []
        self.lista_stock = []
    
    def agregar_lector(self, cliente: Lector):
        if cliente in self.lista_lectores:
              print(f"Ya existe {cliente.nombre}")
        else:
            self.lista_lectores.append(cliente)        

    def mostrar_lectores(self):
       for valor in self.lista_lectores:
           print(f"{valor.nombre}, {valor.apellido}")

    def agregar_libro(self, libro: Libro):
            
            #i = 0
            self.libro = libro
            self.lista_libros.append(libro.titulo)
            self.lista_stock = []
            self.my_dict = {}
            self.my_dict = {i:self.lista_libros.count(i) for i in self.lista_libros}
            print("---")
            print(self.my_dict)
                #if self.libro.titulo in self.lista_libros:
                # for item in self.lista_libros:
                #     if item.titulo == self.libro.titulo:
                #         i +=1
                #         stock = {"Libro": self.libro.titulo, "Cantidad": i}        
                #         #print (f"Cantidad {i}, Se ha agregado el libro {libro.titulo}")
                #         self.lista_stock.append(stock.update(stock))

    def reservar_libro(self, libro: Libro, cliente: Lector):
            self.libro = libro
            self.cliente = cliente
            self.reserva = {}
            self.lista_reservas = []
            print (f"Reserva de {self.libro.titulo}")
            if self.libro.titulo in self.lista_libros:
                for name, cantidad in self.my_dict.items():
                    if name == self.libro.titulo:
                        if self.cliente in self.lista_lectores:
                            print(f"el stock de {name} es {cantidad}")
                            new_stock = {name: cantidad-1}
                            self.my_dict.update(new_stock)
                            self.reserva = {self.cliente.nombre, self.libro.titulo}
                            if cantidad == 0:
                                print("NO HAY EXISTENCIAS")
                                break
                            else:
                                self.lista_reservas.append(self.reserva)
                            for name, cantidad in self.my_dict.items():
                                if name == self.libro.titulo:
                                    print(f"el stock actualizado de {name} es {cantidad}")
                                    print(self.my_dict)
                                    print(self.reserva)
            else:
                print("BYE")         
                        
    def buscar_libro(self, name):
        self.name = name
        if self.name in self.lista_libros:   
            print(f"{self.name} existe")
        else:
            print(f"{self.name} no existe")   

    def mostrar_libros(self):
        i = 0
        for item in self.lista_libros:
            i +=1
            print(f"{i}-{item.titulo}")

    def __str__(self):
        pass

sofia_barat = Biblioteca("Sofia Barat", "Carrer Girona 94")

sofia_barat.agregar_lector(groucho)
# # sofia_barat.agregar_lector(groucho)
sofia_barat.agregar_lector(daniel)
# # sofia_barat.agregar_lector(daniel)
# sofia_barat.agregar_libro(firmin)
#sofia_barat.agregar_libro(firmin)
sofia_barat.agregar_libro(firmin)
sofia_barat.agregar_libro(el_quijote)
#sofia_barat.agregar_libro(firmin)
#sofia_barat.agregar_libro(firmin)
# sofia_barat.mostrar_lectores()
sofia_barat.buscar_libro("El quijote")
#sofia_barat.agregar_libro(firmin)
#sofia_barat.agregar_libro(firmin)
#sofia_barat.agregar_libro(firmin)
#sofia_barat.agregar_libro(firmin)
#sofia_barat.reservar_libro(firmin)
sofia_barat.reservar_libro(el_quijote, daniel)
sofia_barat.reservar_libro(firmin, groucho)
#sofia_barat.reservar_libro(el_quijote)
