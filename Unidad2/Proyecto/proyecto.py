"""
Ejercicio grupal: Sistema de gestión de hospital veterinario
Contexto

Una clínica veterinaria quiere desarrollar un sistema orientado a objetos para organizar su funcionamiento diario. El sistema debe permitir gestionar personas, mascotas, consultas, tratamientos, pagos y hospitalizaciones.

Los estudiantes deben analizar el problema, identificar las clases, construir el modelo UML y luego implementar una versión funcional en Python.

Objetivo del ejercicio

Diseñar e implementar un sistema en Python que permita modelar el funcionamiento básico de un hospital veterinario, aplicando correctamente relaciones entre clases y principios de POO.

Lo que debe incluir obligatoriamente
1. Clase abstracta

Debe existir una clase abstracta llamada Persona.

De ella deben heredar otras clases.

Atributos sugeridos:
nombre
documento
Método abstracto obligatorio:
mostrar_rol()
2. Herencia

Desde Persona deben heredar al menos estas clases:

Veterinario
Recepcionista
Cliente

Cada una debe implementar mostrar_rol() de forma diferente.

3. Asociación

Debe existir una relación de asociación entre:

Veterinario y Mascota

porque un veterinario puede atender muchas mascotas y una mascota puede ser atendida por distintos veterinarios en diferentes momentos.

Esa relación puede reflejarse en la clase Consulta, donde se conectan ambas clases.

4. Agregación

Debe existir una relación de agregación entre:

Cliente y Mascota

porque un cliente tiene mascotas, pero la mascota puede seguir existiendo aunque el cliente se elimine del sistema.

El cliente debe tener un atributo como:

mascotas = []

y un método:

agregar_mascota()
5. Composición

Debe existir una relación de composición entre:

Consulta y Tratamiento

porque una consulta crea sus tratamientos como parte de sí misma.

La idea es que el tratamiento nazca dentro de la consulta.

La clase Consulta puede tener:

lista de tratamientos
método crear_tratamiento()
6. Polimorfismo

Debe existir una clase abstracta llamada MetodoPago.

De ella deben heredar:

PagoEfectivo
PagoTarjeta
PagoTransferencia

Cada una debe implementar el método:

procesar_pago(monto)

Luego una clase Factura debe usar cualquier objeto de tipo MetodoPago para cobrar una consulta.

Clases mínimas sugeridas

Los estudiantes deben trabajar, como mínimo, con estas clases:

Persona (abstracta)
Veterinario
Recepcionista
Cliente
Mascota
Consulta
Tratamiento
Factura
MetodoPago (abstracta)
PagoEfectivo
PagoTarjeta
PagoTransferencia
Reglas del sistema
Persona

Clase abstracta.

Atributos:
nombre
documento
Método abstracto:
mostrar_rol()
Veterinario

Hereda de Persona.

Atributos:
especialidad
Métodos:
mostrar_rol()
atender_mascota()
Recepcionista

Hereda de Persona.

Métodos:
mostrar_rol()
registrar_cliente()
Cliente

Hereda de Persona.

Atributos:
telefono
lista de mascotas
Métodos:
mostrar_rol()
agregar_mascota()
mostrar_mascotas()
Mascota
Atributos:
nombre
especie
edad
peso
Métodos:
mostrar_info()
Consulta
Atributos:
mascota
veterinario
motivo
diagnostico
tratamientos
Métodos:
crear_tratamiento()
mostrar_resumen()
calcular_costo_consulta()

Aquí se evidencia:

asociación con Mascota
asociación con Veterinario
composición con Tratamiento
Tratamiento
Atributos:
nombre
costo
duracion_dias
Métodos:
mostrar_tratamiento()
MetodoPago

Clase abstracta.

Método abstracto:
procesar_pago(monto)
PagoEfectivo

Hereda de MetodoPago.

PagoTarjeta

Hereda de MetodoPago.

PagoTransferencia

Hereda de MetodoPago.

Cada una debe implementar procesar_pago() de forma distinta.

Factura
Atributos:
consulta
subtotal
impuesto
total
Métodos:
calcular_total()
pagar(metodo_pago)

Aquí se debe aplicar polimorfismo.
"""

from abc import ABC, abstractmethod

#  CLASE ABSTRACTA PERSONA

class Persona(ABC):
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    @abstractmethod
    def mostrar_rol(self):
        pass


#  HERENCIA

class Veterinario(Persona):
    def __init__(self, nombre, documento, especialidad):
        super().__init__(nombre, documento)
        self.especialidad = especialidad

    def mostrar_rol(self):
        return f"Veterinario especialista en {self.especialidad}"

    def atender_mascota(self, mascota):
        return f"Atendiendo a {mascota.nombre}"


