"""
Adaptacion de la clase "Biblioteca" con el conector MySQL para crear
los objetos "libro", para almacenar en el vector "Libros = []"
y luego aplicar en la API web

Faltan parametros que en la clase base si estan (BibliotecaClass.py)
Es mas corta, reducida a los siguientes parametros de libros:
- codigo - autor - titulo - portada
"""

"""
Se lista a continuacion los metodos para no estar buscando uno por uno:

# Constructor
def __init__(self,host,user,password,database):

# Nuevo libro - Metodo
def agregar_Libro(self,codigo,autor,titulo,portada):

    # Se tiene dos metodos para busqueda de libros
# Buscar libro codigo -Metodo
def buscarCODIGO_Libro(self,codigo):

# Buscar libro autor -Metodo
def buscarAUTOR_Libro(self,autor):

    # Se tienen dos metodos para eliminado de libros
# Eliminar libro codigo -Metodo
def eliminarCODIGO_Libro(self,codigo):

# Eliminar libro autor -Metodo (Eliminacion en masa)
def eliminarAUTOR_Libro(self,autor):
    
# Modificar libro -Metodo
def modificar_Libro(self,codigo,autor,titulo,portada):
    
# Mostrar libros - 1) Los datos de un libro 2) Toda la DB
def mostrarUNO_libro(self,codigo):
def mostrarTODOS_libro(self):
"""
import mysql.connector
from BibliotecaDBSQLcreator import creatorDBsql

# Importante, se asume que la tabla (no la base) se llama "libros"
# Importante, se asume que la base se llame "db_libromania"

# Revisar ajustes de conexion (conex).
# Revisar ajustes de cierre/apertura de cursor (cursor) en cada metodo.

class Biblioteca:

    # Constructor
    def __init__(self, host, user, password):
        #Contiene codigo duplicado - buscar solucion
        try:
            self.conex = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database='db_libromania'
            )
            self.cursor = self.conex.cursor()
            print("Conexion a base de datos exitosa.\n")

        except mysql.connector.Error as err:
            print(f"No es posible conectarse a la base de datos: {err}")
            print("Se procede a crear una base de datos.")
            creatorDBsql(host, user, password)        
            
            # Aqui arranca el codigo duplicado
            try:
                self.conex = mysql.connector.connect(
                    host=host,
                    user=user,
                    password=password,
                    database='db_libromania'
                )
                self.cursor = self.conex.cursor()
                print("Conexion a base de datos exitosa.\n")    
            
            except mysql.connector.Error as err:
                print(f"No es posible crear db o conectar: {err}.\n")
         
    # Nuevo libro - Metodo
    def agregar_Libro(self,autor,titulo,portada):
        insql = "INSERT INTO  libros (autor,titulo,portada) VALUES (%s,%s,%s)"
        inputLibro = (autor,titulo,portada)
        
        self.cursor.execute(insql,inputLibro)
        self.conex.commit()
        self.cursor.close() # Cierre de conexion
        return self.cursor.lastrowid

    # Se tiene dos metodos para busqueda de libros
    # Buscar libro codigo -Metodo
    def buscarCODIGO_Libro(self,codigo):
        self.cursor.execute(f"SELECT * FROM libros WHERE codigo = {codigo}")
        self.cursor.close()
        return self.cursor.fetchone()

    # Buscar libro autor -Metodo
    def buscarAUTOR_Libro(self,autor):
        self.cursor.execute(f"SELECT * FROM libros WHERE autor = {autor}")
        self.cursor.close()
        return self.cursor.fetchone()

    # Se tienen dos metodos para eliminado de libros
    # Eliminar libro codigo -Metodo
    def eliminarCODIGO_Libro(self,codigo):
        self.cursor.execute(f"DELETE FROM libros WHERE codigo = {codigo}")
        self.conex.commit()
        self.cursor.close()
        return self.cursor.rowcount > 0

    # Eliminar libro autor -Metodo (Eliminacion en masa)
    def eliminarAUTOR_Libro(self,autor):
        self.cursor.execute(f"DELETE FROM libros WHERE autor = {autor}")
        self.conex.commit()
        self.cursor.close()
        return self.cursor.rowcount > 0
    
    # Modificar libro -Metodo
    def modificar_Libro(self,codigo,autor,titulo,portada):
        sql = "UPDATE libros SET autor = %s, titulo = %s, portada = %s WHERE codigo = %s"
        actualizar = (autor,titulo,portada,codigo) 
        self.cursor.execute(sql,actualizar)
        self.conex.commit()
        self.cursor.close()
        return self.cursor.rowcount > 0
    
    # Mostrar libros - 1) Los datos de un libro 2) Toda la DB
    def mostrarUNO_libro(self,codigo):
        libro = self.buscarCODIGO_Libro(codigo)
        if libro:
            print("-" * 30)
            print("Datos solicitados")
            print("-" * 30)
            print(f"COD...... = {libro['codigo']}")
            print(f"AUTOR.... = {libro['autor']}")
            print(f"TITULO... = {libro['titulo']}")
            print(f"PORTADA.. = {libro['portada']}")
            print("-" * 30)
            print()
        else:
            print("Libro INEXISTENTE / NO encontrado.\n")

    def mostrarTODOS_libro(self):
        self.cursor.execute("SELECT * FROM libros")
        libros = self.cursor.fetchall()
        self.cursor.close()
        return libros
