from datetime import datetime

ARCHIVO = "usuarios.txt"


def usuario_existe(nombre_buscar):
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")

                if len(datos) >= 1:
                    nombre = datos[0]

                    if nombre.lower() == nombre_buscar.lower():
                        return True

        return False

    except FileNotFoundError:
        return False


def registrar_usuario():
    try:
        nombre = input("Ingrese el nombre del usuario: ").strip()

        if nombre == "":
            print("El nombre no puede estar vacío.")
            return

        if usuario_existe(nombre):
            print("El usuario ya existe.")
            return

        edad = int(input("Ingrese la edad del usuario: "))

        if edad < 0:
            print("La edad no puede ser negativa.")
            return

        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(ARCHIVO, "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre},{edad},{fecha_hora}\n")

        print("Usuario registrado exitosamente.")

    except ValueError:
        print("La edad debe ser numérica.")

    except PermissionError:
        print("No se tienen permisos para escribir en el archivo.")

    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")


def mostrar_usuarios():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:

            lineas = archivo.readlines()

            if not lineas:
                print("No hay usuarios registrados.")
                return

            print("\nUsuarios registrados:")

            for linea in lineas:

                datos = linea.strip().split(",")

                if len(datos) == 3:
                    nombre, edad, fecha = datos

                    print(
                        f"Nombre: {nombre}, Edad: {edad}, Fecha registro: {fecha}"
                    )

    except FileNotFoundError:
        print("No se encontró el archivo de usuarios.")

    except PermissionError:
        print("No se tienen permisos para leer el archivo.")

    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")


def buscar_usuario():
    try:
        nombre_buscar = input("Ingrese el nombre a buscar: ")

        with open(ARCHIVO, "r", encoding="utf-8") as archivo:

            encontrado = False

            for linea in archivo:

                datos = linea.strip().split(",")

                if len(datos) == 3:

                    nombre, edad, fecha = datos

                    if nombre.lower() == nombre_buscar.lower():

                        print("\nUsuario encontrado:")
                        print(f"Nombre: {nombre}")
                        print(f"Edad: {edad}")
                        print(f"Fecha registro: {fecha}")

                        encontrado = True
                        break

            if not encontrado:
                print("Usuario no encontrado.")

    except FileNotFoundError:
        print("No existe el archivo de usuarios.")

    except Exception as error:
        print(f"Ocurrió un error: {error}")


def validar_archivo():
    try:

        nombre_archivo = input("Ingrese el archivo a validar: ")

        with open(nombre_archivo, "r", encoding="utf-8") as archivo:

            errores = 0

            for numero, linea in enumerate(archivo, start=1):

                datos = linea.strip().split(",")

                if len(datos) != 3:
                    print(f"Línea {numero}: cantidad incorrecta de campos.")
                    errores += 1
                    continue

                nombre, edad, fecha = datos

                if nombre == "":
                    print(f"Línea {numero}: nombre vacío.")
                    errores += 1

                if not edad.isdigit():
                    print(f"Línea {numero}: edad inválida.")
                    errores += 1

            if errores == 0:
                print("Archivo válido.")
            else:
                print(f"\nSe encontraron {errores} errores.")

    except FileNotFoundError:
        print("Archivo no encontrado.")

    except Exception as error:
        print(f"Ocurrió un error: {error}")


def separar_registros():
    try:

        archivo_origen = input("Ingrese el archivo a procesar: ")

        with open(archivo_origen, "r", encoding="utf-8") as origen, \
             open("usuarios_validos.txt", "w", encoding="utf-8") as validos, \
             open("usuarios_error.txt", "w", encoding="utf-8") as errores:

            for linea in origen:

                datos = linea.strip().split(",")

                if len(datos) != 3:
                    errores.write(linea)
                    continue

                nombre, edad, fecha = datos

                if nombre == "" or not edad.isdigit():
                    errores.write(linea)
                else:
                    validos.write(linea)

        print("Archivos generados correctamente.")
        print("usuarios_validos.txt")
        print("usuarios_error.txt")

    except FileNotFoundError:
        print("Archivo no encontrado.")

    except Exception as error:
        print(f"Ocurrió un error: {error}")


def menu():

    opcion = ""

    while opcion != "6":

        print("\n===== USUARIOS =====")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Buscar usuario")
        print("4. Validar archivo")
        print("5. Generar archivo de errores")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()

        elif opcion == "2":
            mostrar_usuarios()

        elif opcion == "3":
            buscar_usuario()

        elif opcion == "4":
            validar_archivo()

        elif opcion == "5":
            separar_registros()

        elif opcion == "6":
            print("Programa finalizado.")

        else:
            print("Opción no válida. Intente nuevamente.")


menu()