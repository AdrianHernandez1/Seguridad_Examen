#Importamos la clase Blueprint del módulo flask
from flask import Blueprint, render_template, redirect, url_for
#Importamos login_required, current_user de flask_security
from flask_security import login_required, current_user
#Importamos el decorador login_required de flask_security
from flask_security.decorators import roles_required, roles_accepted
#Importamos el objeto de la BD desde __init__.py
from . import db
# import forms
from flask import request
# from models import Telefonos
from . models import Telefonos, users_roles

main = Blueprint('main',__name__)


#Definimos la ruta a la página principal
@main.route('/')
def index():
    return render_template('index.html')

@main.route('/contacto')
def contacto():
    return render_template('contacto.html')

# #Definimos la ruta a la página de perfil
@main.route('/profile')
@login_required
@roles_accepted('Administrador','Cliente')
def profile():
    telefonos=Telefonos.query.all()
    return render_template('telefonos.html', name=current_user.name, telefonos=telefonos)
    

