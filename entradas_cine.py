"""
ENTRADAS DEL CINE
Vamos a crear una app para vender entradas del cine.
Hay tres precios:
- Entrada estándar: 9.00
- Mayores de 65 años (seniors) : 6.90
- Infantiles : 7.20
Se puede vender cualquier cantidad de entradas,
pero los menores siempre deber ir acompañados
de un adulto.
Al finalizar la compra mostraremos las entradas 
y el importe total. 
"""

#limpiamos la pantalla
import os
os.system("cls")

#listas que contienen cantidad de tickets.
ticket_estandard = []
ticket_mayores = []
ticket_menores = []

# precio entradas
estandard = 9.00
mayores = 6.90
infantiles = 7.20

# checks

seguridad = False

while True:

    print("TPV DE ENTRADAS")
    print("1 .- Entrada estándar: 9.00")
    print("2 .- Mayores de 65 años (seniors) : 6.90")
    print("3 .- Infantiles : 7.20")
    print("4 .- Indicar Importe Total")
    print("x - para salir")
    opcion = input("Elige tu opcion --> ").strip().lower()

    match opcion:
        case '1':
            cantidad = float(input("¿Cantidad de entradas?"))
            ticket_estandard.append(cantidad*estandard)
            seguridad = True
            pass

        case '2':
            cantidad = float(input("¿Cantidad de entradas?"))
            ticket_mayores.append(cantidad*mayores)
            seguridad = True
            pass

        case '3':
            
            if seguridad:
                cantidad = float(input("¿Cantidad de entradas?"))
                ticket_menores.append(cantidad*infantiles)
                pass
            else:
                seguridad = input("¿va el menor acompañado responda: Si / No?")
                if seguridad == 'Si':
                    pass
                else:
                    print("no se pueden vender entradas a menores no acompañados")
                    break

                

        case '4':
            total = sum(ticket_estandard) + sum(ticket_mayores) + sum(ticket_menores)
            print(f"Cantidad tickets estandard {round(sum(ticket_estandard)/estandard)} total: {sum(ticket_estandard)}")
            print(f"Cantidad tickets mayor edad {round(sum(ticket_mayores)/mayores)} total: {sum(ticket_mayores)}")
            print(f"Cantidad tickets menores {round(sum(ticket_menores)/infantiles)} total: {sum(ticket_menores)}")
            print(f"Cantidad {total}")
            print("Gracias por su visita")
            pass
        case 'x':
            print("Saliendo....")
            break        
            