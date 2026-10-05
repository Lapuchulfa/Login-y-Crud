from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_required
from models import producto_model

productos_bp = Blueprint('productos', __name__) #blueprint para manejar las rutas relacionadas con productos


@productos_bp.route('/')
@login_required #se requiere que el usuario haya iniciado sesion para poder acceder a la pagina principal de productos
def index():
    productos = producto_model.obtener_todos() # obtener todos los productos de la base de datos
    return render_template('index.html', productos=productos)


@productos_bp.route('/producto', methods=['POST'])
@login_required #se requiere que el usuario haya iniciado sesion para poder agregar un producto
def agregar():
    nombre = request.form['Nombre_Producto']
    categoria = request.form['Categoria_Producto']
    precio = request.form['Precio']

    if nombre and categoria and precio:
        producto_model.crear(nombre, categoria, precio)
    return redirect(url_for('productos.index'))


@productos_bp.route('/editar/<int:id_producto>', methods=['POST'])
@login_required #se requiere que el usuario haya iniciado sesion para poder editar un producto
def editar(id_producto):
    nombre = request.form['Nombre_Producto']
    categoria = request.form['Categoria_Producto']
    precio = request.form['Precio']

    if nombre and categoria and precio:
        producto_model.actualizar(id_producto, nombre, categoria, precio)
    return redirect(url_for('productos.index'))



@productos_bp.route('/eliminar/<int:id_producto>', methods=['POST'])
@login_required #se requiere que el usuario haya iniciado sesion para poder eliminar un producto
def eliminar(id_producto):
    producto_model.eliminar(id_producto)
    return redirect(url_for('productos.index'))


