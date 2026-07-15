from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

class Cuadro(Figura):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado * self.lado

c = Cuadro(7)
print(c.area())

"""
Crear una clase abstracta Empleado, Metodo abstracto calcular salario
sub clase Desarrollador
"""

from abc import ABC, abstractmethod

class Empleado(ABC):
    @abstractmethod
    def salario(self):
        pass

class Desarrollador(Empleado):
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.__salario = salario
    
    def get_salario(self):
        return self.__salario

    def salario(self):
        return self.get_salario() * 30

a = Desarrollador("juan", 2000)
print(f"el trabajador {a.nombre} tiene un salario de {a.salario()}")