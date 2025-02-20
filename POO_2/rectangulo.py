"""
Hay que crear una clase llamada Rectangulo.

Necesitamos los métodos para obtener el área, el periímetro y la diagonal de la figura

Cada uno con un metodo diferente

Lo probaremos con un rectangulo de lados 3 y 4



"""

class Rectangulo():
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
    def __str__(self):
       pass
    def calcular_area(self):
        self.area = (self.lado1 * self.lado2)
        return self.area
    def calcular_perimetro(self):
        self.perimetro = (self.lado1 + self.lado2)*2
        return self.perimetro
    def calcular_diagonal(self):
        self.diagonal = ((self.lado1)**2 + (self.lado2)**2)**0.5
        return self.diagonal

        
prueba_rectangulo = Rectangulo(3, 4)

print(prueba_rectangulo.calcular_area())
print(prueba_rectangulo.calcular_perimetro())
print(prueba_rectangulo.calcular_diagonal())