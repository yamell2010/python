"""
Crear una aplicación que permita:

Registrar usuarios.
Validar información.
Guardar en archivo.
Capturar errores.
Mostrar mensajes amigables.

Carlos,25
Ana,30
Pedro,22
"""
def registrar_usuarios():
    try:
        nombre = input("Ingrese nombre de usuario")

        if nombre == "":
            print("el nombre no puede estar vacio")
            return
        edad = int(input("ingrese la edad del usuario"))

        if edad < 0:
            print("La edad no puede ser negativa")
            return
        with open(ARCHIVO, "a", encoding="utf-8")as archivo:
            archivo.write(f"{nombre},{edad}\n")
        print("Usuario registrado exitosamente")
    
    except ValueError:
        print("la edad debe de ser numerica")
    
    except PermissionError:
        print("No se tienen permisos para escribir en el archivo")
    
    except Exception as error:
        print("Ocurrio un error inesperado: {error}")
    


def mostrar_usuarios():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            if not lineas:
                print("No hay usuarios registrados")
                return
            
            print("\n USUARIOS REGISTRADOS:")
            for linea in lineas:
                nombre, edad = linea.strip().split(",")
                print(f"Nombre: {nombre}, Edad: {edad}")
    except FileNotFoundError:
        print("No se encontro el archivo de usuarios")
    
    except PermissionError:
        print("No se tiene permiso para leer")
    
    except Exception as error:
        print(f"ocurrio un error inesperado: {error}")

ARCHIVO = "usuario.txt"

def menu():
    opcion = ""
    while opcion != "3":
        
        print("\n ====USUARIOS====")
        print("1. Registrar usuario")
        print("2. Mostrar Usuarios")
        print("3. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            registrar_usuarios()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            print("Programa finalizado")
        else:
            print("Opcion no valida. Intente de nuevo")

menu()

"""
Modificar el programa para:

Buscar usuarios.
Evitar usuarios duplicados.
Validar un archivo al momento de leerlo y en caso de errores mortralos
Crear archivo de errores. Meter los datos buenos en un archivo y los malos en otro
Registrar fecha y hora de creación.
"""