"""
Este archivo es una base para crear el SQL, usarlo de referencia

Creacion de la clase "Biblioteca" para crear
los objetos "libro", para almacenar en el vector "Libros = []"
y luego aplicar en la API web

Tiene varios parametros queda a conveniencia para agregar/quitar: 
codigo, autor, titulo, año, publicar, formato, portada
"""

# Clase Biblioteca, en lista "Libro=[]" se almacenan todos los objetos creados
class Biblioteca:
    # Atributo "Libros" para almacenamiento
    Libros = []

    # Método para buscar libro por código y titulo
    # "None" como parametro por defecto para buscar 
    def buscador_Libro(self,codigo=None,titulo=None):
        #Si el titulo es vacio (por defecto) busca por codigo
        if titulo == None: 
            for libro in self.Libros:
                if libro["codigo"] == codigo:
                    return libro
            return False
        else:
            for libro in self.Libros:
                if libro["titulo"] == titulo:
                    return libro
            return False
            
    # Método para agregar un libro nuevo
    def agregar_Libro(self, codigo, autor, titulo, año, publicar=False, formato=None, portada=None):
        # Verificamos que el código no esté en uso
        if self.buscador_Libro(codigo,titulo=None):
            return False
        
        # Diccionario que contiene los datos del libro    
        crear_libro = {
            "codigo": codigo,
            "autor": autor,
            "titulo": titulo,
            "año": año,
            "publicar": publicar,
            "formato": formato,
            "portada": portada,
        }

        # Agrega libro con los datos ingresados
        self.Libros.append(crear_libro)
        return True

    # Eliminar libro existente
    def eliminar_Libro(self, codigo):
        existente_libro = self.buscador_Libro(codigo,titulo=None)
        # Recibe un "True", de cumplirse procede a eliminar libro
        if existente_libro:
            self.Libros.remove(existente_libro)
            return True
        else:
            return False
        
    # Modificar libro existente
    def modificar_Libro(self, codigo, autor, titulo, año, publicar, formato, portada):
        existente_libro = self.buscador_Libro(codigo,titulo=None)
        # Elimina el libro existente (datos viejos) y crea uno de reemplazo (datos nuevos)
        if existente_libro:
            self.eliminar_Libro(codigo)
            self.agregar_Libro(codigo, autor, titulo, año, publicar, formato, portada)
            return True
        else:
            return False

    # Listar libros existentes
    def listar_Libro(self):
        print("Listado de libros catalogados / curación")
        print("-" * 10 + "\n")

        for libro in self.Libros:
            print(f"COD: {libro['codigo']}")
            print(f"AUT: {libro['autor']}")
            print(f"TIT: {libro['titulo']}")
            print(f"AÑO: {libro['año']}")
            print(f"EST: {libro['publicar']}")
            print(f"FOR: {libro['formato']}")
            print("-" * 10)

# Crear instancias de Biblioteca
Libro1 = Biblioteca()
Libro2 = Biblioteca()
Libro3 = Biblioteca()
Libro4 = Biblioteca()

#Algunos objetos creados a modo test

Libro1.agregar_Libro("001", "Gabriel García Márquez", "Cien años de soledad", 1967, True, "Impreso", "aqui la URL")
Libro2.agregar_Libro("002", "J.K. Rowling", "Harry Potter y la piedra filosofal", 1997, True, "Digital", "aqui la URL")
Libro3.agregar_Libro("003", "Stephen King", "It", 1986, True, "Impreso", "aqui la URL")
Libro4.agregar_Libro("004", "Jane Austen", "Orgullo y prejuicio", 1813, True, "Digital", "aqui la URL")

