import os
import json


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

    def to_dict(self):
        return {"id_producto": self.id_producto, "nombre": self.nombre, "cantidad": self.cantidad,
                "precio": self.precio}


class Inventario:
    FILE_NAME = "inventario.txt"

    def __init__(self):
        self.productos = []
        self.cargar_inventario()

    def guardar_inventario(self):
        try:
            with open(self.FILE_NAME, "w") as f:
                json.dump([p.to_dict() for p in self.productos], f, indent=4)
        except PermissionError:
            print("⚠️ Error: No se tienen permisos para escribir en el archivo.")
        except Exception as e:
            print(f"⚠️ Error inesperado al guardar el inventario: {e}")

    def cargar_inventario(self):
        if not os.path.exists(self.FILE_NAME):
            return
        try:
            with open(self.FILE_NAME, "r") as f:
                datos = json.load(f)
                self.productos = [Producto(**d) for d in datos]
        except FileNotFoundError:
            print("⚠️ Archivo de inventario no encontrado. Se creará uno nuevo.")
        except json.JSONDecodeError:
            print("⚠️ Error al leer el archivo de inventario. Puede estar corrupto.")
        except Exception as e:
            print(f"⚠️ Error inesperado al cargar el inventario: {e}")

    def agregar_producto(self, producto):
        if any(p.id_producto == producto.id_producto for p in self.productos):
            print("⚠️ Error: El ID ya existe en el inventario.")
            return
        self.productos.append(producto)
        self.guardar_inventario()
        print("✅ Producto agregado con éxito.")

    def eliminar_producto(self, id_producto):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                self.productos.remove(producto)
                self.guardar_inventario()
                print("✅ Producto eliminado correctamente.")
                return
        print("⚠️ Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                self.guardar_inventario()
                print("✅ Producto actualizado correctamente.")
                return
        print("⚠️ Error: Producto no encontrado.")

    def mostrar_inventario(self):
        if not self.productos:
            print("📭 Inventario vacío.")
        else:
            for producto in self.productos:
                print(producto)


def menu():
    inventario = Inventario()

    while True:
        print("\n📦 Sistema de Gestión de Inventarios 📦")
        print("1️⃣ Agregar producto")
        print("2️⃣ Eliminar producto")
        print("3️⃣ Actualizar producto")
        print("4️⃣ Mostrar inventario")
        print("5️⃣ Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_producto = int(input("Ingrese ID del producto: "))
                nombre = input("Ingrese nombre del producto: ")
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("⚠️ Error: Ingrese valores numéricos válidos para ID, cantidad y precio.")

        elif opcion == "2":
            try:
                id_producto = int(input("Ingrese ID del producto a eliminar: "))
                inventario.eliminar_producto(id_producto)
            except ValueError:
                print("⚠️ Error: Ingrese un ID válido.")

        elif opcion == "3":
            try:
                id_producto = int(input("Ingrese ID del producto a actualizar: "))
                cantidad = input("Nueva cantidad (presione Enter para omitir): ")
                precio = input("Nuevo precio (presione Enter para omitir): ")
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualizar_producto(id_producto, cantidad, precio)
            except ValueError:
                print("⚠️ Error: Ingrese valores numéricos válidos.")

        elif opcion == "4":
            inventario.mostrar_inventario()

        elif opcion == "5":
            print("👋 Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("⚠️ Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
