"""
Devolver la edad a partir de dos fechas

Params

fecha_nacimiento: str -> "dd/mm/aaaa
fecha_actual: str -> "dd/mm/aaaa

Return
edad: int


Códigos de error:

-1 : día o mes incorrecto
-2 : la fecha de nacimiento debe ser igual o menor que la actual

"""

def calcula_edad(fecha_nacimiento : str, fecha_actual : str) -> int:
       
    """
    Devolver la edad a partir de dos fechas

    Params

    fecha_nacimiento: str -> "dd/mm/aaaa
    fecha_actual: str -> "dd/mm/aaaa

    Return
    edad: int


    Códigos de error:

    -1 : día o mes incorrecto
    -2 : la fecha de nacimiento debe ser igual o menor que la actual
    
    
    """
    fecha_actual = fecha_actual.split("-")
    #Este segundo split por si el usuario pone espacios, pero no es habitual.
    dia_actual = int(fecha_actual[0])
    mes_actual = int(fecha_actual[1])
    anyo_actual = int(fecha_actual[2])

    fecha_nacimiento = fecha_nacimiento.split("-")
    dia_nacimiento = int(fecha_nacimiento[0])
    mes_nacimiento = int(fecha_nacimiento[1])
    anyo_nacimiento = int(fecha_nacimiento[2])
            
    #No puede ser que un mes sea menor que 1 y mayor a 12
    #No puede ser que un dia sea menor a 1 y mayor que 31

    if (not 1 <= mes_actual <= 12) \
        or (not 1 <= mes_nacimiento <= 12) \
            or (not 1 <= dia_actual <= 31) \
                or (not 1 <= dia_nacimiento <= 31):
        return -1
    
    dif_anyos = anyo_actual - anyo_nacimiento
    dif_meses = mes_actual - mes_nacimiento
    dif_dias = dia_actual - dia_nacimiento

    if (dif_anyos < 0)\
          or (dif_anyos == 0 and dif_meses < 0) or (dif_anyos == 0 and dif_meses == 0 and dif_dias < 0):
        return -2
    
    # despues de eso ahora viene calculo de la edad

    if anyo_actual > anyo_nacimiento:
        
        if mes_actual >= mes_nacimiento:

            if dia_actual >= dia_nacimiento:
                
                return dif_anyos
            
            else:
                
                return dif_anyos-1
            
        else: 
        
            return dif_anyos-1
    

print(calcula_edad("02-10-1982", "18-02-2025"))