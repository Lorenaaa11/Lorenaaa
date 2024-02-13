Nombres=[]
Notas=[]
Amejor=[]
mb=0
b=0
In=0


for x in range(1,5):
    Nom = input("Por favor ingresar el nombre del alumno:")
    Nombres.append(Nom)
    No = int(input(f"Por favor ingresar las notas del alumnno:"))
    Notas.append(No)

for y in range(len(Nombres)):
    print(f"El alumno(A){Nombres[y]}",f"Tiene la nota {Notas[y]}")

    if Notas[y]>=8:
        print("Alumno muy bueno")
        mb += 1
        Amejor.append(Nombres[y])
    else:
        if Notas[y]>=4:
            print("Alumno bueno")
            b += 1
        else:
            print("Alumno no aprueba la materia")
            In += 1
print("Listado inicial de los alumnos son :", Nombres)

eliminar = []
for z in range(len(Notas)):
    if Notas[z]>=4 and Notas[z]<=7:
        eliminar.append(z)

for d in sorted(eliminar,reverse=True):
        Notas.pop(d)
        Nombres.pop(d)

print("Cantidad de alumnos buenos son:",mb)
print("Los nombres de los mejores alumnos x nota son:",Amejor)
print("Listado de alumnos",Nombres)
 