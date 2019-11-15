print("Inrese 3 numeros para encontrar su promedio")
print("Numero 1")
num1 = float(input())
print("Numero 2")
num2 = float(input())
print("Numero 3")
num3 = float(input())

numList = [num1, num2, num3]

promedio = (num1 + num2 + num3)/len(numList)

print("El promedio de los valores es " + str(promedio))