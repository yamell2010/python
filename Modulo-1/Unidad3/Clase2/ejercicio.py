"""
pedir al usuario que ingrese notas entre 0 y 10,
hasta que ingrese -1 para finalizar.
luegi, mostrar el promdeio de las notas ingresada"""

notas =[]

while True:
    nota = float(input("ingrese una nota entre 0 y 10 (o -1 para finalizar)"))
    if nota == -1:
        break
    if 0 <= nota <= 10:
        notas.append(nota)
    else:
        print("nota invalida. ingrese bien la nota")

if notas:
    promedio = sum(notas) /len(notas)
    print(f"el promedio de las notas ingresadas es {promedio}")
else:
    print("no se ingresaron notas valdas.")