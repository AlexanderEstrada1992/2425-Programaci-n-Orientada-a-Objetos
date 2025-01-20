# Este programa simula la gestión de un archivo utilizando clases en Python.
# Utiliza un constructor (__init__) para abrir un archivo en modo escritura y un destructor (__del__)
# para cerrarlo correctamente al finalizar su uso. El objetivo es demostrar cómo se usan los constructores
# y destructores en Python, asegurando que los recursos se gestionen adecuadamente durante la ejecución.

class Archivo:
    def __init__(self, nombre_archivo):
        """
        Constructor de la clase. Se llama al crear una instancia de la clase.
        Inicializa el nombre del archivo y abre el archivo en modo escritura.
        """
        self.nombre_archivo = nombre_archivo
        try:
            self.archivo = open(self.nombre_archivo, 'w')  # Abre el archivo en modo escritura
            print(f"Archivo '{self.nombre_archivo}' abierto correctamente.")
        except Exception as e:
            print(f"Error al abrir el archivo: {e}")
            self.archivo = None

    def escribir(self, contenido):
        """
        Método para escribir contenido en el archivo.
        Solo escribe si el archivo fue abierto correctamente.
        """
        if self.archivo:
            self.archivo.write(contenido)
            print(f"Contenido escrito en el archivo '{self.nombre_archivo}'.")
        else:
            print("El archivo no está abierto. No se puede escribir.")

    def __del__(self):
        """
        Destructor de la clase. Se llama al eliminar la instancia de la clase o al final del programa.
        Cierra el archivo si está abierto.
        """
        if hasattr(self, 'archivo') and self.archivo:
            self.archivo.close()
            print(f"Archivo '{self.nombre_archivo}' cerrado correctamente.")
        else:
            print("No hay archivo abierto que cerrar.")

# Crear una instancia de la clase Archivo
archivo1 = Archivo('ejemplo.txt')

# Escribir contenido en el archivo
archivo1.escribir("Hola, este es un archivo de ejemplo.\n")

# Al finalizar el programa, el archivo se cierra automáticamente gracias al destructor
