# r para leer
# w para escribir
# a para agregar
# r+ para leer y escribir
# x para crear un nuevo archivo, si el archvo ya existe, se genera un error

"""
archivo = open("saludos.txt", "w")
archivo.write("Hola mundo")
archivo.close()
"""
"""
archivo = open("tareas.txt", "r")
linea = archivo.readline()
print(linea)
archivo.close()´
"""
"""
archivo = open("tareas.txt", "r")
lineas = archivo.readlines()
print(lineas)
archivo.close()
for linea in lineas:
    print(linea)
"""
