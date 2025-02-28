"""
AGENDA

Escribir un programa que implemente una agenda.
Supondremos que siempre se indicarán nombres diferentes.

En la agenda se podrán guardar nombres y números de teléfono. 
El programa nos dará el siguiente menú:

* Añadir/modificar: Nos pide un nombre. 
    -- Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, 
    opcionalmente, permitir modificarlo si no es correcto, preguntando
    al usuario si quiere hacerlo. 
    -- Si el nombre no se encuentra debe añadirlo y también el teléfono correspondiente.

* Buscar: Nos pide una cadena de caracteres, 
    y nos muestras todos los contactos 
    cuyos nombres comiencen por dicha cadena.
    Por ejemplo, podemos tener contactos llamados "Mario", María", "Maria", "Mar",
    "Marta". Si buscamos "Mar" nos mostrará todos ellos. 
    Si no hay ningún contacto que comience por dicha cadena, 
    muestra el correspondiente mensaje de aviso:
    "No hay contactos que comiencen por la cadena introducida."

* Borrar: Nos pide un nombre completo y si existe nos preguntará si queremos borrarlo de la agenda. 
    Si no existe muestra el correspondiente mensaje de aviso.

* Listar: Nos muestra todos los contactos de la agenda.
    Si no hay ningún contacto, muestra el correspondiente mensaje de aviso.

* Salir, con un saludo final

Implementar el programa con un diccionario.
Como elemento de selección en el menú puedes usar letras, números o palabras completas
    (por ejemplo, "Añadir", "1", "A"), o incluso emojis.



Posibles mejoras:

* Implementar una opción en el menú que permita buscar un contacto por número de teléfono.

* Implementar el código como una función.

* Y lo que se te ocurra...

"""



#limpiamos la pantalla
import os
os.system('cls')
#guardamos el usuario que esta utilizando el programa
usuario=(os.getlogin())

def menu():
    

    print("┌────────────────────────┐")
    print(f"│AGENDA DE CONTACTOS DE: │")
    print(f"│    {usuario}        │")
    print("└────────────────────────┘")
    print("Elige una opción:")
    print("1. Añadir/modificar")
    print("2. Buscar por nombre")
    print("3. Buscar por número de teléfono")
    print("4. Borrar contacto")
    print("5. Listar todos los contactos")
    print("6. Borrar por prefijo")
    print("6. Salir\n")

def obtener_pais_por_prefijo(telefono):
    # Diccionario de prefijos internacionales más comunes
    prefijos_paises = {
        "+1": "USA/Canada",
        "+34": "España",
        "+44": "Reino Unido",
        "+49": "Alemania",
        "+33": "Francia",
        "+39": "Italia",
        "+55": "Brasil",
        "+52": "México",
        "+61": "Australia",
        "+81": "Japón"
    }
    
    # Verificar si el número empieza con alguno de los prefijos del diccionario
    for prefijo, pais in prefijos_paises.items():
        if telefono.startswith(prefijo):
            return pais  # Si coincide el prefijo, devolvemos el país
    
    return "Unknown country"  # Si no coincide con ninguno, devolvemos "Unknown country"

def añadir_modificar(agenda):
    nombre = input("Introduce el nombre: ")
    #si el nombre se encuentra en la agenda, se muestra el nombre y el numero de telefono y permite modificarlo
    if nombre in agenda:
        print(f"El teléfono de {nombre} es {agenda[nombre]}")
        modificar = input("¿Quieres modificar el teléfono? (sí/no): ").strip().lower()
        if modificar == "sí":
            telefono = input("Introduce el nuevo teléfono: ")
            print("¿El número de teléfono es español?")
            respuesta = input("sí/no: ")
        if respuesta == "sí":
            agenda[nombre] = "+34 "+telefono
        else:
            print("introzca el prefijo del país")
            prefijo = input("Introduce el prefijo del país: ")
            agenda[nombre] = "+"+prefijo+" " + telefono    
    #si el nombre no se encuentra en la agenda, se añade el contacto    
    else:
        telefono = input(f"{nombre} no está en la agenda. Introduce el número de teléfono: ")
        #se añade el contacto al diccionario agenda
        print("¿El número de teléfono es español?")
        respuesta = input("sí/no: ")
        if respuesta == "sí":
            agenda[nombre] = "+34 "+telefono
        else:
            print("introzca el prefijo del país")
            prefijo = input("Introduce el prefijo del país: ")
            agenda[nombre] = "+"+prefijo+" " + telefono    
        print(f"Contacto {nombre} añadido con el número {telefono}.")
#una vez tenemos agenda con los contactos, se llama a la función buscar_por_nombre para buscar un contacto
def buscar_por_nombre(agenda):
    cadena = input("Introduce la cadena de caracteres para buscar: ")
    #si el nombre del contacto empieza por la cadena introducida, se guarda en la lista encontrados
    encontrados = [f"{nombre}: {num}" for nombre, num in agenda.items() if nombre.startswith(cadena)]
    #si se encuentra el contacto, se muestra el nombre y el numero de telefono
    if encontrados:
        #todo lo que hay ena lista encontrados y ha coincidido con la cadena introducida se muestra
        print(f"Contacto(s) encontrado(s): {', '.join(encontrados)}")
    #si no se encuentra el contacto, se muestra un mensaje
    else:
        print("No se encontró ningún contacto con ese nombre.")
    
        

