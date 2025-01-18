# Este programa demuestra los conceptos básicos de Programación Orientada a Objetos (POO) en Python:
# 1. Herencia: La clase "Perro" hereda de la clase base "Animal".
# 2. Encapsulación: El atributo "__edad" de la clase "Animal" es privado, y solo puede ser accedido a través de un método público.
# 3. Polimorfismo: El método "hacer_sonido()" es sobrescrito en la clase "Perro", cambiando su comportamiento.
# El programa crea instancias de ambas clases y demuestra cómo funcionan estos conceptos.

# Clase base
class Animal:
    # Constructor para inicializar atributos
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo público
        self.__edad = edad  # Atributo privado (encapsulación)

    # Método para obtener la edad (encapsulación)
    def obtener_edad(self):
        return self.__edad

    # Método para hacer un sonido (será sobrescrito en la clase derivada)
    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido.")


# Clase derivada que hereda de Animal
class Perro(Animal):
    # Constructor que llama al constructor de la clase base
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.raza = raza  # Atributo específico de la clase Perro

    # Sobrescribir el método hacer_sonido
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Guau!")


# Instanciar objetos de las clases
animal1 = Animal("Bicho", 5)
perro1 = Perro("Rex", 3, "Labrador")

# Mostrar los sonidos que hacen los animales
animal1.hacer_sonido()  # Sonido del animal base
perro1.hacer_sonido()  # Sonido del perro (sobrescrito)

# Mostrar la edad del perro usando el método de la clase base
print(f"La edad de {perro1.nombre} es {perro1.obtener_edad()} años.")

# Mostrar los detalles del perro
print(f"{perro1.nombre} es un {perro1.raza}.")