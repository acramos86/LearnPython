contrasenia = "Alex"
clave = input("Ingrese su contrasenia: ")

while clave != contrasenia:
	print("Clave incorrecta")
	mas = input("Desea intentarlo otra vez?? (S/N)").upper()
	if mas == "N":
		break;
	clave = input("Ingrese su contrasenia: ")


print("Finalizado")
