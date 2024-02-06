cont = 0
Acum = 0

while cont <10:
    Num = int (input("Ingrese el numero"))
    Acum=Acum+Num

    cont += 1
Promedio = Acum/10

print("La suma de los numeros es: ",Acum)
print("El promedio de los 10 numeros es: ",Promedio)