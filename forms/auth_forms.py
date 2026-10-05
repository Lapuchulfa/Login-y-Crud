from flask_wtf import FlaskForm # se importa FlaskForm para crear formularios web con Flask-WTF, que proporciona integración con WTForms y protección contra CSRF
from wtforms import PasswordField, StringField, SubmitField # se importan los campos de formulario que se van a utilizar en el formulario de inicio de sesión
from wtforms.validators import DataRequired, EqualTo, Length # se importan los validadores que se van a utilizar para validar los datos ingresados en el formulario de inicio de sesión

class LoginForms(FlaskForm): # se crea una clase LoginForms que hereda de FlaskForm, lo que permite crear un formulario web con los campos y validaciones especificadas
    correo = StringField('Correo', validators=[DataRequired()]) # se crea un campo de tipo StringField con el texto "Correo" que se mostrará en el formulario y se valida que no esté vacío
    password = PasswordField('Password', validators=[DataRequired()]) # se crea un campo de tipo PasswordField con el texto "Password" que se mostrará en el formulario y se valida que no esté vacío
    submit = SubmitField('Iniciar Sesion') # se crea un campo de tipo SubmitField con el texto "Iniciar Sesion" que se mostrará en el botón de envío del formulario
    

class RegistroForm(FlaskForm):
   nombre = StringField('Nombre', validators=[DataRequired(), Length(max=120)]) # se crea un campo de tipo StringField con el texto "Nombre" que se mostrará en el formulario y se valida que no esté vacío y que tenga una longitud mínima de 2 y máxima de 50 caracteres
   apellido = StringField('Apellido', validators=[DataRequired(), Length(max=120)]) # se crea un campo de tipo StringField con el texto "Apellido" que se mostrará en el formulario y se valida que no esté vacío y que tenga una longitud mínima de 2 y máxima de 50 caracteres
   correo = StringField('Correo', validators=[DataRequired(), Length(max=120)])
   password = PasswordField('Password', validators=[DataRequired(), Length(min=6)]) # se crea un campo de tipo PasswordField con el texto "Password" que se mostrará en el formulario y se valida que no esté vacío y que tenga una longitud mínima de 6 caracteres
   confirm_password = PasswordField('Confirmar Password', validators=[DataRequired(), EqualTo('password', message='Las contraseñas no coinciden')]) # se crea un campo de tipo PasswordField con el texto "Confirmar Password" que se mostrará en el formulario y se valida que no esté vacío y que sea igual al campo password
   submit = SubmitField('Registrarse') # se crea un campo de tipo SubmitField con el texto "Registrarse" que se mostrará en el botón de envío del formulario
   
