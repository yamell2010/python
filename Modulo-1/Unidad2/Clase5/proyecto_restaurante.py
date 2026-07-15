"""
Mini Proyecto: Sistema de Gestión de Restaurante (POO Avanzado)
🎯 Objetivo

Desarrollar un sistema en Python que permita gestionar un restaurante aplicando:

Composición y agregación
Clases abstractas
Relaciones bidireccionales
Bajo acoplamiento
Buenas prácticas de diseño
🧩 Descripción del problema

Se necesita modelar un sistema que permita:

Registrar clientes
Crear pedidos con múltiples platos
Asignar meseros a pedidos
Calcular cuentas y generar facturas
Aplicar diferentes tipos de pago
🏗️ Requisitos del sistema
1. 👤 Clientes
Un cliente puede tener múltiples pedidos (relación bidireccional)
2. 📦 Pedidos
Un pedido:
Pertenece a un cliente
Tiene varios platos (composición)
Tiene un estado (pendiente, servido, pagado)
Tiene un mesero asignado (agregación)
3. 🍝 Platos
Nombre
Precio
4. 👨‍🍳 Empleados (Clase abstracta)

Crear una clase abstracta:

Empleado

Métodos:

calcular_salario()

Subclases:

Mesero
Chef
5. 🧾 Factura
Asociada a un pedido
Calcula:
Total
Impuestos
Descuento opcional
6. 💳 Métodos de pago (tipo interfaz)

Crear una abstracción:

MetodoPago

Implementaciones:

Pago con tarjeta
Pago en efectivo

👉 Debe usarse polimorfismo

🔗 Relaciones clave (muy importante)
Relación	Tipo
Pedido → Plato	Composición
Restaurante → Empleados	Agregación
Pedido → Mesero	Agregación
Cliente ↔️ Pedido	Bidireccional
💻 Estructura sugerida
abc/
modelos/
    cliente.py
    pedido.py
    plato.py
    empleado.py
    factura.py
    pago.py
main.py
🚀 Funcionalidades mínimas (MVP)

✔ Crear cliente
✔ Crear pedido
✔ Agregar platos
✔ Asignar mesero
✔ Calcular total
✔ Generar factura
✔ Pagar pedido

⭐ Funcionalidades extra (para subir nota)
Validar que un pedido no esté vacío
Manejar errores (exceptions)
Aplicar descuentos
Mostrar historial de pedidos por cliente
Separar lógica en módulos
🧪 Ejemplo de uso esperado
cliente = Cliente("Ana")

pedido = Pedido(cliente)
pedido.agregar_plato("Pizza", 20)
pedido.agregar_plato("Refresco", 5)

mesero = Mesero("Carlos")
pedido.asignar_mesero(mesero)

factura = Factura(pedido)
print(factura.calcular_total())

pago = PagoTarjeta()
pago.pagar(factura)
"""