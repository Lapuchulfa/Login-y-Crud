# Login-y-Crud
Aplicación web para administrar productos con un sistema de autenticación de usuarios,
desarrollada en Flask siguiendo el patrón Modelo-Vista-Controlador.

<h2> Demo en Linea</h2>
https://login-y-crud-smbm.onrender.com

<h2> Video de Ejecución</h2>
https://youtu.be/QXF7_g02uQE

<h2>Funcionalidades</h2>
<p>
Registro: crear una cuenta con nombre, apellido, correo y contraseña.
Inicio de sesión: acceso con correo y contraseña.
Cierre de sesión: termina la sesión del usuario.
CRUD de productos: listar, agregar, editar y eliminar productos.
Rutas protegidas: no es posible acceder al CRUD sin iniciar sesión.
Contraseñas encriptadas: se guardan como hash, nunca en texto plano.
</p>

<h2>Capturas</h2>

Login 

<img width="787" height="667" alt="image" src="https://github.com/user-attachments/assets/de9489de-7783-450b-95df-c541126062b7" />

Registro

<img width="605" height="855" alt="image" src="https://github.com/user-attachments/assets/5da223cf-6be4-4b2c-93e7-3dd76703bf76" />

CRUD


<img width="1749" height="609" alt="image" src="https://github.com/user-attachments/assets/ea2f05e4-3dd4-4bf8-b080-f0fd188aba12" />

## Tecnologías
- [Python](https://www.python.org/) · [Flask](https://flask.palletsprojects.com/)
- [Flask-Login](https://flask-login.readthedocs.io/) · [Flask-WTF](https://flask-wtf.readthedocs.io/)
- [MySQL](https://www.mysql.com/) · `mysql-connector-python`
- [Bootstrap 5](https://getbootstrap.com/)
- [Gunicorn](https://gunicorn.org/) · [Render](https://render.com/) · [Aiven](https://aiven.io/)

## Seguridad
- **Rutas protegidas:** todas las rutas del CRUD usan `@login_required` (Flask-Login). Sin sesión, redirigen al login.
- **Contraseñas con hash scrypt** (`werkzeug.security`). Se eligió en lugar de MD5 porque usa *sal* aleatoria y es lento a propósito, lo que dificulta los ataques de fuerza bruta.
- **Protección CSRF** en los formularios de login y registro (Flask-WTF).
- **Sesión firmada** con una `SECRET_KEY` guardada en variables de entorno.
- **Consultas parametrizadas** (`%s`) para evitar inyección SQL.

## Autor
| [<img src="https://github.com/Lapuchulfa.png" width=115><br><sub><Tu nombre></sub>](https://github.com/Lapuchulfa) |
| :---: |

Trabajo Academico CRUD y Login — Ingeniería Web, Semestre 7, UDLA.
