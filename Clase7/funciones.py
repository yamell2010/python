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

