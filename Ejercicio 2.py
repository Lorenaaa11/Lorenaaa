class ListaNumeros:
    def __init__(self):
        self.lista = []

    def agregar_numero(self):
        numero = int(input("Ingrese el número que desea agregar a la lista: "))
        self.lista.append(numero)
        print("Número añadido a la lista.")

    def agregar_numero_posicion(self):
        numero = int(input("Ingrese el número que desea agregar a la lista: "))
        posicion = int(input("Ingrese la posición en la que desea agregar el número (empezando desde 1): "))
        self.lista.insert(posicion - 1, numero)
        print("Número añadido a la lista en la posición especificada.")

    def longitud_lista(self):
        print("La longitud de la lista es:", len(self.lista))

    def eliminar_ultimo_numero(self):
        if self.lista:
            ultimo_numero = self.lista.pop()
            print("Se eliminó el último número de la lista:", ultimo_numero)
        else:
            print("La lista está vacía.")

    def eliminar_numero_posicion(self):
        if self.lista:
            posicion = int(input("Ingrese la posición del número que desea eliminar (empezando desde 1): "))
            if 1 <= posicion <= len(self.lista):
                numero_eliminado = self.lista.pop(posicion - 1)
                print("Se eliminó el número", numero_eliminado, "de la lista.")
            else:
                print("La posición especificada no existe en la lista.")
        else:
            print("La lista está vacía.")

    def contar_numeros(self):
        numero = int(input("Ingrese el número que desea contar en la lista: "))
        cantidad = self.lista.count(numero)
        print("El número", numero, "aparece", cantidad, "veces en la lista.")

    def posiciones_numero(self):
        numero = int(input("Ingrese el número del cual desea conocer las posiciones: "))
        posiciones = [i + 1 for i, x in enumerate(self.lista) if x == numero]
        if posiciones:
            print("El número", numero, "aparece en las posiciones:", posiciones)
        else:
            print("El número", numero, "no está en la lista.")

    def mostrar_numeros(self):
        print("Números en la lista:", self.lista)

    def menu(self):
        while True:
            print("\nMenú:")
            print("1. Añadir número a la lista")
            print("2. Añadir número de la lista en una posición")
            print("3. Longitud de la lista")
            print("4. Eliminar el último número")
            print("5. Eliminar un número")
            print("6. Contar números")
            print("7. Posiciones de un número")
            print("8. Mostrar números")
            print("9. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_numero()
            elif opcion == "2":
                self.agregar_numero_posicion()
            elif opcion == "3":
                self.longitud_lista()
            elif opcion == "4":
                self.eliminar_ultimo_numero()
            elif opcion == "5":
                self.eliminar_numero_posicion()
            elif opcion == "6":
                self.contar_numeros()
            elif opcion == "7":
                self.posiciones_numero()
            elif opcion == "8":
                self.mostrar_numeros()
            elif opcion == "9":
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")


# Instanciar la clase y ejecutar el menú
if __name__ == "__main__":
    lista_numeros = ListaNumeros()
    lista_numeros.menu()

