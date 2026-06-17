# 🎮 Sistema de Gestión de Tienda de Videojuegos

## Proyecto Final - Módulo 3

**Docente:** Carlos Fadul  
**Estudiante:** Carolina Gil  
**Fecha:** 14/05/2026  
**Lenguaje:** Python  

---

## 1. Objetivo General

Desarrollar un programa completo en Python que permita administrar el inventario y las ventas de una tienda de videojuegos.

Este proyecto integrador aplica los conceptos fundamentales aprendidos en el módulo 3:

- Variables y tipos de datos
- Condicionales
- Ciclos
- Funciones
- Diccionarios y listas
- Validación de datos
- Cálculos básicos

---

## 2. Contexto del Proyecto

Una tienda de videojuegos necesita un sistema para gestionar su inventario y controlar las ventas diarias.

Actualmente, la gestión se realiza de forma manual, lo que puede generar:

- Errores en el inventario
- Pérdida de tiempo
- Dificultades para obtener estadísticas
- Problemas en el control de ventas

---

## 3. Problema a Resolver

El sistema debe permitir:

- Controlar el inventario de videojuegos
- Registrar ventas con validación de stock
- Actualizar automáticamente las cantidades disponibles
- Generar reportes y estadísticas
- Mantener la integridad de los datos

---

## 4. Estructura de Datos

Cada videojuego será representado mediante un diccionario anidado.

Ejemplo:

```python
videojuegos = {
    "VG001": {
        "nombre": "FIFA 26",
        "plataforma": "PlayStation 5",
        "precio": 250000,
        "cantidad": 10
    }
}

## 5. Menú Principal

El programa funcionará mediante un menú interactivo en consola:

```text
===== TIENDA DE VIDEOJUEGOS =====
1. Agregar videojuego
2. Mostrar inventario
3. Buscar videojuego por código
4. Actualizar precio
5. Registrar venta
6. Mostrar estadísticas
7. Eliminar videojuego
8. Salir

Seleccione una opción (1-8):
```

---

## 6. Funcionalidades del Sistema

### 6.1 Agregar Videojuego

Permite registrar un nuevo videojuego en el inventario.

**Datos solicitados:**

- Código
- Nombre
- Plataforma
- Precio
- Cantidad inicial

**Validaciones:**

- El código no debe existir previamente.
- El precio debe ser mayor que 0.
- La cantidad debe ser mayor o igual a 0.
- El nombre y la plataforma no pueden estar vacíos.

---

### 6.2 Mostrar Inventario

Muestra todos los videojuegos registrados en formato de tabla.

Si no hay videojuegos registrados, el sistema debe mostrar un mensaje indicando que el inventario está vacío.

---

### 6.3 Buscar Videojuego por Código

Permite consultar la información de un videojuego usando su código.

**Resultado esperado:**

- Si el código existe, muestra toda la información del videojuego.
- Si el código no existe, muestra un mensaje indicando que no fue encontrado.

---

### 6.4 Actualizar Precio

Permite modificar el precio de un videojuego existente.

**Validaciones:**

- El videojuego debe existir.
- El nuevo precio debe ser mayor que 0.

---

### 6.5 Registrar Venta

Permite registrar la venta de un videojuego y actualizar el inventario.

**Validaciones:**

- El videojuego debe existir.
- La cantidad a vender debe ser mayor que 0.
- Debe existir suficiente cantidad disponible en inventario.

**Acciones realizadas:**

- Calcula el total de la venta.
- Resta la cantidad vendida del inventario.
- Genera una factura en consola.

Ejemplo de factura:

```text
==================
FACTURA
==================
Juego: FIFA 26
Precio unitario: $250,000
Cantidad: 2
Total: $500,000
==================
¡Venta registrada exitosamente!
```

---

### 6.6 Mostrar Estadísticas

Genera un reporte general del inventario.

**Métricas calculadas:**

- Total de videojuegos registrados.
- Valor total del inventario.
- Videojuego más costoso.
- Videojuego con mayor cantidad disponible.
- Promedio de precios.

---

### 6.7 Eliminar Videojuego

Permite eliminar un videojuego del inventario.

**Validación:**

- El código ingresado debe existir en el inventario.

---

### 6.8 Salir

Finaliza la ejecución del programa.

---

## 7. Funciones Principales

El proyecto debe implementar como mínimo las siguientes funciones:

```python
def agregar_videojuego(videojuegos: dict) -> None:
    pass

def mostrar_inventario(videojuegos: dict) -> None:
    pass

def buscar_videojuego(videojuegos: dict) -> None:
    pass

