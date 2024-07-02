"""
Aqui lo relacionado para generar las plantillas de flask
Se busca vincular "BibliotecaClassSQL.py" con este archivo
para no estar reescribiendo codigo

Se busca evitar que sea ilegible el producto final
"""

from BibliotecaClassSQL import *
from flask import Flask, jsonify, request

app = Flask(__name__)

biblioteca = Biblioteca(
    host='localhost', 
    user='usuario',
    password='contraseña', 
    database='nombre_basedatos'
    )
 #Continuara...


