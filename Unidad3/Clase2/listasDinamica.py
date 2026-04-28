"""
a = [1,2,3,4,5,"mama,True,3.14,[6,7,8]"]
print(a)
print(a[0])
print(a[5])
print(a[8][2])
"""
"""
a = [1,2,3,4,5,6,7,8,9,10]
print(a)
print(a[0])
print(len(a))
"""

a = ["fresa", "manzana", "pera", "naranja", "sandia"]
print(a[2:4])
print(a[0:4])
c = 0
for elemento in a:
    e = len(elemento)
    c = c+e

print(f"el numero de caracteres de la lista es: {c}") 

"""
pos = 0
while pos < len(a):
    print(a[pos])
    pos += 1
"""

b = ["fresa", "manzana", "pera", "manzana", "naranaja","manzana", "sandia"]

i= 0
while i < len(b):
    if b[i] == "manzana":
        print("encontre manzana en la posicion", i)
        i = i+1
    