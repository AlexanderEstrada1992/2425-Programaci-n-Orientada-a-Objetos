# Clase Libro: Representa un libro en la biblioteca
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Atributos inmutables: Titulo y Autor son tuplas
        self.titulo = titulo
        self.autor = autor  # (nombre_autor, apellido_autor)
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"Libro({self.titulo}, {self.autor}, {self.categoria}, {self.isbn})"


# Clase Usuario: Representa a un usuario de la biblioteca
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros actualmente prestados al usuario

    def __repr__(self):
        return f"Usuario({self.nombre}, {self.id_usuario}, {self.libros_prestados})"


# Clase Biblioteca: Gestiona libros, usuarios y préstamos
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y Libro como valor
        self.usuarios = set()  # Conjunto de IDs de usuarios únicos

    # Añadir un libro a la biblioteca
    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' agregado exitosamente.")
        else:
            print(f"El libro '{libro.titulo}' ya existe en la biblioteca.")

    # Eliminar un libro de la biblioteca
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado exitosamente.")
        else:
            print(f"El libro con ISBN {isbn} no existe.")

    # Registrar un nuevo usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in [u.id_usuario for u in self.usuarios]:
            self.usuarios.add(usuario)
            print(f"Usuario '{usuario.nombre}' registrado exitosamente.")
        else:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")

    # Dar de baja un usuario
    def dar_baja_usuario(self, id_usuario):
        usuario_a_baja = None
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                usuario_a_baja = usuario
                break
        if usuario_a_baja:
            self.usuarios.remove(usuario_a_baja)
            print(f"Usuario con ID {id_usuario} dado de baja exitosamente.")
        else:
            print(f"No se encontró un usuario con ID {id_usuario}.")

    # Prestar un libro a un usuario
    def prestar_libro(self, id_usuario, isbn):
        usuario = self.buscar_usuario(id_usuario)
        if usuario and isbn in self.libros:
            libro = self.libros[isbn]
            if libro not in usuario.libros_prestados:
                usuario.libros_prestados.append(libro)
                print(f"Libro '{libro.titulo}' prestado a '{usuario.nombre}'.")
            else:
                print(f"El usuario '{usuario.nombre}' ya tiene prestado el libro '{libro.titulo}'.")
        else:
            print("Usuario o libro no encontrado.")

    # Devolver un libro
    def devolver_libro(self, id_usuario, isbn):
        usuario = self.buscar_usuario(id_usuario)
        if usuario:
            libro = self.buscar_libro(isbn)
            if libro in usuario.libros_prestados:
                usuario.libros_prestados.remove(libro)
                print(f"Libro '{libro.titulo}' devuelto por '{usuario.nombre}'.")
            else:
                print(f"El usuario '{usuario.nombre}' no tiene prestado el libro '{libro.titulo}'.")
        else:
            print("Usuario no encontrado.")

    # Buscar un libro por título, autor o categoría
    def buscar_libro(self, busqueda):
        libros_encontrados = [libro for libro in self.libros.values()
                              if busqueda.lower() in libro.titulo.lower() or
                              busqueda.lower() in libro.autor[0].lower() or
                              busqueda.lower() in libro.categoria.lower()]
        return libros_encontrados

    # Buscar un usuario por ID
    def buscar_usuario(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None

    # Listar los libros prestados a un usuario
    def listar_libros_prestados(self, id_usuario):
        usuario = self.buscar_usuario(id_usuario)
        if usuario:
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(f"- {libro.titulo} de {libro.autor[0]}")
            else:
                print(f"El usuario '{usuario.nombre}' no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")


# Creación de objetos y prueba del sistema
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("El Quijote", ("Miguel", "de Cervantes"), "Ficción", "12345")
libro2 = Libro("Cien Años de Soledad", ("Gabriel", "García Márquez"), "Realismo Mágico", "67890")

# Crear usuarios
usuario1 = Usuario("Juan Pérez", "U001")
usuario2 = Usuario("María López", "U002")

# Registrar usuarios en la biblioteca
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Agregar libros a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Prestar libros
biblioteca.prestar_libro("U001", "12345")
biblioteca.prestar_libro("U002", "67890")

# Listar libros prestados
biblioteca.listar_libros_prestados("U001")
biblioteca.listar_libros_prestados("U002")

# Devolver libros
biblioteca.devolver_libro("U001", "12345")
biblioteca.devolver_libro("U002", "67890")

# Buscar libros
print(biblioteca.buscar_libro("Quijote"))
print(biblioteca.buscar_libro("García"))

# Eliminar libro
biblioteca.quitar_libro("12345")
