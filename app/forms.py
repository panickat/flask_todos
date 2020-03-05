from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Enviar')
    
class searchUserForm(FlaskForm):
    listSearch = StringField('', validators=[DataRequired()],render_kw={"placeholder": "A quien te gustaría calificar?"})

class SpentOverForm(FlaskForm):
    submit = SubmitField('+')
class SpentUnderForm(FlaskForm):
    submit = SubmitField('-') 