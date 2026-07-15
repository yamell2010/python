from abc import ABC, abstractmethod

class Trabajable(ABC):

    @abstractmethod
    def trabajar(self):
        pass

class Empleado(ABC):

    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

        @abstractmethod
        def calcular_salario(self):
            pass

class Gerente(Empleado, Trabajable):

    def __init__(self, nombre, salario_base, bono):
        super().__init__(nombre, salario_base)
        self.bono = bono

    def calcular_salario(self):
        return self.salario_base + self.bono
    
    def trabajar(self):
        print(f"{self.nombre} esta tallando al equipo")

class Desarrollador(Empleado, Trabajable):

    def __init__(self, nombre, salario_base, lenguaje):
        super().__init__(nombre, salario_base)
        self.lenguaje = lenguaje
    
    def calcular_salario(self):
        return self.salario_base
    
    def trabajar(self):
        print(f"{self.nombre} esta desarrollando en {self.lenguaje}")

empleados = [
    Gerente("Ana", 4000,1000),
    Desarrollador("Luis", 3000, "Python")
]

for elemento in empleados:
    elemento.trabajar()
    print("Salario", elemento.calcular_salario())
    print("------------")