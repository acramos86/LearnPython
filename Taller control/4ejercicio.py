num1 = float(input("Digite un numero "))
num2 = float(input("Digite otro numero diferente de cero (0) "))

if num2 == 0:
	print("El numero ingresado de segundo es 0, la division no se puede realizar")
else:
	respuesta = num1/ num2
	print("La division de los 2 numero es " + str(respuesta))