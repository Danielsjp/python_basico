"""
SET -> conjunto lógico
Los set no pueden tener valores repetidos
"""

lista_numeros = [1, 2, 2, 5, 7, 5, 4, 1]

lista_sin_repeticiones = list(set(lista_numeros))

print(lista_sin_repeticiones)