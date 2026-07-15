frutas = ("manzana", "banana", "naranja")
print(frutas)
print(frutas[0])
print(frutas[1:2])

print(frutas.count("manzana"))
print(frutas.index("naranja"))

# pasar una tupla a lista
#pasar la tupla a una lista eleiminar un elemento y volver a convertirlo a tupla
copia = list(frutas)
copia.remove("naranja")
frutas = tuple(copia)
print(frutas)
