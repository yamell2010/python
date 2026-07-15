"""
crear una clase padre vehiculo y tres clases hijas
carro, moto, barco
"""
class Vehiculo:
    def __init__(self, matricula, marca, ciudad):
        self.__matricula = matricula
        self.marca = marca
        self.ciudad= ciudad
    
    def get_matricula(self):
        return self.__matricula
    
    def set_matricula(self, nueva_placa):
        self.__matricula = nueva_placa


class Carro(Vehiculo):
    def __init__(self, matricula, marca, ciudad, puertas):
        super().__init__(matricula, marca, ciudad)
        self.puertas = puertas

class Moto(Vehiculo):
    def __init__(self, matricula, marca, ciudad, llantas):
        super().__init__(matricula, marca, ciudad)
        self.llantas = llantas

class Barco(Vehiculo):
    def __init__(self, matricula, marca, ciudad, velas):
        super().__init__(matricula, marca, ciudad)
        self.velas = velas

c = Carro("VCX 589", "Hiunday", "valledupar", 5)
print(f"el vehiculo es de placas: {c.get_matricula()}")

m = Moto("VCF 86 V", "Honda", "Valledupar", 4)
print(f"el vihiculo es de placas: {m.get_matricula()}")

b = Barco("ADS 54 SD", "bARS", "Santa Marta", 4)
print(f"el vihiculo es de placas: {b.get_matricula()}")