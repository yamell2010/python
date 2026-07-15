import csv

with open("malo.csv", "r", encoding="utf-8") as archivo:

    lector = csv.DictReader(archivo)

    for fila in lector:
        try:
            nombre = fila["nombre"]
            precio = fila["precio"]
            cantidad = fila["cantidad"]
            if precio < 0 or cantidad < 0:
                print("valores negativos invalidos")
                continue
            print(nombre, precio, cantidad)
        except (ValueError, TypeError):
            print("Error de formato de fila: ", fila)
        except KeyError:
            print("falta una columna en la fila", fila)