import csv

with open(r"C:\Users\57301\Documents\PythonDevSenior\Modulo1\Unidad4\Clase4\productos.csv", "r", encoding="utf-8") as archivo:
    lector_csv = csv.reader(archivo)

    next(lector_csv) # salta la primera fila(encabezado)

    for fila in lector_csv:
        nombre = fila [0]
        precio = fila [1]
        cantidad = fila [2]

        print (nombre, precio, cantidad)
