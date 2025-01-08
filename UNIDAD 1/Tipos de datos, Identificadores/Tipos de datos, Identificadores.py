# Programa para calcular el área y el perímetro de un rectángulo
# Este programa permite al usuario ingresar las dimensiones de un rectángulo y calcula tanto su área como su perímetro.

# Funciones para los cálculos
def calcular_area(base, altura):
    """
    Calcula el área de un rectángulo.
    :param base: Base del rectángulo (float)
    :param altura: Altura del rectángulo (float)
    :return: Área del rectángulo (float)
    """
    return base * altura

def calcular_perimetro(base, altura):
    """
    Calcula el perímetro de un rectángulo.
    :param base: Base del rectángulo (float)
    :param altura: Altura del rectángulo (float)
    :return: Perímetro del rectángulo (float)
    """
    return 2 * (base + altura)

# Solicitar al usuario las dimensiones del rectángulo
print("Calculadora de área y perímetro de un rectángulo")

# Capturar la base del rectángulo
base = float(input("Ingrese la base del rectángulo en unidades: "))

# Capturar la altura del rectángulo
altura = float(input("Ingrese la altura del rectángulo en unidades: "))

# Verificar que las dimensiones sean positivas
if base > 0 and altura > 0:
    # Calcular el área y el perímetro
    area = calcular_area(base, altura)
    perimetro = calcular_perimetro(base, altura)

    # Mostrar los resultados
    print(f"\nResultados:")
    print(f"- Área: {area} unidades cuadradas")
    print(f"- Perímetro: {perimetro} unidades")
else:
    print("\nError: La base y la altura deben ser valores positivos.")