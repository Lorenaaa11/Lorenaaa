import random

Secreto = random.randint(1,10)

Numero = int(input("Adivinar el numero entreo 1 a 10"))

while Numero != Secreto:
    if Numero < Secreto:
        print("el numero es mayor")
    else:
        print("El numero es menor")

    Numero = int(input("Intente de nuevo:"))

print("Felicitaciones adivinaste el numero secreto:",Secreto)