class Recepcionista(Persona):
    def mostrar_rol(self):
        return "Recepcionista"

    def registrar_cliente(self, cliente):
        return f"Cliente {cliente.nombre} registrado"


class Cliente(Persona):
    def __init__(self, nombre, documento, telefono):
        super().__init__(nombre, documento)
        self.telefono = telefono
        self.mascotas = []  # AGREGACIÓN

    def mostrar_rol(self):
        return "Cliente"

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def mostrar_mascotas(self):
        return [mascota.nombre for mascota in self.mascotas]



# CLASE MASCOTA

class Mascota:
    def __init__(self, nombre, especie, edad, peso):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

    def mostrar_info(self):
        return f"{self.nombre} - {self.especie}, {self.edad} años, {self.peso}kg"



# TRATAMIENTO

class Tratamiento:
    def __init__(self, nombre, costo, duracion_dias):
        self.nombre = nombre
        self.costo = costo
        self.duracion_dias = duracion_dias

    def mostrar_tratamiento(self):
        return f"{self.nombre} - ${self.costo} ({self.duracion_dias} días)"



# CONSULTA 

class Consulta:
    def __init__(self, mascota, veterinario, motivo, diagnostico):
        self.mascota = mascota
        self.veterinario = veterinario
        self.motivo = motivo
        self.diagnostico = diagnostico
        self.tratamientos = []  # COMPOSICIÓN

    def crear_tratamiento(self, nombre, costo, duracion):
        tratamiento = Tratamiento(nombre, costo, duracion)
        self.tratamientos.append(tratamiento)

    def mostrar_resumen(self):
        tratamientos_info = [t.mostrar_tratamiento() for t in self.tratamientos]
        return {
            "Mascota": self.mascota.nombre,
            "Veterinario": self.veterinario.nombre,
            "Motivo": self.motivo,
            "Diagnóstico": self.diagnostico,
            "Tratamientos": tratamientos_info
        }

    def calcular_costo_consulta(self):
        return sum(t.costo for t in self.tratamientos)



#  POLIMORFISMO 

class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto):
        pass


class PagoEfectivo(MetodoPago):
    def procesar_pago(self, monto):
        return f"Pago en efectivo realizado por ${monto}"


class PagoTarjeta(MetodoPago):
    def procesar_pago(self, monto):
        return f"Pago con tarjeta aprobado por ${monto}"


class PagoTransferencia(MetodoPago):
    def procesar_pago(self, monto):
        return f"Transferencia realizada por ${monto}"



#  FACTURA

class Factura:
    def __init__(self, consulta):
        self.consulta = consulta
        self.subtotal = consulta.calcular_costo_consulta()
        self.impuesto = self.subtotal * 0.19
        self.total = 0

    def calcular_total(self):
        self.total = self.subtotal + self.impuesto
        return self.total

    def pagar(self, metodo_pago: MetodoPago):
        total = self.calcular_total()
        return metodo_pago.procesar_pago(total)



# PRUEBA DEL SISTEMA

if __name__ == "__main__":
    # Crear personas
    vet = Veterinario("Dr. Juan", "123", "Cirugía")
    cliente = Cliente("Carlos", "456", "3001234567")

    # Crear mascota
    mascota = Mascota("Firulais", "Perro", 5, 12)
    cliente.agregar_mascota(mascota)

    # Crear consulta
    consulta = Consulta(mascota, vet, "Dolor", "Infección")

    # Crear tratamientos
    consulta.crear_tratamiento("Antibiótico", 50000, 5)
    consulta.crear_tratamiento("Vacuna", 30000, 1)

    # Mostrar resumen
    print(consulta.mostrar_resumen())

    # Factura
    factura = Factura(consulta)

    # Pagar con distintos métodos (POLIMORFISMO)
    pago1 = PagoEfectivo()
    pago2 = PagoTarjeta()

    print(factura.pagar(pago1))
    print(factura.pagar(pago2))

"""
Se crea una clase abstracta Persona, de la cual heredan Veterinario, Cliente y Recepcionista, aplicando herencia.
Un Cliente tiene varias Mascotas (esto es agregación, porque pueden existir por separado).
La clase Consulta conecta a Mascota y Veterinario (asociación) y además crea sus propios Tratamientos (composición).
Para los pagos, existe la clase abstracta MetodoPago con varias formas de pago (polimorfismo), que la Factura usa sin importar cuál método se elija.
"""