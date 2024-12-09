# Abstracción: Crear clases y métodos que simplifican interacciones y se centran en lo esencial.
# Este ejemplo usa una nueva clase abstracta que define el esquema base de un personaje.

from abc import ABC, abstractmethod

class PersonajeBase(ABC):  # Clase abstracta que actúa como plantilla para personajes
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    @abstractmethod
    def atributos(self):  # Método abstracto, cada subclase debe implementarlo
        pass

    def esta_vivo(self):
        return self.vida > 0

    @abstractmethod
    def atacar(self, enemigo):  # Método abstracto para realizar ataques
        pass

# Encapsulación: Ocultar detalles internos de las clases y exponer solo lo necesario.
class Guerrero(PersonajeBase):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.__espada = espada  # Atributo encapsulado

    def atributos(self):
        print(f"{self.nombre}:")
        print(f"· Fuerza: {self.fuerza}")
        print(f"· Inteligencia: {self.inteligencia}")
        print(f"· Defensa: {self.defensa}")
        print(f"· Vida: {self.vida}")
        print(f"· Espada: {self.__espada}")

    def cambiar_espada(self, nuevo_daño):
        if 5 <= nuevo_daño <= 15:  # Validación interna
            self.__espada = nuevo_daño
        else:
            print("El daño de la espada no es válido")

    def atacar(self, enemigo):
        daño = self.fuerza * self.__espada - enemigo.defensa
        enemigo.vida -= daño
        print(f"{self.nombre} atacó a {enemigo.nombre} causando {daño} puntos de daño.")

# Herencia: Reutilizar y extender código mediante subclases.
class Mago(PersonajeBase):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        print(f"{self.nombre}:")
        print(f"· Fuerza: {self.fuerza}")
        print(f"· Inteligencia: {self.inteligencia}")
        print(f"· Defensa: {self.defensa}")
        print(f"· Vida: {self.vida}")
        print(f"· Libro: {self.libro}")

    def atacar(self, enemigo):
        daño = self.inteligencia * self.libro - enemigo.defensa
        enemigo.vida -= daño
        print(f"{self.nombre} atacó a {enemigo.nombre} causando {daño} puntos de daño.")

# Polimorfismo: Habilidad para usar métodos compartidos entre objetos de diferentes tipos.
def mostrar_atributos(personaje):
    personaje.atributos()

# Crear objetos de tipo Guerrero y Mago.
guerrero = Guerrero("Arthur", 20, 5, 10, 100, 8)
mago = Mago("Merlín", 10, 30, 5, 80, 3)

# Mostrar atributos usando polimorfismo.
mostrar_atributos(guerrero)
mostrar_atributos(mago)

# Simular un ataque.
guerrero.atacar(mago)
mago.atacar(guerrero)