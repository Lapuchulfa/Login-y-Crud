import mysql.connector
import config
import os

opciones = dict(
    host=config.DB_HOST,
    port=config.DB_PORT,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    database=config.DB_NAME,
)

# En la nube (Aiven) se usa SSL; en tu PC no
if config.DB_HOST != "localhost":
    opciones["ssl_ca"] = os.path.join(os.path.dirname(__file__), "ca.pem")

database = mysql.connector.connect(**opciones)
