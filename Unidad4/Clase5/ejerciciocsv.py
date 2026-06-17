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
def registrar_producto(productos):
    nombre = input("Ingrese el nombre del producto: ").strip().lower()
    try:
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        if precio >= 0 and cantidad >= 0:
            productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
            print("Producto registrado en memoria.")
    except ValueError:
        print("Precio y cantidad deben ser números. Producto no registrado.")

def mostrar_inventario(productos):
    if len(productos) == 0:
        print("No hay productos en el inventario.")
    
    print("\n -- Inventario --")
    for i, producto in enumerate(productos, start=1):
        print(f"{i}. Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    

def buscar_producto(productos):
    if len(productos) == 0:
        print("No hay productos en el inventario.")
        return
    
    palabra = input("Ingrese el nombre del producto a buscar: ").strip().lower()
    
    encontrados = []

    for producto in productos:
        if palabra in producto["nombre"]:
            encontrados.append(producto)

    if len(encontrados) > 0:
        print("\n -- Productos encontrados --")
        for i, producto in enumerate(encontrados, start=1):
            print(f"{i}. Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    else:
        print("No se encontraron productos con ese nombre.")

def validar_datos(productos):
    if len(productos) == 0:
        print("No hay productos en el inventario.")
        return
    errores = 0
    nombres = []
    invalidos = set()

    for producto in productos:
        nombre = producto["nombre"].strip()
        precio = producto["precio"]
        cantidad = producto["cantidad"]

        if nombre == "":
            print("Error: El nombre del producto no puede estar vacío.")
            errores += 1
            invalidos.add(nombre)
        if precio < 0:
            print(f"Error: El precio del producto '{nombre}' no puede ser negativo.")
            errores += 1
            invalidos.add(nombre)
        if cantidad < 0:
            print(f"Error: La cantidad del producto '{nombre}' no puede ser negativa.")
            errores += 1
            invalidos.add(nombre)
        else:
            nombres.append(nombre)
        
        

    if errores == 0:
        print("Todos los datos son válidos.")
        
    else:
        print(f"Se encontraron {errores} errores en los datos.")
        

    print("Productos válidos")
    for nombre in nombres:
        print(f"Producto válido: {nombre}")
    print("Productos inválidos")
    for nombre in invalidos:
        print(f"Producto inválido: {nombre}")    


def guardar_csv(productos):
    if len(productos) == 0:
        print("No hay productos en el inventario para guardar.")
        return
    with open("inventario.csv", "w") as archivo:
        archivo.write("nombre,precio,cantidad\n")
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")

def cargar_productos_iniciales():
    productos = [
        {"nombre": "mouse",
         "precio": 120000,
         "cantidad":10
         },
         {"nombre": "teclado",
         "precio": -95000,
         "cantidad":-5
         },
         {"nombre": "monitor",
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