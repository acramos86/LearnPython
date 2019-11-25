num1 = float(input("Ingrese el primer numero "))
num2 = float(input("Ingrese el segundo numero "))
if num1 > num2:
	print("El numero que ingrsado primero (" + str(num1) + ") es mayor al segundo (" + str(num2) + ")")
elif num1 == num2:
	print("Los numero ingresados son iguales")
else:
	print("El numero que se ingreso de segundo (" + str(num2) + ") es mayor que el que se ingreso de primero (" + str(num2) + ")")