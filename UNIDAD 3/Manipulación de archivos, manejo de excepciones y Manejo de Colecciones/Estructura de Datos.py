class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """Constructor de la clase Producto que inicializa sus atributos."""
        self.id_producto = id_producto  # Identificador único para cada producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad disponible en el inventario
        self.precio = precio  # Precio unitario del producto

    def __str__(self):
        """Método especial para representar el objeto Producto como una cadena de texto."""
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

    # Métodos Getters: permiten acceder a los atributos privados de la clase
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Métodos Setters: permiten modificar atributos específicos del producto
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio


class Inventario:
    def __init__(self):
        """Constructor de la clase Inventario que inicializa una lista vacía de productos."""
        self.productos = []  # Lista donde se almacenarán los productos

    def agregar_producto(self, producto):
        """Añade un producto al inventario si el ID es único."""
        # Verifica que el ID del nuevo producto no exista en el inventario
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("⚠️ Error: El ID ya existe en el inventario.")
            return
        self.productos.append(producto)
        print("✅ Producto agregado con éxito.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario según su ID."""
        for producto in self.productos:
            if producto.get_id() == id_producto:
                self.productos.remove(producto)
                print("✅ Producto eliminado correctamente.")
                return
        print("⚠️ Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualiza la cantidad o el precio de un producto dado su ID."""
        for producto in self.productos:
            if producto.get_id() == id_producto:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)  # Actualiza la cantidad si se proporciona un valor
                if precio is not None:
                    producto.set_precio(precio)  # Actualiza el precio si se proporciona un valor
                print("✅ Producto actualizado correctamente.")
                return
        print("⚠️ Error: Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        """Busca productos en el inventario cuyo nombre contenga la cadena ingresada."""
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("⚠️ No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("📭 Inventario vacío.")
        else:
            for producto in self.productos:
                print(producto)


def menu():
    """Función principal que maneja la interacción con el usuario."""
    inventario = Inventario()  # Se crea un objeto Inventario

    while True:
        # Se muestra el menú de opciones
        print("\n📦 Sistema de Gestión de Inventarios 📦")
        print("1️⃣ Agregar producto")
        print("2️⃣ Eliminar producto")
        print("3️⃣ Actualizar producto")
        print("4️⃣ Buscar producto por nombre")
        print("5️⃣ Mostrar inventario")
        print("6️⃣ Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Entrada de datos para crear un nuevo producto
            id_producto = int(input("Ingrese ID del producto: "))
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)  # Creación del objeto Producto
            inventario.agregar_producto(producto)  # Se agrega el producto al inventario

        elif opcion == "2":
            id_producto = int(input("Ingrese ID del producto a eliminar: "))
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = int(input("Ingrese ID del producto a actualizar: "))
            cantidad = input("Nueva cantidad (presione Enter para omitir): ")
            precio = input("Nuevo precio (presione Enter para omitir): ")
            cantidad = int(cantidad) if cantidad else None  # Se convierte la cantidad a entero si no está vacía
            precio = float(precio) if precio else None  # Se convierte el precio a flotante si no está vacío
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            print("👋 Saliendo del sistema. ¡Hasta luego!")
            break  # Se termina el ciclo y el programa finaliza

        else:
            print("⚠️ Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()  # Se ejecuta la función principal
