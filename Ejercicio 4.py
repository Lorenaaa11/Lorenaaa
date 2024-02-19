class CestaDeCompra:
    def __init__(self):
        self.cesta = {}

    def agregar_articulo(self):
        articulo = input("Ingrese el artículo que desea añadir a la cesta: ")
        precio = float(input("Ingrese el precio del artículo: "))
        self.cesta[articulo] = precio
        print(articulo, "agregado a la cesta.")

    def mostrar_cesta(self):
        print("\nCesta de la compra:")
        total = 0
        for articulo, precio in self.cesta.items():
            print(articulo, ":", precio)
            total += precio
        print("\nCoste total: ", total)

    def menu(self):
        while True:
            print("\nMenú:")
            print("1. Añadir artículo a la cesta")
            print("2. Mostrar cesta de la compra")
            print("3. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_articulo()
            elif opcion == "2":
                self.mostrar_cesta()
            elif opcion == "3":
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

def main():
    cesta_compra = CestaDeCompra()
    cesta_compra.menu()

if __name__ == "__main__":
    main()
