import random

def mostrar_menu():
    print("Menú Principal")
    print("1. Juego de dados")
    print("2. Grupos de alumnos")
    print("3. Precio de entrada a la sala de juegos")
    print("4. Contraseña")
    print("5. Salir")

def juego_dados():
    nombres = ['Álvaro', 'Bárbara']
    puntuaciones = [random.randint(1, 6) for _ in range(2)]

    print(f"{nombres[0]} tira un dado y obtiene un puntaje de {puntuaciones[0]}")
    print(f"{nombres[1]} tira un dado y obtiene un puntaje de {puntuaciones[1]}")

    if puntuaciones[0] > puntuaciones[1]:
        print(f"{nombres[0]} gana")
    elif puntuaciones[0] < puntuaciones[1]:
        print(f"{nombres[1]} gana")
    else:
        print("Empate")

def grupos_alumnos():
    nombre = input("Ingrese su nombre: ")
    sexo = input("Ingrese su sexo (M/F): ").upper()

    if (sexo == "M" and nombre < "M") or (sexo == "F" and nombre >= "M"):
        print("Le corresponde el grupo A")
    else:
        print("Le corresponde el grupo B")

def precio_entrada():
    edad = int(input("Ingrese la edad del cliente: "))

    if edad < 4:
        print("La entrada es gratuita")
    elif 4 <= edad <= 18:
        print("Debe pagar 30000 pesos")
    else:
        print("Debe pagar 50000 pesos")

def validar_contraseña():
    contraseña = "secr3t"
    while True:
        user_password = input("Ingrese la contraseña: ")
        if user_password == contraseña:
            print("Contraseña correcta")
            break
        else:
            print("Contraseña incorrecta, vuelva a intentarlo")

def calcular_iva(cantidad, porcentaje=0.21):
    return cantidad * (1 + porcentaje)

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            juego_dados()
        elif opcion == 2:
            grupos_alumnos()
        elif opcion == 3:
            precio_entrada()
        elif opcion == 4:
            validar_contraseña()
        elif opcion == 5:
            print("Vuelva Pronto :) ")
            break
        else:
            print("Opción inválida")