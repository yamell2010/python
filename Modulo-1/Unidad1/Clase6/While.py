menu = """
MENU
1. Carne
2. Pechuga 
3. Hamburguesa 
4. Perro
5. Salchipapa
6. Salir 
"""
opcion = 0
while opcion != 6:
    opcion = int(input("seleccione una opcion: "))
    if opcion == 1:
        print("selecciono carne")
    elif opcion == 2:
        print("selecciono pechuga")
    elif opcion == 3:
        print("selecciono hamburguesa")
    elif opcion == 4:
        print("selecciono perro")
    elif opcion == 5:
        print("selecciono salchipapa")
    elif opcion == 6:
        print("gracias por visitarnos")
        break
    else:
        print("seleccione una opcon valida")
print(menu)


"""
agregar el precio ahora
"""

menu = """
MENU
1. Carne - 20000
2. Pechuga - 15000
3. Hamburguesa - 16000
4. Perro - 18000
5. Salchipapa - 22000
6. Salir 
"""
opcion = 0
total = 0 
while opcion != 6:
    opcion = int(input("seleccione una opcion: "))
    if opcion == 1:
        print("selecciono carne")
        total = total + 20000
    elif opcion == 2:
        total = total + 15000
        print("selecciono pechuga")   
    elif opcion == 3:
        total = total + 16000
        print("selecciono hamburguesa")
    elif opcion == 4:
        total = total + 18000
        print("selecciono perro")
    elif opcion == 5:
        total = total + 22000
        print("selecciono salchipapa")
    elif opcion == 6:
        print("gracias por visitarnos")
        print(f"el valor total es: {total}")
        break
    else:
        print("seleccione una opcon valida")
print(menu)