dia_Semana=input("¿Que día de la semana es?").lower()
match dia_Semana:
    case "lunes":
        print("Toca sistemas")
    case "martes" | "miercoles"| "miércoles" |"jueves" | "viernes" :
        print("Toca Python")
    case "sabado" | "sábado" |"domingo":
        print("Es fin de semana!!! yuuuuhuhu")
    case _:
        print("Creo que estás confundido")