"""
Sistema de Gestión de Biblioteca
🎯 Objetivo del reto

Diseñar la estructura de datos más adecuada para representar una biblioteca utilizando listas, diccionarios, conjuntos y tuplas.

El reto no consiste únicamente en almacenar datos, sino en pensar como un arquitecto de software, seleccionando la estructura correcta para cada tipo de información.

📚 Contexto

Una biblioteca necesita almacenar información sobre:

Libros
Autores
Usuarios
Préstamos
Fechas
Categorías

Tu equipo debe diseñar un modelo de datos que permita representar toda esta información de forma organizada y sin redundancias.

📝 Requerimientos del sistema
1. Libros

Cada libro debe almacenar:

ISBN
Título
Año de publicación
Lista de autores
Categorías
Número total de copias
Número de copias disponibles
2. Autores

Cada autor debe tener:

Identificación única
Nombre
Nacionalidad
Año de nacimiento
3. Usuarios

Cada usuario debe almacenar:

ID
Nombre completo
Correo electrónico
Teléfono
4. Préstamos

Cada préstamo debe registrar:

ID del préstamo
Usuario
ISBN del libro
Fecha de préstamo
Fecha de devolución
Estado (activo, devuelto, atrasado)
5. Fechas

Las fechas deben almacenarse usando una estructura apropiada.

6. Categorías

No deben existir categorías repetidas.

🎯 Parte 1 — Diseñar el esquema de datos

Construyan una estructura principal llamada biblioteca que contenga toda la información.

Sugerencia:
biblioteca = {
    "autores": {},
    "libros": {},
    "usuarios": {},
    "prestamos": {}
}
🎯 Parte 2 — Cargar datos de ejemplo

Agregar al menos:

3 autores
5 libros
4 usuarios
3 préstamos
🎯 Parte 3 — Consultas a resolver

El programa debe mostrar:

Todos los libros disponibles.
Todos los libros de un autor específico.
Todos los préstamos activos.
Usuarios con préstamos atrasados.
Categorías existentes.
Libro más prestado.
Cantidad total de libros.
Cantidad total de préstamos activos.
🎯 Parte 4 — Justificación técnica

El equipo debe explicar:

¿Por qué usaron diccionarios para ciertas entidades?
¿Por qué las categorías son conjuntos?
¿Por qué las fechas pueden representarse como tuplas?
¿Qué ventajas tiene evitar redundancia?
🎯 Parte 5 — Refactorización

Analicen el siguiente diseño deficiente:

biblioteca = [
    ["978001", "Python Básico", "Juan Pérez", "Programación"],
    ["978002", "Python Avanzado", "Juan Pérez", "Programación"],
    ["978003", "Bases de Datos", "Ana Gómez", "Tecnología"]
]
Preguntas
¿Qué redundancias existen?
¿Qué problemas tendría este diseño?
¿Cómo lo reestructurarían?
🏅 Bonus

Agregar:

Historial de préstamos por usuario.
Búsqueda por categoría.
Ranking de usuarios con más préstamos."""

biblioteca = {
    "autores": {},
    "libros": {},
    "usuarios": {},
    "prestamos": {}
}

biblioteca["autores"] = {
    1: {
        "nombre": "Gabriel García Márquez",
        "nacionalidad": "Colombiana",
        "nacimiento": 1927
    },
    2: {
        "nombre": "J.K. Rowling",
        "nacionalidad": "Británica",
        "nacimiento": 1965
    },
    3: {
        "nombre": "George Orwell",
        "nacionalidad": "Británica",
        "nacimiento": 1903
    }
}

biblioteca["libros"] = {
    "9780307474728": {
        "titulo": "Cien años de soledad",
        "anio": 1967,
        "autores": [1],
        "categorias": {"Novela", "Realismo mágico"},
        "copias_totales": 5,
        "copias_disponibles": 3,
        "veces_prestado": 2
    },
    "9788478884452": {
        "titulo": "Harry Potter y la piedra filosofal",
        "anio": 1997,
        "autores": [2],
        "categorias": {"Fantasía", "Aventura"},
        "copias_totales": 8,
        "copias_disponibles": 6,
        "veces_prestado": 2
    },
    "9780451524935": {
        "titulo": "1984",
        "anio": 1949,
        "autores": [3],
        "categorias": {"Distopía", "Política"},
        "copias_totales": 4,
        "copias_disponibles": 3,
        "veces_prestado": 1
    },
    "9780307389732": {
        "titulo": "Rebelión en la granja",
        "anio": 1945,
        "autores": [3],
        "categorias": {"Sátira", "Política"},
        "copias_totales": 3,
        "copias_disponibles": 3,
        "veces_prestado": 0
    },
    "9788498382662": {
        "titulo": "Harry Potter y la cámara secreta",
        "anio": 1998,
        "autores": [2],
        "categorias": {"Fantasía", "Aventura"},
        "copias_totales": 6,
        "copias_disponibles": 5,
        "veces_prestado": 1
    }
}

