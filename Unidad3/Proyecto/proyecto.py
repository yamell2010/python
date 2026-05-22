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