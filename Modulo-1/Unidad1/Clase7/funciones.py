for x in range (1,11):
    print (x)

"""
tabla de multiplicar con el ciclo for
"""
tabla = int(input("que tabla de multiplicar quiere? "))
for x in range(1,11):
    print(f"{tabla} x {x} = {tabla * x}")

"""
Hacer desde la tabla del 1 hasta la tabla del 10
"""

for x in range (1, 11):
    print(f"Tabla del {x}")
    for z in range (1,11):
        print(f"{x} x {z} = {x*z}")
    print("")

"""
funciones
"""

def suma1():
    a = int(input("digite el primer numero: "))
    b = int(input("digite el segundo numero: "))
    resultado = a+b
    print(f"el resultado de la suma es: {resultado}")

def suma2(a,b):
    resultado = a + b
    print(f"el resultado de la suma es: {resultado}")

def suma3():
    a = int(input("digite el primer numero: "))
    b = int(input("digite el segundo numero: "))
    resultado = a+b
    return resultado

def suma4(a,b):
    resultado = a + b
    return resultado

suma1()

n1 = int(input("digite el primer numero: "))
n2 = int(input("digite el segundo numero: "))
suma2(n1,n2)
# suma2(2,5)

print(suma3())

n1 = int(input("digite el primer numero: "))
n2 = int(input("digite el segundo numero: "))
print(suma4(n1, n2))

# suma4(2,5)

