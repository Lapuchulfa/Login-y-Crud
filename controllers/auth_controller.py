from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required, login_user, logout_user
from forms.auth_forms import LoginForms, RegistroForm
from models import usuario_model

auth_bp = Blueprint('auth', __name__) # se crea un blueprint llamado auth para manejar las rutas relacionadas con la autenticación de usuarios

@auth_bp.route('/login', methods=['GET', 'POST']) # se define la ruta /login que acepta los métodos GET y POST
def login():
    if current_user.is_authenticated: # verifica si el usuario ya ha iniciado sesion 
        return redirect(url_for('productos.index')) # si el usuario ya ha iniciado sesion, se redirige a la pagina principal de productos
    
    form = LoginForms() # se crea una instancia del formulario de inicio de sesion
    if form.validate_on_submit():
        usuario = usuario_model.buscar_por_correo(form.correo.data) # se busca el usuario en la base de datos por correo
        if usuario and usuario.verificar_password(form.password.data): # se verifica si el usuario existe y si la contraseña es correcta
            login_user(usuario) # se inicia la sesion del usuario
            return redirect(url_for('productos.index')) # se redirige a la pagina principal de productos
        flash('Correo o contraseña incorrectos') # se muestra un mensaje de error si el correo o la contraseña son incorrectos
    return render_template ('login.html', form=form) # se renderiza la plantilla login.html y se pasa el formulario como argumento

@auth_bp.route('/registro', methods=['GET', 'POST']) # se define la ruta /registro que acepta los métodos GET y POST
def registro():
    form = RegistroForm() # se crea una instancia del formulario de registro
    if form.validate_on_submit(): # se valida el formulario al enviarlo
        if usuario_model.buscar_por_correo(form.correo.data): # se busca el usuario en la base de datos por correo
            flash('El correo ya esta registrado intentelo con uno nuevo')
        else:
            usuario_model.crear(form.nombre.data, form.apellido.data,  # se crea un nuevo usuario en la base de datos con los datos del formulario
                                form.correo.data, form.password.data) # se crea un nuevo usuario en la base de datos con los datos del formulario
            flash('Usuario registrado correctamente') # se muestra un mensaje de exito si el usuario se registro correctamente
            return redirect(url_for('auth.login')) # se redirige a la pagina de inicio de sesion despues de registrar al usuario
    return render_template('registro.html', form=form) # se renderiza la plantilla registro.html y se pasa el formulario como argumento

@auth_bp.route('/logout', methods=['POST']) # se define la ruta /logout que acepta el método POST
@login_required # se requiere que el usuario haya iniciado sesion para poder cerrar sesion
def logout():
    logout_user() # se cierra la sesion del usuario
    return redirect(url_for('auth.login')) # se redirige a la pagina de inicio de sesion despues de cerrar sesion