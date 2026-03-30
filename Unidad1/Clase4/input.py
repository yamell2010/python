nombre1 = input("ingrese su nombre: ")

numero1 = int(input("ingrese un numero: "))
numero2 = int(input("ingrese otro numero: "))

print(f"Hola {nombre1} la suma de los numero es, {numero1+numero2}")
print(f"Hola {nombre1} la resta de los numero es, {numero1-numero2}")
print(f"Hola {nombre1} la multiplicacion de los numero es, {numero1*numero2}")
print(f"Hola {nombre1} la division de los numero es, {numero1/numero2}")
print(f"Hola {nombre1} la division entera de los numero es, {numero1//numero2}")
print(f"Hola {nombre1} el modulo de la divison de los numero es, {numero1%numero2}")
print(f"Hola {nombre1} la potencia de los numero es, {numero1**numero2}")

# calcule el area de un circulo 
PI = 3.1416
diametro = float(input("cual es el diametro del circulo? "))
print(f"el area del circulo es{PI*(diametro**2)}")

# escriba un programa en python que calcule el area de un triangulo rectangulo

base = float(input("digite la base del triangulo rectangulo: "))
altura = float(input("digite la altura del triangulo rectangulo"))
print(f"el areal del triangulo rectangulo es {(base*altura)/2}")

""" vamos a calcular el valor a pagar a un empleado por su trabajo de la semana
le vamos a preguntar al usuario cuantas horas trabajo el empleado y cuanto gana por hora 
y al final le vamos a mostrar el valor a pagar al empleado por su trabajo de la semana
"""
horasDeTrabajo = int(input("cuantas horas trabajo esta semana?"))
valorHora = float(input("cuanto es el valor de cada hora de trabajo?"))
print(f"esta semana has ganado el valor de {horasDeTrabajo * valorHora}")