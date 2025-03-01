import pickle
import os

# =============================================================================
# Documentación:
# Este programa implementa un sistema avanzado de gestión de inventario utilizando
# conceptos de Programación Orientada a Objetos (POO). Se utiliza la clase Producto
# para representar cada item del inventario y la clase Inventario para gestionar dichos
# productos mediante un diccionario, lo que permite una búsqueda rápida y un manejo
# eficiente de los datos.
#
# El almacenamiento persistente se implementa mediante la serialización del diccionario
# de productos usando el módulo pickle, permitiendo guardar y cargar el estado del
# inventario desde un archivo.
#
# Las colecciones (en este caso, un diccionario) se utilizan para:
#   - Almacenar los productos con el ID como clave.
#   - Permitir búsquedas y actualizaciones eficientes.
#
# El menú interactivo en la consola brinda opciones para agregar, eliminar, actualizar,
# buscar y mostrar productos, además de guardar y cargar el inventario.
# =============================================================================

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self._id = id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Métodos getter y setter para cada atributo
    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        self._cantidad = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        self._precio = valor

    def __str__(self):
        return f"ID: {self._id}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"


class Inventario:
    def __init__(self):
        # Usamos un diccionario para almacenar los productos:
        # clave -> ID del producto; valor -> instancia de Producto.
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print("El producto con este ID ya existe.")
        else:
            self.productos[producto.id] = producto
            print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado correctamente.")
        else:
            print("No se encontró un producto con ese ID.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if nueva_cantidad is not None:
                producto.cantidad = nueva_cantidad
            if nuevo_precio is not None:
                producto.precio = nuevo_precio
            print("Producto actualizado correctamente.")
        else:
            print("No se encontró un producto con ese ID.")

    def buscar_producto(self, nombre):
        # Búsqueda de productos que contengan el nombre (sin distinguir mayúsculas/minúsculas)
        encontrados = [prod for prod in self.productos.values() if nombre.lower() in prod.nombre.lower()]
        if encontrados:
            for prod in encontrados:
                print(prod)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    def guardar_inventario(self, archivo):
        # Serializamos el diccionario de productos y lo guardamos en un archivo.
        try:
            with open(archivo, "wb") as f:
                pickle.dump(self.productos, f)
            print("Inventario guardado correctamente.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def cargar_inventario(self, archivo):
        # Cargamos el diccionario de productos desde el archivo, si existe.
        if os.path.exists(archivo):
            try:
                with open(archivo, "rb") as f:
                    self.productos = pickle.load(f)
                print("Inventario cargado correctamente.")
            except Exception as e:
                print(f"Error al cargar el inventario: {e}")
        else:
            print("El archivo de inventario no existe. Se creará uno nuevo al guardar.")


def menu():
    inventario = Inventario()
    archivo = "inventario.dat"  # Archivo para almacenamiento persistente

    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Agregar nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar producto (cantidad/precio)")
        print("4. Buscar productos por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario en archivo")
        print("7. Cargar inventario desde archivo")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            try:
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
            except ValueError:
                print("Cantidad o precio inválidos. Intente nuevamente.")
                continue
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            print("Si no desea actualizar algún campo, déjelo en blanco.")
            nueva_cant_input = input("Ingrese la nueva cantidad: ")
            nuevo_precio_input = input("Ingrese el nuevo precio: ")

            nueva_cantidad = None
            nuevo_precio = None

            if nueva_cant_input:
                try:
                    nueva_cantidad = int(nueva_cant_input)
                except ValueError:
                    print("Cantidad inválida.")
                    continue

            if nuevo_precio_input:
                try:
                    nuevo_precio = float(nuevo_precio_input)
                except ValueError:
                    print("Precio inválido.")
                    continue

            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == "4":
            nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre_buscar)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            inventario.guardar_inventario(archivo)

        elif opcion == "7":
            inventario.cargar_inventario(archivo)

        elif opcion == "8":
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
