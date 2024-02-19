class Fruteria:
    def __init__(self):
        self.precios_frutas = {
            "manzana": 2500, 
            "banana": 1800,
            "naranja": 3000,
            "pera": 2000,
            "uva": 4500
        }

    def calcular_precio(self, fruta, cantidad):
        if fruta in self.precios_frutas:
            precio_unitario = self.precios_frutas[fruta]
            precio_total = precio_unitario * cantidad
            print(f"El precio total de {cantidad} {fruta}(s) es: ${precio_total}")
        else:
            print("Lo siento, esa fruta no está en nuestro inventario.")

    def menu(self):
        while True:
            print("\nMenú:")
            print("1. Consultar precio de una fruta")
            print("2. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                fruta = input("Ingrese el nombre de la fruta: ").lower()
                cantidad = int(input("Ingrese la cantidad vendida: "))
                self.calcular_precio(fruta, cantidad)
            elif opcion == "2":
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

def main():
    fruteria = Fruteria()
    fruteria.menu()


if __name__ == "__main__":
    main()
