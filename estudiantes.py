edades_mañana = 0
edades_tarde = 0
edades_noche = 0


for i in range(6):
    edad = int(input("Ingrese la edad del estudiante del turno mañana: "))
    edades_mañana += edad

for i in range(7):
    edad = int(input("Ingrese la edad del estudiante del turno tarde: "))
    edades_tarde += edad

for i in range(12):
    edad = int(input("Ingrese la edad del estudiante del turno noche: "))
    edades_noche += edad

promedio_mañana = edades_mañana / 6
promedio_tarde = edades_tarde / 7
promedio_noche = edades_noche / 12

print("Promedio de edades del turno mañana:", promedio_mañana)
print("Promedio de edades del turno tarde:", promedio_tarde)
print("Promedio de edades del turno noche:", promedio_noche)


if promedio_mañana > promedio_tarde and promedio_mañana > promedio_noche:
    print("El turno mañana tiene el promedio de edades mayor.")
elif promedio_tarde > promedio_mañana and promedio_tarde > promedio_noche:
    print("El turno tarde tiene el promedio de edades mayor.")
else:
    print("El turno noche tiene el promedio de edades mayor.")
