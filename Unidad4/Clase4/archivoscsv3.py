import csv 

datos = [
    ["portati", 2500000],
    ["tablet", 1500000],
    ["Smartphone", 1000000]
]

with open ("inventario.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["productos", "precio"])

    for fila in datos:
        escritor.writerow(fila)