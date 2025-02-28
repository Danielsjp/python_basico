"""
LISTAS

Escriba un programa que permita crear una lista de palabras y que, a continuación, 
pida una palabra y diga cuántas veces aparece esa palabra en la lista.

Mediante este menú:

        LISTA DE PALABRAS

        Elige una opción:
        1. Crear lista, preguntando cuantas palabras incluirá
        2. Buscar palabra
        3. Añadir palabra a la lista
        4. Borrar palabra de la lista (si existe)
        5. Mostrar la lista de palabras

        Cualquier otra opción para salir

        Tu elección es ....

Requerimientos:

    -- Las opciones 2-3-4-5 deben verificar que existan elementos en la lista.
        Si no hay, mostrar el correspondiente mensaje.

    -- La opción 1 siempre crea una lista nueva. Por tanto elimina la
        lista anterior si existe.

    -- Cuando se pregunte cuantas palabras incluirá la lista, no hay que
        verificar que sea un número. Se asume que el usuario escribe un número.
        Lo que sí que se debe comprobar es que sea mayor a 0.

Posibles mejoras:

    -- Añadir una opción para editar una palabra en la lista.
    
    -- Añadir una opción para borrar todas las palabras de la lista.

    -- Comprobar que al pedir la cantidad de palbras de la lista, el usuario
        escribe un número entero.

    -- Y lo que se te ocurra...

  
"""
#limpiamos la pantalla
import os
os.system('cls')

#creamos la función menu para mostrar las opciones
def menu():
    print("LISTA DE PALABRAS")
    print("\nElige una opción:")
    print("1. Crear lista, preguntando cuántas palabras incluirá")
    print("2. Buscar palabra")
    print("3. Añadir palabra a la lista")
    print("4. Borrar palabra de la lista (si existe)")
    print("5. Mostrar la lista de palabras")
    print("Cualquier otra opción para salir\n")

#creamos la función crear_lista para crear la lista de palabras
def crear_lista():
    #definimos global la variable lista_palabras para poder modificarla fuera de la función
    global lista_palabras
    #creamos un bucle para que el usuario introduzca un número mayor que 0
    while True:
        #el try-except es para que si el usuario introduce un valor que no sea un número entero, se le pida que lo haga
        try:
            #definimos la variable n y cambiamos el tipo por defecto string a int
            n = int(input("¿Cuántas palabras incluirá la lista? "))
            # si el usuario indica un numero mayor que 0, se entra en el if
            if n > 0:
                #aqui se crea la lista de palabras vacía
                lista_palabras = []
                #se crea un bucle con el tamaño indicado en n para que el usuario introduzca las palabras
                for i in range(n):
                    palabra = input(f"Ingrese la palabra {i+1}: ")
                    #con append se añade la palabra al final de la lista
                    lista_palabras.append(palabra)
                    #se muestra un mesaje de confirmación
                print("Lista creada exitosamente.")
                #saliendo del bucle una vez creada la lista con el tamaño indicado
                break
            #si el usuario introduce un número menor o igual a 0, se le pide que lo haga de nuevo
            else:
                print("Debe ingresar un número mayor que 0.")
                #el except valuerror es para que si el usuario introduce un valor que no sea un número entero, se le pida que lo haga
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
#creamos la funcion buscar_palabra para buscar una palabra en la lista
def buscar_palabra():
    #si la lista esta vacía, se muestra un mensaje
    if not lista_palabras:
        print("La lista está vacía.")
        #si la lista está vacía, se sale de la función
        return
    #se pide al usuario que introduzca la palabra que desea buscar
    palabra = input("Ingrese la palabra que desea buscar: ")
    #se cuenta cuantas veces aparece la palabra en la lista
    conteo = lista_palabras.count(palabra)
    #si el conteo es mayor que 0, se muestra un mensaje con el número de veces que aparece la palabra
    if conteo > 0:
        print(f"La palabra '{palabra}' aparece {conteo} vez/veces en la lista.")
        #si el conteo es 0, se muestra el mensaje
    else:
        print(f"La palabra '{palabra}' no se encuentra en la lista.")
#creamos la función añadir_palabra para añadir una palabra a la lista
def añadir_palabra():
    #esto verifica que la lista no esté vacía
    if not lista_palabras:
        print("La lista está vacía.")
        #si la lista está vacía, se sale de la función
        return
    #se pide al usuario que introduzca la palabra que desea añadir
    palabra = input("Ingrese la palabra que desea añadir: ")
    #se añade la palabra al final de la lista
    lista_palabras.append(palabra)
    #se muestra un mensaje de confirmación
    print(f"La palabra '{palabra}' ha sido añadida a la lista.")
#creamos la función borrar_palabra para borrar una palabra de la lista
def borrar_palabra():
    #lo mismo que en las funciones anteriores, se verifica que la lista no esté vacía
    if not lista_palabras:
        print("La lista está vacía.")
        #si la lista está vacía, se sale de la función
        return
    #se pide al usuario que introduzca la palabra que desea borrar
    palabra = input("Ingrese la palabra que desea borrar: ")
    #si la palabra está en la lista, se entra en el if
    if palabra in lista_palabras:
        #se borra la palabra de la lista con remove
        lista_palabras.remove(palabra)
        #se muestra un mensaje de confirmación
        print(f"La palabra '{palabra}' ha sido borrada de la lista.")
    else:
        #si la palabra no está en la lista, se muestra un mensaje tambien
        print(f"La palabra '{palabra}' no se encuentra en la lista.")

#esta funciona muestra la lista de palabras
def mostrar_lista():
    #si la lista está vacía, se muestra un mensaje
    if not lista_palabras:
        print("La lista está vacía.")
    #si la lista no está vacía, se muestra la lista de palabras directamente accediendo a la variable global
    else:
        print("Lista de palabras:", lista_palabras)
#esta función es la principal, donde se llama a las funciones anteriores
def main():
    #se define la variable global lista_palabras pero ya estaba creada antes porque se necesita en todas las funciones donde se llama
    global lista_palabras
    lista_palabras = []
    #se crea un bucle infinito para que el menú se muest
    while True:
        #se llama a la función menu que muestra las opciones
        menu()
        #se pide al usuario que elija una opción
        try:
            #se cambia el tipo de dato de la opción de string a int
            opcion = int(input("Tu elección es: "))
            #si el usuario elige la opción 1, se llama a la función crear_lista
            if opcion == 1:
                crear_lista()
                #si el usuario elige la opción 2, se llama a la función buscar_palabra
            elif opcion == 2:
                buscar_palabra()
            elif opcion == 3:
                #si el usuario elige la opción 3, se llama a la función añadir_palabra
                añadir_palabra()
            elif opcion == 4:
                #si el usuario elige la opción 4, se llama a la función borrar_palabra
                borrar_palabra()
            elif opcion == 5:
                #si el usuario elige la opción 5, se llama a la función mostrar_lista
                mostrar_lista()
            else:
                #si el usuario elige cualquier otra opción, se muestra un mensaje y se sale del programa
                print("Saliendo del programa.")
                break
            #si el usuario elige una opción que no sea un número, se muestra un mensaje
        except ValueError:
            print("Opción inválida. Por favor, ingrese un número del 1 al 5, o cualquier otra opción para salir.")

#se llama a la función principal que contiene la llama a las demás funciones y ejecuta el programa
main()

