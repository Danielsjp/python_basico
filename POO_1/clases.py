# la plantilla seria persona y la instancia se genera al persona_1 = Persona()
# nombre y apellido serian atributos

class Persona():
    
    """
    
    Propiedades de una persona
    
    """
    # METODOS 
    # METODO DE INSTANCIA

    def __init__(self, nombre, apellido, funcion):
        self.nombre = nombre
        self.apellido = apellido
        self.funcion = funcion

    def __str__(self):
        return f"Nombre: {self.nombre}, apelido: {self.apellido}, funcion: {self.funcion}"

# Un objeto es la instancia de una clase

persona_1 = Persona("Peter", "Parker", "Alumno")

print(type(persona_1))

persona_1.nombre = "Manolo"

print(persona_1.nombre)

print(persona_1)

