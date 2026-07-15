"""
escribir un programa que pida al usuario dos numeros y muestre un
menu de opciones, usma, resta, multiplicacion y division.
1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Division entera
6. Potencia 
7. Modulo (Residuo de la division)
8. Salir
"""
def suma(x,y):
    resultado = x + y
    return resultado

def resta(x,y):
    resultado = x - y
    return resultado

def multiplicacion(x,y):
    resultado = x * y
    return resultado

def division(x,y):
    resultado = x / y
    return resultado

def divisionEntera(x,y):
    resultado = x // y
    return resultado

def potencia(x,y):
    resultado = x ** y
    return resultado

def modulo(x,y):
    resultado = x % y
    return resultado

a = int(input("ingrese el primer numero: "))
b = int(input("ingrese el segundo numero: "))

menu = """
1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Division entera
6. Potencia 
7. Modulo (Residuo de la division)
8. Salir
"""
print(menu)

opcion = 0

while opcion != 8:
    opcion = int(input("seleccione una opcion"))
    if opcion == 1:
        print(f"el resultado de la suma es {suma(a,b)}")
    elif opcion == 2:
        print(f"el resultado de la resta es {resta(a,b)}")
    elif opcion == 3:
        print(f"el resultado de la multiplicacion es {multiplicacion(a,b)}")
    elif opcion == 4:
        print(f"el resultado de la division es {division(a,b)}")
    elif opcion == 5:
        print(f"el resultado de la division entera es {divisionEntera(a,b)}")
    elif opcion == 6:
        print(f"el resultado de la potencia es {potencia(a,b)}")
    elif opcion == 7:
        print(f"el resultado del modulo es {modulo(a,b)}")
    elif opcion == 8:
        print("Hasta pronto")
        break
    else:
        print("seleccione una opcion valida")