from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Enviar')
    
class dailyForm(FlaskForm):
    to_qualify = StringField('', validators=[DataRequired()])
    submit = SubmitField('Buscar')

class DeletedailyForm(FlaskForm):
    submit = SubmitField('Borrar')

class UpdatedailyForm(FlaskForm):
    submit = SubmitField('Actualizar')

class SpentOverForm(FlaskForm):
    submit = SubmitField('+')
class SpentUnderForm(FlaskForm):
    submit = SubmitField('-') 