def actualizar_precio(videojuegos: dict) -> None:
    pass

def registrar_venta(videojuegos: dict) -> None:
    pass

def mostrar_estadisticas(videojuegos: dict) -> None:
    pass

def eliminar_videojuego(videojuegos: dict) -> None:
    pass

def menu() -> None:
    pass
```

---

## 8. Datos Iniciales de Prueba

El programa debe iniciar con el siguiente diccionario:

```python
videojuegos_iniciales = {
    "VG001": {
        "nombre": "FIFA 26",
        "plataforma": "PlayStation 5",
        "precio": 250000,
        "cantidad": 10
    },
    "VG002": {
        "nombre": "Zelda: Breath of the Wild",
        "plataforma": "Nintendo Switch",
        "precio": 220000,
        "cantidad": 5
    },
    "VG003": {
        "nombre": "Forza Horizon 5",
        "plataforma": "Xbox Series X",
        "precio": 210000,
        "cantidad": 8
    }
}
```

---

## 9. Ejemplos de Ejecución

### Ejemplo 1: Agregar Videojuego

```text
Código: VG004
Nombre: God of War Ragnarök
Plataforma: PlayStation 5
Precio: 280000
Cantidad: 12
```

Resultado esperado:

```text
Videojuego agregado exitosamente.
```

---

### Ejemplo 2: Registrar Venta

```text
Código del videojuego: VG001
Cantidad a vender: 2
```

Resultado esperado:

```text
Juego: FIFA 26
Precio unitario: $250,000
Cantidad: 2
Total: $500,000
¡Venta registrada exitosamente!
```

---

### Ejemplo 3: Mostrar Estadísticas

```text
Estadísticas del Inventario
---------------------------
Total de videojuegos: 3
Valor total del inventario: $6,950,000
Videojuego más costoso: FIFA 26 ($250,000)
Mayor cantidad disponible: FIFA 26 (10 unidades)
Promedio de precios: $230,000
```

---

## 10. Retos Adicionales Opcionales

Si se completa el proyecto básico, se pueden implementar mejoras como:

### Búsqueda Avanzada

- Buscar videojuegos por plataforma.
- Buscar videojuegos por rango de precios.

### Alertas de Inventario

- Mostrar videojuegos con inventario bajo.
- Alertar cuando la cantidad sea menor a 3 unidades.

### Descuentos

- Aplicar descuento del 10% en compras mayores a $500,000.
- Implementar promociones como 3x2.

### Historial de Ventas

- Guardar cada venta en una lista de diccionarios.
- Mostrar historial completo.
- Calcular el videojuego más vendido.

### Exportación de Datos

- Guardar inventario en archivo JSON.
- Generar reportes en archivo de texto.

---

## 11. Conceptos Practicados

Con este proyecto se practican los siguientes conceptos:

### Estructuras de Datos

- Diccionarios anidados.
- Listas.
- Manipulación de colecciones.

### Funciones

- Funciones con parámetros.
- Funciones con retorno.
- Modularidad.
- Separación de responsabilidades.

### Control de Flujo

- Condicionales `if`, `elif`, `else`.
- Ciclos `while`.
- Ciclos `for`.

### Validaciones

- Validación de entradas del usuario.
- Manejo de errores.
- Casos especiales.

### Lógica de Negocio

- Cálculo de totales.
- Cálculo de promedios.
- Actualización de inventario.
- Registro de ventas.

---

## 12. Criterios de Evaluación

| Criterio | Porcentaje |
|---|---:|
| Funcionalidad | 60% |
| Código limpio y organizado | 25% |
| Validaciones | 10% |
| Creatividad | 5% |

---

## 13. Entrega

El proyecto debe entregarse en un archivo llamado:

```text
PROYECTOFINALmodulo3.py
```

También debe incluir una breve documentación con las decisiones tomadas durante el desarrollo.

---

## 14. Recomendaciones de Desarrollo

Para desarrollar el proyecto correctamente:

1. Leer todo el enunciado antes de empezar.
2. Diseñar primero las funciones principales.
3. Implementar una función a la vez.
4. Probar cada funcionalidad individualmente.
5. Validar entradas incorrectas.
6. Revisar los cálculos matemáticos.
7. Limpiar el código antes de entregar.
8. Agregar comentarios claros y útiles.

---

## 15. Conclusión

Este proyecto permite demostrar el dominio de los fundamentos de Python mediante la creación de un sistema funcional de consola para una tienda de videojuegos.

El objetivo principal es aplicar la lógica de programación, el uso de estructuras de datos, funciones, ciclos, condicionales y validaciones en un caso práctico cercano a una situación real.