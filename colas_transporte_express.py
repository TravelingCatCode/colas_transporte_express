class ColaSeguimiento:
    print('*** Bienvenido al Sistema de envíos de Transporte Express ***')

    # Inicializamos la cola del sistema
    def __init__(self):
        self.cola = []

    def enqueue(self, producto):
        # Agregamos los productos al final de la cola
        self.cola.append(producto)
        print(f"Producto '{producto}' agregado.")

    def dequeue(self):
        # Borra y muestra el producto al frente de la cola
        if self.is_empty():
            print("La cola está vacía, no hay productos para procesar.")
            return None
        producto = self.cola.pop(0)
        print(f"Producto '{producto}' procesado.")
        return producto

    def peek(self):
        # Muestra el primer producto de la cola sin eliminarlo
        if self.is_empty():
            print("La cola está vacía.")
            return None
        return self.cola[0]

    def is_empty(self):
        # Verificamos si la cola está vacía
        return len(self.cola) == 0

    def size(self):
        # Muestra el número de pedidos en la cola
        return len(self.cola)

# Menú del sistema
def menu():
    sistema_seguimiento = ColaSeguimiento()

    while True:
        # Mostramos las opciones del menú
        print("\nOpciones:")
        print("1. Agregar un producto a la cola")
        print("2. Procesar el producto al frente de la cola")
        print("3. Consultar el siguiente producto a procesar")
        print("4. Verificar si la cola está vacía")
        print("5. Consultar el número de productos en la cola")
        print("6. Salir")

        # Solicitamos la opción al usuario
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Agregar un producto
            producto = input("Ingrese el nombre del producto: ")
            sistema_seguimiento.enqueue(producto)

        elif opcion == "2":
            # Procesar un producto
            sistema_seguimiento.dequeue()

        elif opcion == "3":
            # Consultar el primer producto
            producto = sistema_seguimiento.peek()
            if producto:
                print(f"El siguiente producto a procesar es: {producto}")

        elif opcion == "4":
            # Verificar si la cola está vacía
            if sistema_seguimiento.is_empty():
                print("La cola está vacía.")
            else:
                print("La cola no está vacía.")

        elif opcion == "5":
            # Consultar el número de productos en la cola
            print(f"El número de productos en la cola es: {sistema_seguimiento.size()}")

        elif opcion == "6":
            # Salir del programa
            print("Saliendo del sistema. ¡Gracias por usar Transporte Express!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

# Solo ejecutamos el menú si este archivo es el principal
if __name__ == "__main__":
    menu()