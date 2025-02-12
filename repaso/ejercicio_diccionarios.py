"""
EJERCICIO DICCIONARIOS

Tenemos un sitio que registra los accesos de los usuarios.

Necesitamos un menú con estas opciones
1. Añadiremos un usuario 
        (si no existe ya)
2. Añadiremos una visita al usuario indicado 
        (si el usuario no existe mostrar el error)
3. Mostraremos las visitas del usuario que se decida
        (si el usuario no existe mostrar el error)
4. Mostraremos las visitas de todos los usuarios
        (si no hay usuarios todavía indicarlo)
X. Salir

Consideraremos que el nombre de cada usuario es único

"""

import os
os.system("cls")

def add_user(new_user, users):
    user_dic = {"nombre":new_user, "visitas": 0 }
    users.append(user_dic)
    return (f"Usuario {new_user} añadido correctamente")


users_name = []
users = []
while True:
    menu = """
1. Añadiremos un usuario 
2. Añadiremos una visita al usuario indicado 
3. Mostraremos las visitas del usuario que se decida
4. Mostraremos las visitas de todos los usuarios
X. Salir
"""
    print(menu)
    opcion = input("Elige tu opcion --> ").strip().lower()

    match opcion:
        case "1":
            # Pido al usuario los datos
            new_user = input("Nuevo usuario --> ").strip().title()
            # verificamos si ya hay algún usuario en la lista
            if users:
                # si ya hay algún usuario en la lista
                # debemos verificar que no coincida con new_user
                # lista para guardar los nombres de los usuarios 
                for user in users:
                    # Obtenemos y guardamos los nmbres de los usarios
                    users_name.append(user['nombre'])
                
                # Si el nombre no está en la lista lo añadimos
                if new_user not in users_name:
                    # user_dic = {"nombre":new_user, "visitas": 0 }
                    # users.append(user_dic)
                    # print(f"Usuario {new_user} añadido correctamente")
                    print(add_user(new_user, users))

                else:
                    print("El usuario ya existe")
            else:
                # user_dic = {"nombre":new_user, "visitas": 0 }
                # users.append(user_dic)
                # print(f"Usuario {new_user} añadido correctamente")
                print(add_user(new_user, users))
        case "2": 

            nombre_usuario = input("Nombre usuario --> ").strip().title()
    
            for usuario in users:
                if nombre_usuario == usuario["nombre"]:
                    usuario['visitas'] += 1
                    print(f"Actualizado usuari {nombre_usuario}")
                    break      
        case "3":
            
            nombre_usuario = input("Nombre usuario --> ").strip().title()
    
            for usuario in users:
                if nombre_usuario == usuario["nombre"]:
                    print(f"{nombre_usuario} tiene {usuario['visitas']} visitas")
                    break    
        case "4":
            if users:
                print(users)
            else:
                print("No hay usuarios todavía")
        case "x":
            print("Fin del programa")
            break
        case _ :
            print("Opción no reconocida.\nVuélvelo a probar.")

print(users)