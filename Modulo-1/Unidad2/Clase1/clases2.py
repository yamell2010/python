class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
            return self.__nombre
        
    def set_nombre(self, nombre):
            self.__nombre = nombre

persona1 = Persona("juan")
print(persona1.get_nombre())
persona1.set_nombre("pedro")
print(persona1.get_nombre())
p1 = Persona("Maria")