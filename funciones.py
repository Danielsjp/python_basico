"""
FUNCIONES
"""

# Declaración
def sumar(a, b):
        print(a+b)
    
# Invocación
sumar(1,4)

# Declaración con parametros
def sumar2(num1, num2):
        return num1 + num2
    
#argumentos 3,5, hola, manolo....

print(sumar2(3,5))

print(sumar2("hola ","Manolo"))


#Ejemplos de funciones:
#--- ver si un numero es primo o no
#--- corregir nombres mal escritos
#--- calcular dias horas etc de unos segundos
#--- para calcular los dias que faltan para una fecha

#el scope(ambito) de la variable es que si esta dentro de  una funcion no se ve fuera de ella... 
# 

def prueba_variable() :
    variable = "Soy una prueba"

print(variable)
