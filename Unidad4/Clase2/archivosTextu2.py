"""
archivo = open("datos1.txt","w")
archivo.write("saludos para todos")
archivo.close()
"""

with open("datos2.txt","w", encoding="utf-8") as archivo:
    archivo.write("saludos para todos")

with open("datos2.txt", "r", encoding="utf-8") as archivo:
    linea = archivo.readline()
    print(linea)

with open("datos2.txt","a", encoding="utf-8") as archivo:
    archivo.write("\nque onda pues pelaitos")

with open("datos2.txt", "r", encoding="utf-8") as archivo:
    linea2 = archivo.readlines()
    print(linea2)
    for x in linea2:
        x = x.rstrip("\n")
        print(x)