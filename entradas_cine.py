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
os.system('cls' if os.name == 'nt' else 'clear')

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

def comprar_entradas(cantidad, case):
    if case == 1:
        ticket_estandard.append(cantidad*estandard)
    if case == 2:    
        ticket_mayores.append(cantidad*mayores)
    if case == 3:
        ticket_menores.append(cantidad*infantiles)

iterar = True

while iterar:
    
    print("")
    print("-------TPV D3 ENTRADAS------")
    print("")
    print("1 .- Entrada estándar: 9.00")
    print("2 .- Mayores de 65 años (seniors) : 6.90")
    print("3 .- Infantiles : 7.20")
    print("4 .- Indicar Importe Total")
    print("x - para salir")
    print("")

    opcion = input("Elige tu opcion --> ")

    match opcion:
        case '1':
            case = 1
            cantidad = float(input("¿Cantidad de entradas?"))
            comprar_entradas(cantidad, case)
            seguridad = True
            pass

        case '2':
            case = 2
            cantidad = float(input("¿Cantidad de entradas?"))
            comprar_entradas(cantidad, case)
            seguridad = True
            pass

        case '3':
            case = 3
            if seguridad:
                cantidad = float(input("¿Cantidad de entradas?"))
                comprar_entradas(cantidad, case)
                pass
            else:
                seguridad = input("¿va el menor acompañado responda: Si / No?")
                if seguridad == 'Si':
                    cantidad = float(input("¿Cantidad de entradas?"))
                    comprar_entradas(cantidad, case)
                else:
                    print("no se pueden vender entradas a menores no acompañados")
                    #break
                    iterar = False

        case '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("")
            print("########################################################################")
            total = sum(ticket_estandard) + sum(ticket_mayores) + sum(ticket_menores)
            print(f"Cantidad tickets estandard {round(sum(ticket_estandard)/estandard)} total: {sum(ticket_estandard)} Euros")
            print(f"Cantidad tickets mayor edad {round(sum(ticket_mayores)/mayores)} total: {sum(ticket_mayores)} Euros")
            print(f"Cantidad tickets menores {round(sum(ticket_menores)/infantiles)} total: {sum(ticket_menores)} Euros")
            print("")
            print(f"-------------------->> Total {total} Euros")
            print("Gracias por su visita")
            print("########################################################################")
            pass

        case 'x':

            print("Saliendo....")
            #break        
            iterar = False
else:
    print("Programa finalizado")            