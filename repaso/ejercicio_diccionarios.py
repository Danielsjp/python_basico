"""
EJERCICIO DICCIONARIOS

Tenemos un sitio que registra los accesos de los usuarios.

Necesitamos un menu con estas opciones 

"""

users = [] 
visitas = 1


a=True

while a==True:
    menu = """1. Añadiremos un usuario
        (si no existe ya)
    2. Añadiremos una visita al usuario indicado
        ( si el usuario no existe mostrar el error)
    3. Mostraremos las visitas del usuario que se decida
        (si el usuario no existe mostrar el error)
    4.- Mostraremos las visitas de todos los usarios
        ( si no hay usuarios todavia indicarlo)
    X.- Salir\n\n\n
    """

    print(menu)
    opcion = input("introduce tu opcion ->")

    match opcion:
        case "1":
            new_user = input("Nuevo usuario -->").strip().title()
            if users:
                for user in users:
                    if user["nombre"] == new_user:
                        print("Ya existe el usuario")
                    else:
                        user_dic = {"nombre":new_user, "visitas": visitas}
                        users.append(user_dic)
            else:
                user_dic = {"nombre":new_user, "visitas": 1}
                users.append(user_dic)
        case "2":
            visita_usuario = input("Visita del usuario -->").strip().title()
            if users:
                for user in users:
                    if user["nombre"] == visita_usuario:
                        visitas += 1
                        user_dic.update({"nombre": visita_usuario, "visitas": visitas})
                    else:
                        print("El usuario no existe")
        case "3":
            pass
        case "4":
            if users:
                print(users)
            else:
                print("no hay usuarios todavia")
        case "x":
            a=False