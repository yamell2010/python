veterinaria = {}

opcion = ""

while opcion != 8:

    print("\n========== MENÚ VETERINARIA ==========")
    print("1. Agregar cliente")
    print("2. Agregar mascota a un cliente")
    print("3. Mostrar todos los clientes y sus mascotas")
    print("4. Buscar una mascota")
    print("5. Calcular peso promedio de mascotas de un cliente")
    print("6. Encontrar la mascota más pesada")
    print("7. Eliminar una mascota")
    print("8. Eliminar un cliente")
    print("9. Salir")

    opcion = input("seleccione una opcion: ")

    if opcion ==1:
        nombre_cliente = input("ingrese el nombre del cliente: ")

        if nombre_cliente in veterinaria:
            print("el cliente ya existe")
        else:
            telefono = input("ingrese el numero del cliente: ")

            veterinaria[nombre_cliente] = {
                "telefono": telefono,
                "mascotas": {}
            }
    elif opcion == 2:
        nombre_cliente = input("ingrese el nombre del cliente:")

        if nombre_cliente in veterinaria:
            nombre_mascota = input("ingrese el nombre de la mascota: ")

            if nombre_mascota in veterinaria[nombre_cliente]["mascotas"]:
                print("esta mascota ya esta registrada para este cliente")
            else:
                especie = input("ingrese la especie de la mascota: ")
                edad = int(input("ingrese la edad de la mascota: "))
                peso = float(input("ingrese el peso de la mascota en kg: "))

                veterinaria[nombre_cliente]["mascotas"][nombre_mascota] ={
                    "especie" : especie,
                    "edad" : edad,
                    "peso" : peso
                }

                print("Mascoa agregada correctamente")
        else:
            print("el cliente no existe")