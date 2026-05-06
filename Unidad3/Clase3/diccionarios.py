carro = {
    "marca" : "toyota",
    "modelo" : "corolla",
    "año" : 2020,
    "colores": ["rojo", "azul", "negro"],
    "electrico": False
} 

print(carro["marca"])
print(carro["modelo"])
print(carro["modelo"])

carro["color"] = "rojo"
print(carro)
print(len(carro))
print(carro["colores"])
print(type(carro))

fruta = dict(nombre = "Manzana", color = "rojo", sabor = "dulce", valor = 2500)
print(fruta)

carro.pop("marca")

#recorrer el diccionario
#este imprime la clave
for x in carro:
    print(x)

for x in carro.values:
    print(x)
#este imprime lo que contiene
for x in carro:
    print(carro[x])

for x in carro.keys:
    print(x)

#para ver los dos 
for x, y in carro.items:
    print(x, y)

# copia del diccionario

carro = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
carro2 = carro.copy()
print(carro2)

# Diccionaros anidados

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# de otra forma

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# imprimir un elemento de los diccionarios 

print(myfamily["child2"]["name"])

