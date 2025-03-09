#Desarrollar un sistema para gestionar una biblioteca digital. El sistema permitirá administrar los libros disponibles,
# las categorías de libros, los usuarios registrados y el historial de préstamos.
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla para título y autor (inmutables)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} de {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"


class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario ISBN -> Objeto Libro
        self.usuarios_registrados = set()  # Conjunto de IDs de usuarios únicos
        self.historial_prestamos = {}  # Diccionario user_id -> lista de libros prestados

    def agregar_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro
        print(f"Libro agregado: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("El libro no existe en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.user_id in self.usuarios_registrados:
            print("Este usuario ya está registrado.")
        else:
            self.usuarios_registrados.add(usuario.user_id)
            self.historial_prestamos[usuario.user_id] = []
            print(f"Usuario registrado: {usuario}")

    def dar_de_baja_usuario(self, user_id):
        if user_id in self.usuarios_registrados:
            self.usuarios_registrados.remove(user_id)
            del self.historial_prestamos[user_id]
            print(f"Usuario con ID {user_id} dado de baja.")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, user_id, isbn):
        if user_id not in self.usuarios_registrados:
            print("Usuario no registrado.")
            return
        if isbn not in self.libros_disponibles:
            print("Libro no disponible.")
            return
        libro = self.libros_disponibles.pop(isbn)  # Quita el libro del diccionario
        self.historial_prestamos[user_id].append(libro)
        print(f"Libro prestado: {libro} a usuario {user_id}")

    def devolver_libro(self, user_id, isbn):
        if user_id not in self.usuarios_registrados:
            print("Usuario no registrado.")
            return
        libros_prestados = self.historial_prestamos[user_id]
        for libro in libros_prestados:
            if libro.isbn == isbn:
                libros_prestados.remove(libro)
                self.libros_disponibles[isbn] = libro  # Regresa el libro a la biblioteca
                print(f"Libro devuelto: {libro}")
                return
        print("El usuario no tiene este libro prestado.")

    def buscar_libro(self, clave):
        resultados = [libro for libro in self.libros_disponibles.values()
                      if clave.lower() in libro.info[0].lower() or clave.lower() in libro.info[1].lower() or clave.lower() in libro.categoria.lower()]
        if resultados:
            print("Libros encontrados:")
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros.")

    def listar_libros_prestados(self, user_id):
        if user_id in self.historial_prestamos:
            libros = self.historial_prestamos[user_id]
            if libros:
                print(f"Libros prestados al usuario {user_id}:")
                for libro in libros:
                    print(libro)
            else:
                print("El usuario no tiene libros prestados.")
        else:
            print("Usuario no registrado.")


# Ejemplo de uso
biblioteca = Biblioteca()

libro1 = Libro("1984", "George Orwell", "Ficción", "20578")
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "Infantil", "12345")

usuario1 = Usuario("Juan Pérez", "U001")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

biblioteca.registrar_usuario(usuario1)
biblioteca.prestar_libro("U001", "20578")
biblioteca.listar_libros_prestados("U001")
biblioteca.devolver_libro("U001", "20578")
biblioteca.listar_libros_prestados("U001")
