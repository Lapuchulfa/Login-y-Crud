from flask import Flask
from flask_login import LoginManager

import config
from controllers.auth_controller import auth_bp
from controllers.producto_controller import productos_bp
from models import usuario_model

app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY  # se establece la clave secreta de la aplicación Flask, que se utiliza para proteger las sesiones y otros datos sensibles.
   
login_manager = LoginManager(app) # se crea una instancia de LoginManager, que se utiliza para manejar la autenticación de usuarios en la aplicación Flask.
login_manager.login_view = 'auth.login' # se establece la vista de inicio de sesión, que se utiliza para redirigir a los usuarios no autenticados a la página de inicio de sesión cuando intentan acceder a una página protegida.
login_manager.login_message = 'Iniciar sesion para poder acceder al CRUD'

@login_manager.user_loader
def cargar_usuario(id_usuario):
    return usuario_model.buscar_por_id(int(id_usuario)) # se define una función que carga un usuario a partir de su ID, que se utiliza para mantener la sesión del usuario autenticado.

app.register_blueprint(auth_bp) # se registra el blueprint de autenticación, que contiene las rutas y vistas relacionadas con el inicio de sesión y el registro de usuarios.
app.register_blueprint(productos_bp) # se registra el blueprint de productos, que contiene las rutas y vistas relacionadas con la gestión de productos.   
   
if __name__ == '__main__': 
    app.run(debug=True)

