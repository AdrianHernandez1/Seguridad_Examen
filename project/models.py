#Importamos el objeto de la base de  desde __init__.py
from . import db
from flask_sqlalchemy import SQLAlchemy
#Importamos las clases UserMixin y RoleMixin de flask_security
from flask_security import UserMixin, RoleMixin

#db = SQLAlchemy()

#Definiendo la tabla relacional entre usuarios roles
users_roles = db.Table('users_roles',
    db.Column('userId', db.Integer, db.ForeignKey('user.id')),
    db.Column('roleId', db.Integer, db.ForeignKey('role.id')))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean)
    confirmed_at = db.Column(db.DateTime)
    admin = db.Column(db.Boolean, nullable=True)
    roles = db.relationship('Role',
        secondary=users_roles,
        backref= db.backref('users', lazy='dynamic'))

class Role(RoleMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description =  db.Column(db.String(255))

class Telefonos(db.Model):
    __tablename__='telefonos'
    id=db.Column(db.Integer, primary_key=True) 
    nombre=db.Column(db.String(50))
    marca=db.Column(db.String(50)) 
    descripccion=db.Column(db.String(200))
    precio=db.Column(db.String(50)) 
    existencias=db.Column(db.Integer)  
    foto=db.Column(db.Text)