def buscar_por_telefono(agenda):
    #se pide al usuario que introduzca el numero de telefono a buscar en la agenda verificando que sea un numero
    telefono = input("Introduce el número de teléfono para buscar: ")
    encontrados = [nombre for nombre, num in agenda.items() if num == telefono]
    #si el telefono se encuentra en la agenda, se guarda el nombre en la lista encontrados
    if encontrados:
        #se muestra el nombre del contacto encontrado
        print(f"Contacto(s) encontrado(s): {', '.join(encontrados)}")
    else:
        print("No se encontró ningún contacto con ese número de teléfono.")

def borrar_contacto(agenda):
    nombre = input("Introduce el nombre del contacto a borrar: ")
    #si el nombre se encuentra en la agenda, se pregunta al usuario si quiere borrarlo
    if nombre in agenda:
        confirmar = input(f"¿Estás seguro de que quieres borrar a {nombre}? (sí/no): ").strip().lower()
        #si ponemos si, se entra en el if y se borra el contacto
        if confirmar == "sí":
            #borramos el contacto de la agenda con el metodo pop
            agenda.pop(nombre)
            print(f"{nombre} ha sido borrado de la agenda.")
    else:
        #si el contacto no se encuentra en la agenda, se muestra un mensaje
        print(f"No se encontró el contacto {nombre} en la agenda.")

def listar_contactos(agenda):
    if agenda:
        print("Contactos en la agenda:\n")
        #recorremos el diccionario para mostrar el nombre y el numero de telefono
        for nombre, telefono in agenda.items():
            if telefono.startswith("+34"):
                print(f"{nombre}: {telefono} {obtener_pais_por_prefijo(telefono)}")
            else:
                print(f"{nombre}: {telefono} {obtener_pais_por_prefijo(telefono)}")
    else:
        print("La agenda está vacía.")
        #se le pregunta al usuario si quiere añadir un contacto y si dice si llama a la función añadir_modificar
        añadir = input("¿Quieres añadir un contacto? (sí/no): ").strip().lower()
        if añadir == "sí":
            añadir_modificar(agenda)

def borrar_por_prefijo(agenda):
    count = 0
    prefijo = input("Introduce el prefijo del país: ejemplo +34: ")
    #se recorre el diccionario agenda para buscar el prefijo introducido
    # y se guarda en la lista encontrados
    encontrados = [nombre for nombre, num in agenda.items() if num.startswith(prefijo)]
    #si se encuentra el prefijo, se muestra el nombre y el numero de telefono
    if encontrados:
        #borra
        print(f"Contacto(s) que se borraran: {', '.join(encontrados)}")
        #delete en bucle
        for nombre in encontrados:
            agenda.pop(nombre)
            count = count + 1
        print(f"Se han borrado {count} contactos con el prefijo {prefijo}.")
    else:
        print("No se encontró ningún contacto con ese prefijo.")

def main():
    #creamos un diccionario vacio para guardar los contactos
    agenda = {}
    #bucle infinito para mostrar el menu hasta que el usuario decida salir
    while True:
        #se llama a la función menu que muestra las opciones
        menu()
        #se pide al usuario que elija una opción y con strip y lower se eliminan los espacios y se pasa a minusculas
        opcion = input("Tu elección es: ").strip().lower()

        if opcion == "1" or opcion == "Añadir" or opcion == "A":
            #se llama a la función añadir_modificar pasando el diccionario agenda como argumento
            añadir_modificar(agenda)
        elif opcion == "2" or opcion == "Buscar" or opcion == "B":
            #se llama a la función buscar_por_nombre pasando el diccionario agenda como argumento
            buscar_por_nombre(agenda)
        elif opcion == "3" or opcion == "Buscar teléfono" or opcion == "T":
            #se llama a la función buscar_por_telefono pasando el diccionario agenda como argumento
            buscar_por_telefono(agenda)
        elif opcion == "4" or opcion == "Borrar" or opcion == "D":
            #se llama a la función borrar_contacto pasando el diccionario agenda como argumento
            borrar_contacto(agenda)
        elif opcion == "5" or opcion == "Listar" or opcion == "L":
            #se llama a la función listar_contactos pasando el diccionario agenda como argumento
            listar_contactos(agenda)
        elif opcion == "6" or opcion == "Borrar por prefijo" or opcion == "P":
            #se llama a la función borrar_por_prefijo pasando el diccionario agenda como argumento
            borrar_por_prefijo(agenda)
        elif opcion == "7" or opcion == "Salir" or opcion == "S":
            #si el usuario elige la opción 6, se sale del programa
            print("¡Gracias por usar la agenda! Hasta pronto.")
            break
        else:
            #si el usuario elige una opción que no está en el menú, se muestra un mensaje
            print("Opción inválida. Por favor, elige una opción del menú.")

#se llama a la función principal que contiene el bucle infinito
main()

