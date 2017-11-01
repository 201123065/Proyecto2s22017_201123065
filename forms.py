from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField

class crea_user_form(Form):
	username=StringField('username')
	password=StringField('password')
	address=StringField('address')
	phone=StringField('phone')
	age=StringField('age')