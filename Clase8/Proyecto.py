"""
Ejercicio práctico (2 horas)
Sistema de Gestión Básica de Estudiantes
Contexto

Una universidad quiere desarrollar un pequeño programa en Python que permita registrar estudiantes y evaluar su estado académico de forma simple desde la terminal.

Tu tarea será desarrollar un script en Python estructurado con funciones que permita ingresar información de estudiantes, calcular su promedio y mostrar su estado académico.

Requisitos del programa

El programa debe permitir:

1️⃣ Registrar estudiantes
2️⃣ Calcular el promedio de tres notas
3️⃣ Determinar el estado del estudiante
4️⃣ Permitir registrar varios estudiantes usando un menú
5️⃣ Mostrar un resumen final

Reglas del sistema

Para cada estudiante se debe ingresar:

Nombre

Edad

Nota 1

Nota 2

Nota 3

El programa debe calcular:

promedio = (nota1 + nota2 + nota3) / 3

Y determinar el estado académico:

Promedio	Estado
>= 4.0	Aprobado
>= 3.0 y < 4.0	En recuperación
< 3.0	Reprobado
Estructura obligatoria del programa

El programa debe tener al menos estas funciones:

1️⃣ Función para registrar estudiante
def registrar_estudiante():

Debe pedir:

nombre

edad

3 notas

Debe retornar los datos.

2️⃣ Función para calcular promedio
def calcular_promedio(n1, n2, n3):

Debe retornar el promedio.

3️⃣ Función para determinar estado
def evaluar_estado(promedio):

Debe retornar:

"Aprobado"

"En recuperación"

"Reprobado"

4️⃣ Menú principal con bucle

El programa debe mostrar un menú como este:

1. Registrar estudiante
2. Salir

Debe usar un while para permitir registrar varios estudiantes.

Ejemplo de salida esperada
===== SISTEMA DE ESTUDIANTES =====

Ingrese el nombre del estudiante: Ana
Ingrese la edad: 20
Ingrese nota 1: 4.5
Ingrese nota 2: 3.8
Ingrese nota 3: 4.2

Promedio del estudiante: 4.17
Estado académico: Aprobado
Validaciones mínimas

El programa debe validar:

Que las notas estén entre 0 y 5

Que la edad sea mayor que 0

Si los datos no son válidos, debe pedirlos nuevamente.

Parte final (obligatoria)

Al terminar el programa debe mostrar:

Total de estudiantes registrados: X
Promedio general del grupo: X
"""

menu = """
===== SISTEMA DE ESTUDIANTES =====
1. Registrar estudiante
2. Mostrar todos los estudiantes
3. Salir
"""
"""
print(menu)
estudiantes = []
estudiante = {}
opcion = 0
while opcion != 3:
    opcion = int(input("Seleccione una opcion: "))
    if opcion == 1:
        estudiante["nombre"] = input("ingrese su nombre: ")
        estudiante["edad"] = int(input("digite su edad: "))
        estudiante["nota1"] = float(input("digite la primera nota: "))
        estudiante["nota2"] = float(input("digite la segunda nota: "))
        estudiante["nota3"] = float(input("digite la tercera nota: "))
        estudiante["promedio"] = (estudiante["nota1"]+ estudiante["nota2"]+ estudiante["nota3"])/3
        if estudiante["promedio"] < 3.0:
            estudiante["estado"] = "reprobado"
        elif estudiante["promedio"] >= 3.0 and estudiante["promedio"] < 4.0:
            estudiante["estado"] = "recuperacion"
        elif estudiante["promedio"] > 4.0:
            estudiante["estado"] = "Aprobado" 
        print(f"Nombe: {estudiante["nombre"]}")
        print(f"Edad: {estudiante["edad"]}")
        print(f"Promedio: {estudiante["promedio"]}")
        print(f"Estado: {estudiante["estado"]}")
        estudiantes.append(estudiante)
    elif opcion == 2:
        for x in estudiantes:
            print(estudiante["nombre"])
            print(estudiante["edad"])
            print(estudiante["promedio"])
            print(estudiante["estado"])
    elif opcion == 3:
        print ("Hasta pronto")
        break
    else:
        print("Seleccione una opcion valida")
"""
print(menu)
estudiantes = []
estudiante = {}
opcion = 0
while opcion != 3:
    opcion = int(input("Seleccione una opcion: "))
    if opcion == 1:
        nombre = input("ingrese su nombre: ")
        edad = int(input("digite su edad: "))
        nota1 = float(input("digite la primera nota: "))
        nota2 = float(input("digite la segunda nota: "))
        nota3 = float(input("digite la tercera nota: "))
        promedio = (nota1 + nota2 + nota3)/3
        if promedio < 3.0:
            estado = "reprobado"
        elif promedio >= 3.0 and promedio < 4.0:
            estado = "recuperacion"
        elif promedio >= 4.0:
            estado = "Aprobado" 
        print(f"Nombre: {nombre}")
        print(f"Edad: {edad}")
        print(f"Promedio: {promedio}")
        print(f"Estado: {estado}")
        estudiantes.append({
            "nombre" : nombre,
            "edad" : edad,
            "nota1" : nota1,
            "nota2" : nota2,
            "nota3" : nota3,
            "promedio" : promedio,
            "estado" : estado
        })
    elif opcion == 2:
        for x in estudiantes:
            print("Nombre:", x["nombre"])
            print("Edad:", x["edad"])
            print("Promedio:", x["promedio"])
            print("Estado:", x["estado"])
            print("------")

    elif opcion == 3:
        print ("Hasta pronto")
        break
    else:
        print("Seleccione una opcion valida")