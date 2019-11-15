import math

print("Inrese los catetos del triangulo rectangulo")
print("Cateto 1")
cat1 = float(input())

print("Cateto 2")
cat2 = float(input())

hiputenusa = math.pow( (math.pow(cat1,2) + math.pow(cat2,2)), (1/2))

print("La hiputenusa del trianguloo es " + str(hiputenusa))