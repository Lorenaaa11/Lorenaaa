alturas = input("Ingrese un conjunto de números de alturas de personas, separados por espacios: ")

alturas_list = [int(altura) for altura in alturas.split()]

altura_promedio = sum(alturas_list) / len(alturas_list)

print("La altura promedio de las personas es:", altura_promedio)