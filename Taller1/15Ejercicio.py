print("Ingrese 2 variables para ser intercambiadas")
print("Variable equivalente a A")
a = float(input())
print("Variable equivalente a B")
b = float(input())
print("La variable A es igual a " + str(a) + " Y la variabe B es igual a " + str(b))

c = a
a = b
b = c

print("Despues de procesado la variable A es igual A " + str(a) + " y la variable B es igual a " + str(b))