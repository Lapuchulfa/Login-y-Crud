from contextlib import closing # closing es un administrador de contexto que garantiza que el cursor se cierre automáticamente después de su uso, incluso si ocurre una excepción durante la ejecución de la consulta.
from flask_login import UserMixin # es necesario para que la clase Usuario pueda ser utilizada con Flask-Login
from werkzeug.security import check_password_hash, generate_password_hash # es necesario para poder hashear la contraseña y verificarla

from database import database

class Usuario(UserMixin):
    def __init__(self, id, nombre, apellido, correo, password):
        self.id =id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.password = password
        
    def verificar_password(self, password):
        return check_password_hash(self.password, password)

def buscar_por_id(id_usuario):
    return _buscar_uno("Select * from usuario where ID_usuario = %s", (id_usuario,))

def buscar_por_correo(correo):
    return _buscar_uno("Select * from usuario where correo = %s", (correo,))

def crear(nombre, apellido, correo, password):
    with closing(database.cursor()) as cursor: # se utiliza closing para cerrar la conexion a la base de datos automaticamente al finalizar el bloque with
        cursor.execute( # se utiliza execute para ejecutar la consulta SQL, en este caso se utiliza un INSERT para agregar un nuevo usuario a la base de datos
            "Insert into usuario (Nombre, Apellido, correo, password) values (%s, %s, %s, %s)",
            (nombre, apellido, correo, generate_password_hash(password)),
        )
        database.commit() # se utiliza commit para guardar los cambios en la base de datos


def _buscar_uno(sql, parametros): # se utiliza para buscar un solo usuario en la base de datos, ya sea por id o por correo
    with closing(database.cursor(dictionary=True)) as cursor:
        cursor.execute(sql, parametros)
        fila = cursor.fetchone() # se utiliza fetchone para obtener una sola fila de la consulta, en este caso se espera que sea un solo usuario
        if fila is None:
            return None
        return Usuario(fila['ID_usuario'], fila['Nombre'], fila['Apellido'], fila['correo'],fila['password'])
    
     