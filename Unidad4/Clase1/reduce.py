from functool import reduce

numeros = [1,2,3,4,5]

suma_total = reduce(lambda acumulador, numero: acumulador + numero, numeros)
producto = reduce(lambda acumulador, numero: acumulador * numero, numeros)
maximo = reduce(lambda a, b: a if a > b else b, numeros)

print(suma_total)
print(producto)
print(maximo)
