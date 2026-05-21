frutas = {"manzana", "banana", "naranja", "pera", "uva"}

print(frutas)
print(len(frutas))
frutas.add("kiwi")
print(frutas)
frutas.remove("pera")
#elimina aleatoriamente
frutas.pop()
print(frutas)

#para limpiar el conjunto pero el conjunto sigue extistiendo 
frutas.clear()
print(frutas)

#para hcaer una copia
frutas.copy()

#muestra las frutas que estan frutas1 pero no esta en frutas 2
frutas1 = {"manzana", "banana", "naranja", "pera", "uva"}
frutas2 = {"kiwi", "fresa", "melon", "pera", "uva"}
print(frutas1.difference(frutas2))

#intersection muestra las que estan en las dos 
print(frutas1.intersection(frutas2))

#union une lo que esta en los dos
print(frutas1.union(frutas2))

#difetence update - 