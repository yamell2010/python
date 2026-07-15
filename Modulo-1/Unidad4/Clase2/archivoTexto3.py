def guardar_texto(nombre_archivo, texto):
    with open(nombre_archivo, "w") as archivo:
        archivo.write(texto)


def cargar_texto(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            texto = archivo.read()
        return texto
    except FileNotFoundError:
        print(f"el carchivo {nombre_archivo} no existe")
        return None
    
def guardar_tareas(tareas):
    with open("tareas5.txt", "w", encoding="utf-8") as archivo:
        for tarea in tareas:
            archivo.write(tarea + "\n")

def cargar_tareas():
    try:
        with open("tareas5.txt","r", encoding="utf-8") as archivo:
            return [linea.strip() for linea in archivo.readlines]
    except FileNotFoundError:
        print("el archivo de tareas no existe.")
        return []

guardar_texto("saludo2.txt", "el hijo de rana es rana")
texto_cargado = cargar_texto("saludo3.txt")
print(texto_cargado)
tareas = ["hacer la cama", "lavar los platos", "sacar basura"]

guardar_tareas(tareas)
print(cargar_tareas())