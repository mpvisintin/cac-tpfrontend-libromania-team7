"""
Esto es un menu de prueba para trabajar por consola
Comprueba que esten funcionando todos los metodos de la clase "Biblioteca"
ubicada en el archivo "BibliotecaClass.py"

Dedique mas tiempo de mi vida a este menu de prueba que a la clase
"""

# Importar la clase Biblioteca desde el archivo BibliotecaClass.py
from BibliotecaClass import Biblioteca

print("\nBienvenido al sistema de gestión de libros\n")

# Función para mostrar el menú de opciones
def mostrar_menu():
    print("1. Agregar libro")
    print("2. Buscar libro por código")
    print("3. Buscar libro por título")
    print("4. Eliminar libro")
    print("5. Modificar libro")
    print("6. Listar todos los libros")
    print("7. Salir\n")

# Función para agregar un libro
def agregar_libro(conjuntolibros):
    print("Ingrese los datos del libro a agregar:")
    codigo = input("Código: ")
    
    if conjuntolibros.buscador_Libro(codigo=codigo):  # Mini seguro
        print("\nERROR - Código existente.\n")
        return

    autor = input("Autor: ")
    titulo = input("Título: ")
    año = int(input("Año de publicación: "))
    publicado = input("¿Está publicado? (Sí/No): ").lower() == 'sí'
    formato = input("Formato: ")
    portada = input("Portada: ")

    resultado = conjuntolibros.agregar_Libro(codigo, autor, titulo, año, publicado, formato, portada)
    if resultado:
        print("Libro agregado correctamente.")
    else:
        print("Error al agregar el libro.")

# Función para buscar un libro por código
def buscar_libro_codigo(conjuntolibros):
    codigo = input("Ingrese el código del libro: ")
    libro = conjuntolibros.buscador_Libro(codigo=codigo)
    if libro:
        print("Libro encontrado:")
        print(f"Código: {libro['codigo']}")
        print(f"Autor: {libro['autor']}")
        print(f"Título: {libro['titulo']}")
        print(f"Año: {libro['año']}")
        print(f"Publicado: {libro['publicar']}")
        print(f"Formato: {libro['formato']}")
        print(f"Portada: {libro['portada']}")
    else:
        print("Libro no encontrado.")

# Función para buscar un libro por título
def buscar_libro_titulo(conjuntolibros):
    titulo = input("Ingrese el título del libro: ")
    libro = conjuntolibros.buscador_Libro(titulo=titulo)
    if libro:
        print("Libro encontrado:")
        print(f"Código: {libro['codigo']}")
        print(f"Autor: {libro['autor']}")
        print(f"Título: {libro['titulo']}")
        print(f"Año: {libro['año']}")
        print(f"Publicado: {libro['publicar']}")
        print(f"Formato: {libro['formato']}")
        print(f"Portada: {libro['portada']}")
    else:
        print("Libro no encontrado.")

# Función para eliminar un libro
def eliminar_libro(conjuntolibros):
    codigo = input("Ingrese el código del libro a eliminar: ")
    resultado = conjuntolibros.eliminar_Libro(codigo)
    if resultado:
        print("Libro eliminado correctamente.")
    else:
        print("Error al eliminar el libro. Verifique el código.")

# Función para modificar un libro
def modificar_libro(conjuntolibros):
    print("Ingrese los nuevos datos del libro:")
    codigo = input("Código del libro a modificar: ")
    autor = input("Nuevo autor: ")
    titulo = input("Nuevo título: ")
    año = int(input("Nuevo año de publicación: "))
    publicado = input("¿Está publicado? (Sí/No): ").lower() == 'sí'
    formato = input("Nuevo formato: ")
    portada = input("Nueva portada: ")

    resultado = conjuntolibros.modificar_Libro(codigo, autor, titulo, año, publicado, formato, portada)
    if resultado:
        print("Libro modificado correctamente.")
    else:
        print("Error al modificar el libro. Verifique el código.")

# Función para listar todos los libros
def listar_libros(conjuntolibros):
    print("Listado de libros:")
    conjuntolibros.listar_Libro()

# Función principal para ejecutar el programa
def main():
    #Instanciado
    conjuntolibros = Biblioteca() 
    
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción que desea realizar (1-7): ")

        if opcion == '1':
            agregar_libro(conjuntolibros)
        elif opcion == '2':
            buscar_libro_codigo(conjuntolibros)
        elif opcion == '3':
            buscar_libro_titulo(conjuntolibros)
        elif opcion == '4':
            eliminar_libro(conjuntolibros)
        elif opcion == '5':
            modificar_libro(conjuntolibros)
        elif opcion == '6':
            listar_libros(conjuntolibros)
        elif opcion == '7':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()

