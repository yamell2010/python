# Los 4 tipos de funciones que existen 
def suma1():
    a =5
    b=10
    print(a+b)

def suma2(n1, n2):
    print(n1 + n2)

def suma3():
    n1 = 5
    n2 = 10
    return n1 + n2

def suma4(n1, n2):
    return n1 + n2

#lambda

suma5 = lambda n1, n2: n1 + n2

print("aqui arranca el programa")
suma1()
suma2(15, 20)
print(suma3())
print(suma4(25, 30))

print(suma4(5, 10))
print(suma5(5, 10))

a = 5
b = 6
print(suma5(a, b))


"""
-------------------------------------------------------------------------
"""
suma = lambda n1, n2, n3:n1+n2+n3

print(suma(5,10,15))


doble = lambda x: x*2

print(doble(5))

es_mayor = lambda edad : "es mayor" if edad >= 18 else "menor de edad"

print(es_mayor(18))
print(es_mayor(17))


numeros = [1,2,3,4,5]
# map() hace que se multiplique por cada numero de la lista
# list() convierte los numeros en una lista porque es un constructor
dobles = list(map(lambda x: x*2, numeros))

print(dobles)


nombres = ["Alice", "Bob", "Charlie"]

nombres_mayuscula = list(map(lambda x: x.upper(), nombres))
print(nombres_mayuscula)

nombres_largos = list(map(lambda x: "nombre largo" if len(x) > 3 else "nombre corto", nombres))
print(nombres_largos)


def nombre_largo_fun ():
    l =[]
    for i in nombres:   
        l.append(i.upper())
    print(l)
nombre_largo_fun()



precios = [10,20,30,40,50]
precios_iva = list(map(lambda x:x*1.19, precios))
print(precios_iva)


#-----------------------------------------------------
#FILTER

numeros = [1,2,3,4,5,6,7,8,9,1]

pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

#------------------------------------------------------
edades = [15, 22, 30, 17, 25, 19]

mayores_edad = list(filter(lambda x: x >= 18, edades))

print(mayores_edad)