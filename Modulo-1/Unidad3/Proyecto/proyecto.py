"""
Ejercicio Integrador en Python
Sistema de Gestión de una Tienda de Videojuegos
Objetivo
Desarrollar un programa en Python que permita administrar el inventario y las ventas de una tienda de videojuegos utilizando:
Variables
Condicionales (if, elif, else)
Ciclos (while, for)
Funciones
Colecciones (diccionarios y listas)
Enunciado del Problema
Una tienda de videojuegos desea llevar el control de sus productos y ventas.
Cada videojuego tendrá la siguiente información:
Código
Nombre
Plataforma (PC, PlayStation, Xbox, Nintendo)
Precio
Cantidad en inventario
La información se almacenará en un diccionario con la siguiente estructura:
Python
videojuegos = {
    "VG001": {
        "nombre": "FIFA 26",
        "plataforma": "PlayStation 5",
        "precio": 250000,
        "cantidad": 10
    }
}
Menú Principal
El programa debe mostrar repetidamente el siguiente menú:
Plain text
===== TIENDA DE VIDEOJUEGOS =====
1. Agregar videojuego
2. Mostrar inventario
3. Buscar videojuego por código
4. Actualizar precio
5. Registrar venta
6. Mostrar estadísticas
7. Eliminar videojuego
8. Salir
Requisitos del Programa
1. Agregar videojuego
Crear una función que solicite los datos del videojuego y lo agregue al diccionario.
Validaciones:
No se debe permitir un código repetido.
El precio y la cantidad deben ser mayores que cero.
2. Mostrar inventario
Recorrer el diccionario e imprimir todos los videojuegos registrados.
3. Buscar videojuego por código
Solicitar un código y mostrar toda la información del videojuego si existe.
4. Actualizar precio
Permitir cambiar el precio de un videojuego existente.
5. Registrar venta
Solicitar:
Código del videojuego
Cantidad a vender
Validaciones:
El videojuego debe existir.
Debe haber suficiente inventario.
Acciones:
Restar del inventario.
Calcular el valor total de la venta.
Mostrar factura.
6. Mostrar estadísticas
Crear una función que muestre:
Total de videojuegos registrados.
Valor total del inventario.
Videojuego más costoso.
Videojuego con mayor cantidad disponible.
Promedio de precios.
7. Eliminar videojuego
Eliminar un videojuego por código.
8. Salir
Finalizar el programa.
Requisitos Técnicos
Funciones obligatorias
Debes implementar al menos las siguientes funciones:
Python
def agregar_videojuego(videojuegos):
def mostrar_inventario(videojuegos):
def buscar_videojuego(videojuegos):
def actualizar_precio(videojuegos):
def registrar_venta(videojuegos):
def mostrar_estadisticas(videojuegos):
def eliminar_videojuego(videojuegos):
def menu():
Datos Iniciales de Prueba
Python
videojuegos = {
    "VG001": {
        "nombre": "FIFA 26",
        "plataforma": "PlayStation 5",
        "precio": 250000,
        "cantidad": 10
    },
    "VG002": {
        "nombre": "Zelda: Breath of the Wild",
        "plataforma": "Nintendo Switch",
        "precio": 220000,
        "cantidad": 5
    },
    "VG003": {
        "nombre": "Forza Horizon 5",
        "plataforma": "Xbox Series X",
        "precio": 210000,
        "cantidad": 8
    }
}
Ejemplo de Venta
Plain text
Ingrese código del videojuego: VG001
Ingrese cantidad a vender: 2

Factura:
Juego: FIFA 26
Precio unitario: $250000
Cantidad: 2
Total: $500000
Retos Adicionales (Opcionales)
Si terminas antes, agrega:
Buscar videojuegos por plataforma.
Mostrar videojuegos con inventario bajo (cantidad < 3).
Aplicar descuentos del 10% en ventas mayores a $500.000.
Guardar historial de ventas en una lista.
Mostrar el videojuego más vendido.
Conceptos que Practicarás
Diccionarios anidados
Listas
Funciones con parámetros y retorno
Condicionales
Ciclos while y for
Validación de datos
Cálculos estadísticos básicos
Nivel de Dificultad
Intermedio
Tiempo Estimado
2 a 3 horas
Resultado Esperado
Al finalizar tendrás un sistema completo de consola para administrar una tienda de videojuegos, aplicando de forma práctica los principales fundamentos de Python.
"""
videojuegos = {
    "VG001": {
        "nombre": "FIFA 26",
        "plataforma": "PlayStation 5",
        "precio": 250000,
        "cantidad": 10
    },
    "VG002": {
        "nombre": "Zelda: Breath of the Wild",
        "plataforma": "Nintendo Switch",
        "precio": 220000,
        "cantidad": 5
    },
    "VG003": {
        "nombre": "Forza Horizon 5",
        "plataforma": "Xbox Series X",
        "precio": 210000,
        "cantidad": 8
    }
}


# =========================
# FUNCIONES
# =========================

