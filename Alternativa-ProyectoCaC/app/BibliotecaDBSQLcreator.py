"""
Este es un creador de base de datos
Por defecto creara la base "db_libromania"

El creador se insertara en el -constructor init- de "BibliotecaClassSQL.py"
se busca reducir la cantidad de lineas realizando este modulo.

Ir a la ultima linea y utilizar los valores configurados en sus PC
Ponele -play- y verifica si se creo en tu propia consola o GUI dedicado (esto no se importa solo la funcion)
"""

import mysql.connector

def creatorDBsql(host,user,password):
    
    print("/n","-"*30)
    print("Creacion de base de datos 'db_libromania'.\n")

    # Conexion a MySQL - Creacion de cursor
    conex = mysql.connector.connect(
        host = host,
        user = user, 
        password = password
    )

    cursor = conex.cursor()

    # Creacion de base "db_libromania"
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS db_libromania")
    print("Base de datos 'db_libromania' creada.\n")

    # Conexion a la base "db_libromania"
    conex = mysql.connector.connect(
        host = host,
        user = user, 
        password = password,
        database = 'db_libromania'
    )

    cursor = conex.cursor()

    # Creacion tabla
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS libros (
        Codigo INT AUTO_INCREMENT PRIMARY KEY,
        Autor VARCHAR(255) NOT NULL,
        Titulo VARCHAR(255) NOT NULL,
        Portada VARCHAR(255)
        )
    """)
    print("Tabla 'libros' creada.\n")

    # Insercion libros por defecto

    libros_test = [
        ('Gabriel García Márquez', 'Cien años de soledad', 'aqui url al png'),
        ('J.K. Rowling', 'Harry Potter y la piedra filosofal', 'aqui url al png'),
        ('F. Scott Fitzgerald', 'El gran Gatsby', 'aqui url al png')
    ]

    insql = "INSERT INTO libros (Autor, Titulo, Portada) VALUES (%s, %s, %s)"
    cursor.executemany(insql,libros_test)
    conex.commit()
    
    print("Libros por defecto insertados.\n")
    print("-"*30,"\n")    

    # Cierre conexiones provisorias
    cursor.close()
    conex.close()

creatorDBsql("localhost","root","0000")