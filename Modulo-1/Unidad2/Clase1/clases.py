class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        return "¡Guau!"
    def rascarse(self):
        print("me estoy rascando")
    
perro1 = Perro("Fido", 3)
perro2 = Perro("Trosky",5)
print(perro1.nombre, perro1.edad)
print(perro2.nombre, perro2.edad)

print(perro1.ladrar())
perro1.ladrar()