def agregar_videojuego(videojuegos):

    codigo = input("Ingrese el código del videojuego: ")

    if codigo in videojuegos:
        print("El videojuego ya está registrado")
        return

    nombre = input("Ingrese el nombre del videojuego: ")
    plataforma = input("Ingrese la plataforma: ")

    precio = int(input("Ingrese el precio: "))
    cantidad = int(input("Ingrese la cantidad: "))

    if precio <= 0:
        print("El precio debe ser mayor a 0")
        return

    if cantidad <= 0:
        print("La cantidad debe ser mayor a 0")
        return

    videojuegos[codigo] = {
        "nombre": nombre,
        "plataforma": plataforma,
        "precio": precio,
        "cantidad": cantidad
    }

    print("Videojuego agregado correctamente")


def mostrar_inventario(videojuegos):

    print("\n===== INVENTARIO =====")

    for codigo, juego in videojuegos.items():

        print(f"""
Código: {codigo}
Nombre: {juego["nombre"]}
Plataforma: {juego["plataforma"]}
Precio: ${juego["precio"]}
Cantidad: {juego["cantidad"]}
""")


def buscar_videojuego(videojuegos):

    codigo = input("Ingrese el código del videojuego: ")

    if codigo in videojuegos:

        juego = videojuegos[codigo]

        print(f"""
Código: {codigo}
Nombre: {juego["nombre"]}
Plataforma: {juego["plataforma"]}
Precio: ${juego["precio"]}
Cantidad: {juego["cantidad"]}
""")
    else:
        print("El videojuego no existe")


def actualizar_precio(videojuegos):

    codigo = input("Ingrese el código del videojuego: ")

    if codigo in videojuegos:

        nuevo_precio = int(input("Ingrese el nuevo precio: "))

        if nuevo_precio <= 0:
            print("El precio debe ser mayor a 0")
            return

        videojuegos[codigo]["precio"] = nuevo_precio

        print("Precio actualizado correctamente")

    else:
        print("El videojuego no existe")


def registrar_venta(videojuegos):

    codigo = input("Ingrese el código del videojuego: ")

    if codigo not in videojuegos:
        print("El videojuego no existe")
        return

    cantidad_vender = int(input("Ingrese cantidad a vender: "))

    if cantidad_vender <= 0:
        print("Cantidad inválida")
        return

    if cantidad_vender > videojuegos[codigo]["cantidad"]:
        print("No hay suficiente inventario")
        return

    videojuegos[codigo]["cantidad"] -= cantidad_vender

    precio_unitario = videojuegos[codigo]["precio"]
    total = precio_unitario * cantidad_vender

    print("\n===== FACTURA =====")
    print(f"Juego: {videojuegos[codigo]['nombre']}")
    print(f"Precio unitario: ${precio_unitario}")
    print(f"Cantidad: {cantidad_vender}")
    print(f"Total: ${total}")


def mostrar_estadisticas(videojuegos):

    total_videojuegos = len(videojuegos)

    valor_total = 0

    juego_costoso = ""
    precio_mayor = 0

    juego_mayor_stock = ""
    mayor_cantidad = 0

    suma_precios = 0

    for codigo, juego in videojuegos.items():

        valor_total += juego["precio"] * juego["cantidad"]

        suma_precios += juego["precio"]

        # Juego más costoso
        if juego["precio"] > precio_mayor:
            precio_mayor = juego["precio"]
            juego_costoso = juego["nombre"]

        # Juego con más cantidad
        if juego["cantidad"] > mayor_cantidad:
            mayor_cantidad = juego["cantidad"]
            juego_mayor_stock = juego["nombre"]

    promedio_precios = suma_precios / total_videojuegos

    print("\n===== ESTADÍSTICAS =====")
    print(f"Total videojuegos registrados: {total_videojuegos}")
    print(f"Valor total del inventario: ${valor_total}")
    print(f"Videojuego más costoso: {juego_costoso}")
    print(f"Videojuego con mayor cantidad: {juego_mayor_stock}")
    print(f"Promedio de precios: ${promedio_precios:.2f}")


def eliminar_videojuego(videojuegos):

    codigo = input("Ingrese el código del videojuego a eliminar: ")

    if codigo in videojuegos:

        del videojuegos[codigo]

        print("Videojuego eliminado correctamente")

    else:
        print("El videojuego no existe")


def menu():

    opcion = ""

    while opcion != "8":

        print("\n========== TIENDA DE VIDEOJUEGOS ==========")
        print("1. Agregar videojuego")
        print("2. Mostrar inventario")
        print("3. Buscar videojuego por código")
        print("4. Actualizar precio")
        print("5. Registrar venta")
        print("6. Mostrar estadísticas")
        print("7. Eliminar videojuego")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_videojuego(videojuegos)

        elif opcion == "2":
            mostrar_inventario(videojuegos)

        elif opcion == "3":
            buscar_videojuego(videojuegos)

        elif opcion == "4":
            actualizar_precio(videojuegos)

        elif opcion == "5":
            registrar_venta(videojuegos)

        elif opcion == "6":
            mostrar_estadisticas(videojuegos)

        elif opcion == "7":
            eliminar_videojuego(videojuegos)

        elif opcion == "8":
            print("Saliendo del sistema...")

        else:
            print("Opción inválida")


# =========================
# INICIO DEL PROGRAMA
# =========================

menu()