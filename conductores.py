
Nombre_Conductores = []
Kilometros_Diarios = []
Total_kms = []

Conductores = int(input("Ingrese la cantidad de conductores: "))

for x in range(Conductores):
    Nom = input("Por favor ingrese el nombre del conductor: ")
    Nombre_Conductores.append(Nom)
    Acum_kms = 0
    Kilometros_Diarios = []
for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]:
    Kilometros = int(input(f"Ingrese la cantidad de kilometros recorridos por {Nom} el {dia}: "))
    Kilometros_Diarios.append(Kilometros)
    Acum_kms += Kilometros
    Total_kms.append(Acum_kms)

print("\nResumen de los kilómetros recorridos por cada conductor:")
for i in range(Conductores):
    print(f"{Nombre_Conductores[i]} recorrió un total de {Total_kms[i]} km esta semana.")
