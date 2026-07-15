"""
Crear un sistema que permita:

1. Registrar productos.
2. Mostrar inventario.
3. Buscar productos.
4. Validar datos.
5. Guardar información en CSV.
6. Terminar el programa.

La estructura sería
nombre,precio,cantidad
Mouse,120000,10
Teclado,95000,5
Monitor,250000,3
"""
def registrar_produtos(productos):
    nombre = input("Ingrese el nombre del producto: ").strip().lower()
    try:
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        if precio >= 0 and cantidad >= 0:
            productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
            print("Producto registrado en memoria.")
    except ValueError:
        print("Precio y cantidad deben ser números. Producto no registrado.")
def cargar_productos_iniciales():
    productos = [
        {"nombre": "Mouse",
         "precio": 120000,
         "cantidad": 10
         },
         {"nombre": "teclado",
          "precio": 95000,
          "cantidad":5
         },
         {"nombre": "Monitor",
          "precio": 250000,
          "cantidad":3
          }
    ]
    return productos

def mostrar_menu():
    print("1. Registrar productos")
    print("2. Mostrar inventario")
    print("3. Buscar productos")
    print("4. Validar datos")
    print("5. Guardar información en CSV")
    print("6. Terminar el programa")

def ejecutar_programa():
    productos = cargar_productos_iniciales()
    opcion = 0
    while opcion != 6:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            registrar_producto(productos)
        elif opcion == 2:
            mostrar_inventario(productos)
        elif opcion == 3:
            buscar_producto(productos)
        elif opcion == 4:
            validar_datos(productos)
        elif opcion == 5:
            guardar_csv(productos)
        elif opcion == 6:
            print("Programa terminado.")
        else:
            print("Opción no válida. Intente nuevamente.")

ejecutar_programa()