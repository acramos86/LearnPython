print("Ingrese la nota de los 3 talleres")
print("Taller 1")
taller1 = float(input())
print("Taller 2")
taller2 = float(input())
print("Taller 3")
taller3 = float(input())
print("Ingrese la nota del examen final")
exaFinal = float(input())
print("Ingrese la nota del trabajo final")
trabFinal = float(input())

talleres = (( taller3+taller2+taller1 ) /3 ) * 0.55

parcial = exaFinal * 0.3

final = trabFinal * 0.15

print("La nota de talleres definitiva es " + str(talleres))
print("La nota del parcial final es " + str(exaFinal) + " y su acumulado es " + str(parcial))
print("La nota del trabajo final es " + str(trabFinal) + " y su acumulado es " + str(final))
print("La nota definitiva es " + ( str( parcial+final+talleres )))