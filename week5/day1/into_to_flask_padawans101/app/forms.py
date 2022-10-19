from ast import Pass
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Datarequired, EqualTo

class UserCreationForm(FlaskForm):
    username = StringField('Username', validators = [Datarequired()])
