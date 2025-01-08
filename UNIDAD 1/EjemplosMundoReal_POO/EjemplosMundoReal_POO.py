# Sistema de Reservas de Hotel usando Programación Orientada a Objetos

class Habitacion:
    """
    Clase que representa una habitación de un hotel.
    """
    def __init__(self, numero, tipo, precio):
        self.numero = numero  # Número de la habitación
        self.tipo = tipo      # Tipo de habitación (simple, doble, suite)
        self.precio = precio  # Precio por noche
        self.ocupada = False  # Estado de la habitación (True si está ocupada, False si está libre)

    def ocupar(self):
        """Marca la habitación como ocupada."""
        if not self.ocupada:
            self.ocupada = True
            return True
        return False

    def liberar(self):
        """Marca la habitación como libre."""
        if self.ocupada:
            self.ocupada = False
            return True
        return False

class Cliente:
    """
    Clase que representa un cliente del hotel.
    """
    def __init__(self, nombre, identificacion):
        self.nombre = nombre              # Nombre del cliente
        self.identificacion = identificacion  # Documento de identificación del cliente

class Reserva:
    """
    Clase que representa una reserva de hotel.
    """
    def __init__(self, cliente, habitacion, noches):
        self.cliente = cliente            # Cliente asociado a la reserva
        self.habitacion = habitacion      # Habitación reservada
        self.noches = noches              # Número de noches de la reserva
        self.costo_total = self.calcular_costo()

    def calcular_costo(self):
        """Calcula el costo total de la reserva."""
        return self.habitacion.precio * self.noches

class Hotel:
    """
    Clase que representa un hotel con habitaciones y reservas.
    """
    def __init__(self, nombre):
        self.nombre = nombre               # Nombre del hotel
        self.habitaciones = []             # Lista de habitaciones disponibles
        self.reservas = []                 # Lista de reservas realizadas

    def agregar_habitacion(self, habitacion):
        """Agrega una habitación a la lista del hotel."""
        self.habitaciones.append(habitacion)

    def buscar_habitacion_disponible(self, tipo):
        """Busca una habitación disponible por tipo."""
        for habitacion in self.habitaciones:
            if habitacion.tipo == tipo and not habitacion.ocupada:
                return habitacion
        return None

    def realizar_reserva(self, cliente, tipo_habitacion, noches):
        """Realiza una reserva si hay una habitación disponible."""
        habitacion = self.buscar_habitacion_disponible(tipo_habitacion)
        if habitacion:
            if habitacion.ocupar():
                reserva = Reserva(cliente, habitacion, noches)
                self.reservas.append(reserva)
                return reserva
        return None

# Ejemplo de uso del sistema

# Crear un hotel
hotel = Hotel("Hotel Paradiso")

# Agregar habitaciones al hotel
hotel.agregar_habitacion(Habitacion(101, "simple", 50))
hotel.agregar_habitacion(Habitacion(102, "doble", 80))
hotel.agregar_habitacion(Habitacion(103, "suite", 150))

# Crear un cliente
cliente = Cliente("Juan Perez", "1234567890")

# Realizar una reserva
reserva = hotel.realizar_reserva(cliente, "doble", 3)

if reserva:
    print(f"Reserva realizada con éxito para {reserva.cliente.nombre}.")
    print(f"Habitación: {reserva.habitacion.numero}")
    print(f"Costo total: ${reserva.costo_total}")
else:
    print("No hay habitaciones disponibles del tipo solicitado.")