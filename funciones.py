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

# def prueba_variable() :
#     variable = "Soy una prueba"

# print(variable)

def mostrar_datos_alumno(nombre, apelido, becado= False):
        if becado:
                becado = "Sí"
        else:
                becado = "No"

        return f"¿el alumno {nombre} {apelido} tiene beca? {becado}"

alumno_1 = mostrar_datos_alumno("Anna", "Diaz")
alumno_2 = mostrar_datos_alumno("Juan", "Sanchez", True)

print(alumno_1)
print(alumno_2)
        
def multiples_argumento(*argv):
        for valor in argv:
                suma = valor + valor
        print(suma)

multiples_argumento(1,2,3)