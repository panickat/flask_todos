from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField,SubmitField,HiddenField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')
    