biblioteca["usuarios"] = {
    101: {
        "nombre": "Carlos Fadul",
        "email": "carlos@example.com",
        "telefono": "3001111111"
    },
    102: {
        "nombre": "Ana Gómez",
        "email": "ana@example.com",
        "telefono": "3002222222"
    },
    103: {
        "nombre": "Luis Pérez",
        "email": "luis@example.com",
        "telefono": "3003333333"
    },
    104: {
        "nombre": "María Torres",
        "email": "maria@example.com",
        "telefono": "3004444444"
    }
}

biblioteca["prestamos"] = {
    1: {
        "usuario_id": 101,
        "isbn": "9780307474728",
        "fecha_prestamo": (2026, 4, 1),
        "fecha_devolucion": (2026, 4, 15),
        "estado": "devuelto"
    },
    2: {
        "usuario_id": 102,
        "isbn": "9788478884452",
        "fecha_prestamo": (2026, 5, 1),
        "fecha_devolucion": (2026, 5, 15),
        "estado": "activo"
    },
    3: {
        "usuario_id": 103,
        "isbn": "9780451524935",
        "fecha_prestamo": (2026, 4, 20),
        "fecha_devolucion": (2026, 5, 5),
        "estado": "atrasado"
    }
}

print("=" * 60)
print("LIBROS DISPONIBLES")
print("=" * 60)

for isbn, libro in biblioteca["libros"].items():
    if libro["copias_disponibles"] > 0:
        print(f"{libro['titulo']} - Disponibles: {libro['copias_disponibles']}")

print("\n" + "=" * 60)
print("LIBROS DE GEORGE ORWELL")
print("=" * 60)

autor_id = 3

for isbn, libro in biblioteca["libros"].items():
    if autor_id in libro["autores"]:
        print(libro["titulo"])

print("\n" + "=" * 60)
print("PRÉSTAMOS ACTIVOS")
print("=" * 60)

for prestamo_id, prestamo in biblioteca["prestamos"].items():
    if prestamo["estado"] == "activo":
        usuario = biblioteca["usuarios"][prestamo["usuario_id"]]["nombre"]
        libro = biblioteca["libros"][prestamo["isbn"]]["titulo"]
        print(f"Préstamo {prestamo_id}: {usuario} -> {libro}")

print("\n" + "=" * 60)
print("USUARIOS CON PRÉSTAMOS ATRASADOS")
print("=" * 60)

for prestamo in biblioteca["prestamos"].values():
    if prestamo["estado"] == "atrasado":
        usuario = biblioteca["usuarios"][prestamo["usuario_id"]]["nombre"]
        print(usuario)

print("\n" + "=" * 60)
print("CATEGORÍAS EXISTENTES")
print("=" * 60)

categorias = set()

for libro in biblioteca["libros"].values():
    categorias.update(libro["categorias"])

for categoria in sorted(categorias):
    print(categoria)

print("\n" + "=" * 60)
print("LIBRO MÁS PRESTADO")
print("=" * 60)

isbn_mas_prestado = max(
    biblioteca["libros"],
    key=lambda isbn: biblioteca["libros"][isbn]["veces_prestado"]
)

print(biblioteca["libros"][isbn_mas_prestado]["titulo"])

print("\n" + "=" * 60)
print("TOTAL DE COPIAS EN LA BIBLIOTECA")
print("=" * 60)

total_copias = 0

for libro in biblioteca["libros"].values():
    total_copias += libro["copias_totales"]

print(total_copias)

print("\n" + "=" * 60)
print("TOTAL DE PRÉSTAMOS ACTIVOS")
print("=" * 60)

activos = 0

for prestamo in biblioteca["prestamos"].values():
    if prestamo["estado"] == "activo":
        activos += 1

print(activos)

print("\n" + "=" * 60)
print("HISTORIAL DE PRÉSTAMOS POR USUARIO")
print("=" * 60)

for usuario_id, usuario in biblioteca["usuarios"].items():
    print(f"\n{usuario['nombre']}:")
    tiene_prestamos = False

    for prestamo in biblioteca["prestamos"].values():
        if prestamo["usuario_id"] == usuario_id:
            titulo = biblioteca["libros"][prestamo["isbn"]]["titulo"]
            print(f" - {titulo} ({prestamo['estado']})")
            tiene_prestamos = True

    if not tiene_prestamos:
        print(" - Sin préstamos")