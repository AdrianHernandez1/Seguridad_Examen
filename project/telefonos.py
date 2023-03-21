#Importamos la clase Blueprint del módulo flask
from flask import Blueprint, render_template, redirect, url_for
#Importamos login_required, current_user de flask_security
from flask_security import login_required, current_user
#Importamos el decorador login_required de flask_security
from flask_security.decorators import roles_required, roles_accepted
#Importamos el objeto de la BD desde __init__.py
from . import db, forms
# import forms
from flask import request
# from models import Telefonos
from .models import Telefonos


telefonos= Blueprint('telefonos', __name__)



@telefonos.route('/guardar')
@login_required
@roles_required('Administrador')
@roles_accepted()
def guardar():
    return render_template('guardar.html')

@telefonos.route('/guardar', methods=['POST'])
@login_required
@roles_required('Administrador')
@roles_accepted()
def guardar_post():
    nombre= request.form.get('nombre')
    marca= request.form.get('marca')
    descripccion= request.form.get('descripccion')
    precio= request.form.get('precio')
    existencia= request.form.get('existencia')
    foto= request.form.get('foto')

    if request.method=='POST':
        t=Telefonos(nombre=nombre, marca=marca, descripccion=descripccion, precio=precio, existencias=existencia, foto=foto)
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('main.profile'))

    return render_template('guardar.html',name=current_user.name)


@telefonos.route("/modificar", methods=['GET','POST'])
@login_required
@roles_required('Administrador')
@roles_accepted()
def modificar():
    create_form=forms.TelefonosForms(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        #select * from alumnos where id=id
        t=db.session.query(Telefonos).filter(Telefonos.id==id).first()
        create_form.id.data=request.args.get('id')
        create_form.nombre.data=t.nombre
        create_form.marca.data=t.marca
        create_form.descripccion.data=t.descripccion
        create_form.precio.data=t.precio
        create_form.existencias.data=t.existencias
        create_form.foto.data=t.foto

    if request.method=='POST':
        id=create_form.id.data
        t=db.session.query(Telefonos).filter(Telefonos.id==id).first()
        t.nombre=create_form.nombre.data
        t.marca=create_form.marca.data
        t.descripccion=create_form.descripccion.data
        t.precio=create_form.precio.data
        t.existencias=create_form.existencias.data
        t.foto=create_form.foto.data
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('main.profile'))
    return render_template('modificar.html',form=create_form)

@telefonos.route("/eliminar", methods=['GET','POST'])
@login_required
@roles_required('Administrador')
@roles_accepted()
def eliminar():
    create_form=forms.TelefonosForms(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        #select * from alumnos where id=id
        t=db.session.query(Telefonos).filter(Telefonos.id==id).first()
        create_form.id.data=request.args.get('id')
        create_form.nombre.data=t.nombre
        create_form.marca.data=t.marca
        create_form.descripccion.data=t.descripccion
        create_form.precio.data=t.precio
        create_form.existencias.data=t.existencias
        create_form.foto.data=t.foto

    if request.method=='POST':
        id=create_form.id.data
        t=db.session.query(Telefonos).filter(Telefonos.id==id).first()
        db.session.delete(t)
        db.session.commit()
        return redirect(url_for('main.profile'))
    return render_template('eliminar.html',form=create_form)