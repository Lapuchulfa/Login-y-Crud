from contextlib import closing # closing es un administrador de contexto que garantiza que el cursor se cierre automáticamente después de su uso, incluso si ocurre una excepción durante la ejecución de la consulta.

from database import database


def obtener_todos():
    with closing(database.cursor(dictionary=True)) as cursor: # dictionary=True hace que el cursor devuelva los resultados como diccionarios en lugar de tuplas, lo que facilita el acceso a los datos por nombre de columna. 
        cursor.execute("SELECT * FROM producto")
        return cursor.fetchall() # fetchall() devuelve todas las filas de la consulta como una lista de diccionarios, donde cada diccionario representa una fila de la tabla producto.


def crear(nombre, categoria, precio):
    _ejecutar_cambio(
        "INSERT INTO producto (Nombre_Producto, Categoria_Producto, Precio) VALUES (%s, %s, %s)",
        (nombre, categoria, precio),
    )


def actualizar(id_producto, nombre, categoria, precio):
    _ejecutar_cambio(
        "UPDATE producto SET Nombre_Producto = %s, Categoria_Producto = %s, Precio = %s WHERE ID_Producto = %s",
        (nombre, categoria, precio, id_producto),
    )


def eliminar(id_producto):
    _ejecutar_cambio("DELETE FROM producto WHERE ID_Producto = %s", (id_producto,))


def _ejecutar_cambio(sql, parametros):
    with closing(database.cursor()) as cursor: # closing() se utiliza para garantizar que el cursor se cierre automáticamente después de su uso, incluso si ocurre una excepción durante la ejecución de la consulta.
        cursor.execute(sql, parametros) # execute() ejecuta la consulta SQL con los parámetros proporcionados, evitando inyecciones SQL y asegurando que los datos se manejen de manera segura.
        database.commit() # commit() se utiliza para guardar los cambios realizados en la base de datos.
