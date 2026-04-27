frutas = ["papaya", "naranja", "pera", "fresa"]
print(len(frutas))
print("naranja" in frutas)
frutas.append("kiwi")
print(frutas)
frutas[2]="aguacate"
print(frutas)
print(frutas[2])
frutas.reverse()
print(frutas)

frutas.clear()
# limpia la lista

# del frutas
# elimina la 

copia = frutas.copy
print(copia)
# copy crea una copia 

# para hacer una copia de una lista no se puede asiganr porque si se borra
# la original se borra la copia tambien,por eso se usa copy()

# count dice cuantas veces hay un elemento en la lista
frutas.copy("pera")

# extend agrega a la lista los valores que yo le paso
frutas.extend("platano", "banano")

verduras = ["platano", "banano", "piña"]
frutas.extend(verduras)
print(frutas)

# el append mete un elemento y el extend agreg una coleccion

#index muestra la posicion en la que esta el elemento 
print(frutas.index("pera"))

# el insert mete el elemento en la posicion que se desee

frutas.insert(4,"mango")

# pop es para extraer, se lo puedes asignar una variable o no 
# si no se le da la posicion saca el ultimo 
a = frutas.pop(1)
print(frutas)

# Upper es para convertir todo en mayuscula

txt = "Carlos fadul"
print(txt.upper())

# remove remueve el elemento que yo le diga
frutas.remove("naranaja")
print(frutas)

# si hay varios elementos toca recorrer la lista con un ciclo

#reverse voltea la lista
frutas.reverse()
print(frutas)


# sort ordena pero solo si todos los elementos son del mismo tipo

frutas.sort()
print(frutas)
