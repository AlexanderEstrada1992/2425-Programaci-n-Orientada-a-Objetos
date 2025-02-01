import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'UNIDAD 1/Comparación de Programación Tradicional y POO en Python/Programación Orientada a Objetos (POO).py',
        '2': 'UNIDAD 1/Comparación de Programación Tradicional y POO en Python/Programación Tradicional.py',
        '3': 'UNIDAD 1/EjemplosMundoReal_POO/EjemplosMundoReal_POO.py',
        '4': 'UNIDAD 1/Tipos de datos, Identificadores/Tipos de datos, Identificadores.py',
        '5': 'UNIDAD 1/1.2 Tecnicas de Programacion.py',
        '6': 'UNIDAD 2/Aplicación de Conceptos de POO en Python/Ejemplo de Clases, objetos, herencia, encapsulamiento y polimorfismo.py',
        '7': 'UNIDAD 2/Constructores y destructores/Ejemplo con constructores y destructores.pY',

        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\n********Menu Principal - Dashboard*************")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()