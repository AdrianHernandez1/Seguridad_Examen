from wtforms import Form
from wtforms import StringField, IntegerField
from wtforms import EmailField

from wtforms import validators
    
class TelefonosForms(Form):
    id=IntegerField('id',[validators.number_range(min=1, max=20, message='Valor no validado')])
    nombre=StringField('Nombre',[
        validators.DataRequired(message='Valor no valido')])
    marca=StringField('marca',{
        validators.DataRequired(message='Valor no valido')})
    descripccion=StringField('descripccion',{
        validators.DataRequired(message='Valor no valido')})
    precio=StringField('precio',[
        validators.DataRequired(message='Valor no valido')])
    existencias=StringField('existencias',[
        validators.DataRequired(message='Valor no valido')])
    foto=StringField('existencias',[
        validators.DataRequired(message='Valor no valido')])
    