"""
vamos a hacer un programa que nos diga el sueldo a recibir
deun empleado, si gana menos de 2.000.000 de pesos le vamos a dar 
un subsidio de 200.000 pesos
"""

sueldo =int(input("ingrese el sueldo del empleado: "))
if sueldo <2000000:
    print(f"el sueldo que recibira el empleado es de {sueldo + 200000}")
else:
    print(f"el sueldo que recibira el empleado es de {sueldo}")



"""
escribir un programa e python que solicite al usuario su edad
y determinar si es mayor o no.
si la edad es mayor o igual a 18 años, el programa debe imprimir "eres mayor de de edad"
en caso contrario, debe imprimir "eres menor de edad".
"""
edad = int(input("dime cual es tu edad: "))
if edad >= 18:
    print("eres mayor de edad")
else:
    print("eres menor de edad")


"""
de cero a 5 primera infancia
de 6 a 12 infancia 
de 13 a 18 adolecente
mayor a 18 adultez
"""

edad2 = int(input("dime cual es tu edad: "))
if edad2 <= 5:
    print("estas en la primera infancia")
elif edad2 >=6 and edad2 <= 12:
    print("estas en la infancia")
elif edad2 >= 13 and edad2<= 18:
    print("estas en la dolecencia")
elif edad2 > 18:
    print("estas en la adultez")

"""
escribir un programa con python que solicite al usuario un numero entre 1 y 7 
si es 1 impirmir "lunes"
si es 2 imprimir "martes"
si es 3 imprimir "miercoles"
si es 4 imprimir "jueves"
si es 5 imprimir "viernes"
si es 6 imprimir "sabado"
si es 7 imprimir "domingo"
y si el numero no esta entre 1 y 7 imprimir "numero no valido"
"""

numero =int(input("digite un numero: "))
if numero == 1:
    print("lunes")
elif numero == 2:
    print("martes")
elif numero == 3:
    print("miercoles")
elif numero == 4:
    print("jueves")
elif numero == 5:
    print("viernes")
elif numero == 6:
    print("sabado")
elif numero == 7:
    print("domingo")
elif numero <= 0 and numero > 7:
    print("digite un numero valido")

numero =int(input("digite un numero: "))
if numero == 1:
    print("lunes")
elif numero == 2:
    print("martes")
elif numero == 3:
    print("miercoles")
elif numero == 4:
    print("jueves")
elif numero == 5:
    print("viernes")
elif numero == 6:
    print("sabado")
elif numero == 7:
    print("domingo")
else:
    print("digite un numero valido")

"""
preguntar al usuario un animel (perro, gato, pez)
si el animal es perro impirmir "guau"
si el animal es gato imprimir "miau"
si el animal es pez imprimir "blub"
y si es animal no es ninguno de esos imprimir "animal no conocido"
"""

animal = input("dime un animal: ")
match animal:
    case "perro":
        print("guau")
    case "gato":
        print("miau")
    case "pez":
        print("blub")
    case _:
        print("animal no conocido")

"""
while
"""
i = 1
while i < 11:
    print(i)
    i = i+1

"""
que tabla de multiplicar quiere
"""
n = int(input("que tabla de multiplicar quiere?"))
i = 1
while i <= 10:
    print(f" {n*i}")
    i=i+1
