class Animal:
    def __init__(self,nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        return "hacer sonido generico"

class Perro(Animal):
    def hacer_sonido(self):
        return "guau guau"
    
class Gato(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre)
        self.edad = edad

# da como resultado "guau guau" porque la clase hija tiene su propio metodo
p = Perro("Trosky")
print(f"{p.nombre} dice", p.hacer_sonido())
p.hacer_sonido()

a = Animal("Laika")
print(f"{a.nombre} dice", p.hacer_sonido())
a.hacer_sonido()

g = Gato("Mirringo", 5)
print(g.edad)
print(g.hacer_sonido())
# el sonido que el objeto gato retorna es "un sonido generico" debido a que no tiene ese metodo pero si lo tiene la clase padre
