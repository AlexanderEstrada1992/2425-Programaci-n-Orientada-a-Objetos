class Clima:
    def __init__(self, ciudad, semanas):
        # Almacena la información de la ciudad y las semanas
        self.ciudad = ciudad
        self.semanas = semanas  # Cada semana contiene una lista de días con temperatura

    def calcular_promedio(self):
        suma_temperaturas = 0
        total_dias = 0
        # Iterar sobre cada semana
        for semana in self.semanas:
            # Sumar las temperaturas de cada día en la semana
            for dia in semana:
                suma_temperaturas += dia["temp"]
                total_dias += 1
        # Calcular el promedio
        return suma_temperaturas / total_dias

def main():
    # Definir los datos de temperatura para cada ciudad y semana
    ciudades = [
        # Ciudad 1
        [
            [{"day": "Lunes", "temp": 78}, {"day": "Martes", "temp": 80}, {"day": "Miércoles", "temp": 82},
             {"day": "Jueves", "temp": 79}, {"day": "Viernes", "temp": 85}, {"day": "Sábado", "temp": 88}, {"day": "Domingo", "temp": 92}],
            [{"day": "Lunes", "temp": 76}, {"day": "Martes", "temp": 79}, {"day": "Miércoles", "temp": 83},
             {"day": "Jueves", "temp": 81}, {"day": "Viernes", "temp": 87}, {"day": "Sábado", "temp": 89}, {"day": "Domingo", "temp": 93}],
            [{"day": "Lunes", "temp": 77}, {"day": "Martes", "temp": 81}, {"day": "Miércoles", "temp": 85},
             {"day": "Jueves", "temp": 82}, {"day": "Viernes", "temp": 88}, {"day": "Sábado", "temp": 91}, {"day": "Domingo", "temp": 95}],
            [{"day": "Lunes", "temp": 75}, {"day": "Martes", "temp": 78}, {"day": "Miércoles", "temp": 80},
             {"day": "Jueves", "temp": 79}, {"day": "Viernes", "temp": 84}, {"day": "Sábado", "temp": 87}, {"day": "Domingo", "temp": 91}]
        ],
        # Ciudad 2
        [
            [{"day": "Lunes", "temp": 62}, {"day": "Martes", "temp": 64}, {"day": "Miércoles", "temp": 68},
             {"day": "Jueves", "temp": 70}, {"day": "Viernes", "temp": 73}, {"day": "Sábado", "temp": 75}, {"day": "Domingo", "temp": 79}],
            [{"day": "Lunes", "temp": 63}, {"day": "Martes", "temp": 66}, {"day": "Miércoles", "temp": 70},
             {"day": "Jueves", "temp": 72}, {"day": "Viernes", "temp": 75}, {"day": "Sábado", "temp": 77}, {"day": "Domingo", "temp": 81}],
            [{"day": "Lunes", "temp": 61}, {"day": "Martes", "temp": 65}, {"day": "Miércoles", "temp": 68},
             {"day": "Jueves", "temp": 70}, {"day": "Viernes", "temp": 72}, {"day": "Sábado", "temp": 76}, {"day": "Domingo", "temp": 80}],
            [{"day": "Lunes", "temp": 64}, {"day": "Martes", "temp": 67}, {"day": "Miércoles", "temp": 69},
             {"day": "Jueves", "temp": 71}, {"day": "Viernes", "temp": 74}, {"day": "Sábado", "temp": 77}, {"day": "Domingo", "temp": 80}]
        ],
        # Ciudad 3
        [
            [{"day": "Lunes", "temp": 90}, {"day": "Martes", "temp": 92}, {"day": "Miércoles", "temp": 94},
             {"day": "Jueves", "temp": 91}, {"day": "Viernes", "temp": 88}, {"day": "Sábado", "temp": 85}, {"day": "Domingo", "temp": 82}],
            [{"day": "Lunes", "temp": 89}, {"day": "Martes", "temp": 91}, {"day": "Miércoles", "temp": 93},
             {"day": "Jueves", "temp": 90}, {"day": "Viernes", "temp": 87}, {"day": "Sábado", "temp": 84}, {"day": "Domingo", "temp": 81}],
            [{"day": "Lunes", "temp": 91}, {"day": "Martes", "temp": 93}, {"day": "Miércoles", "temp": 95},
             {"day": "Jueves", "temp": 92}, {"day": "Viernes", "temp": 89}, {"day": "Sábado", "temp": 86}, {"day": "Domingo", "temp": 83}],
            [{"day": "Lunes", "temp": 88}, {"day": "Martes", "temp": 90}, {"day": "Miércoles", "temp": 92},
             {"day": "Jueves", "temp": 89}, {"day": "Viernes", "temp": 86}, {"day": "Sábado", "temp": 83}, {"day": "Domingo", "temp": 80}]
        ]
    ]

    while True:
        print("Seleccione una ciudad:")
        print("1 - Ciudad 1")
        print("2 - Ciudad 2")
        print("3 - Ciudad 3")
        print("4 - Salir")

        opcion = input("Ingrese la opción: ")
        if opcion == "1":
            clima = Clima(ciudad="Ciudad 1", semanas=ciudades[0])
            promedio = clima.calcular_promedio()
            print(f'Promedio de temperatura para Ciudad 1: {promedio:.2f}')
        elif opcion == "2":
            clima = Clima(ciudad="Ciudad 2", semanas=ciudades[1])
            promedio = clima.calcular_promedio()
            print(f'Promedio de temperatura para Ciudad 2: {promedio:.2f}')
        elif opcion == "3":
            clima = Clima(ciudad="Ciudad 3", semanas=ciudades[2])
            promedio = clima.calcular_promedio()
            print(f'Promedio de temperatura para Ciudad 3: {promedio:.2f}')
        elif opcion == "4":
            break
        else:
            print("Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    main()