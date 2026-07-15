# Relacion de asociacion
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente

c1 = Cliente("Pedro")
p1 = Pedido(c1)

# Realacion de agregacion (relacion debil)

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
    
class Restaurante:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

e = Empleado("Roberto")
r = Restaurante()
r.agregar_empleado(e)

# Relacion de composicion (relacion fuerte)

class Plato:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Pedido:
    def __init__(self):
        self.platos = []

    def agregar_plato(self, nombre, precio):
        plato = Plato(nombre, precio)
        self.platos.append(plato)

pedido = Pedido()
pedido.agregar_plato("Sancocho", 30000)
pedido.agregar_plato("mojarra frita", 40000)


# ejemplo con clases abstractas

from abc import ABC, abstractmethod

# abc ---> es la que premite crear las clases abstractas
# astractmethod ---> es la que me dice que estoy obligado a implementarlas en las clases hijas

class Empleado(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
    
    @abstractmethod
    def calcular_salario(self):
        pass

class Mesero(Empleado):
    def calcular_salario(self):
        return 1000

class Chef(Empleado):
    def calcular_salario(self):
        return 2000
