"""
Crear una clase Libro con:
-Atributos (privados)
titulo
autor
ISBN
precio
-Requsitos
Contructor parametrizado
Getter y setters para todos los atributos
Metodo que muestre la informacion del libro
crear minimo 3 libros
"""

class Libro:
    def __init__(self, titulo, autor, ISBN, precio):
        self.__titulo = titulo
        self.__autor = autor
        self.__ISBN = ISBN
        self.__precio = precio
    
    def get_titulo(self):
        return self.__titulo
    
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_autor(self):
        return self.__autor
    
    def set_autor(self, autor):
        self.__autor = autor

    def get_ISBN(self):
        return self.__ISBN
    
    def set_ISBN(self, ISBN):
        self.__ISBN = ISBN
    
    def get_precio(self):
        return self.__precio
    
    def set_precio(self, precio):
        if precio > 0:
            self.__precio = precio
        else:
            print("El precio debe ser mayor")

    def mostrar(self):
        print("Titulo:", self.get_titulo())
        print("Autor:", self.get_autor())
        print("ISBN:", self.get_ISBN())
        print("Precio:",self.get_precio())
        print("---------------------")
    

def main():

    libro1 = Libro("Cien años de soledad", "gabriel garcia", 1351, 14523)
    libro2 = Libro("las ovejas", "pepe perez", 5881, 20523)
    libro3 = Libro("Las cabras", "jose pintor", 1351, 14523)

    libro1.mostrar()
    libro2.mostrar()
    libro3.mostrar()

    # ejemplo de setter

    libro1.set_precio(16000)
    print("nuevo valor libro1", libro1.get_precio())
    libro1.mostrar()

main()