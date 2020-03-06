from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField,SubmitField
from wtforms.validators import DataRequired

from wtforms.widgets.core import html_params
from wtforms import BooleanField
from wtforms.widgets import HTMLString

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Enviar')
    
class searchUserForm(FlaskForm):
    listSearch = StringField('', validators=[DataRequired()],render_kw={"placeholder": "A quien te gustarìa calificar?"})

class InlineButtonWidget(object):
    def __init__(self, css_class,face):
        self.css_class =css_class
        self.face=face
    """
    Render a basic ``<button>`` field.
    """
    input_type = 'submit'
    html_params = staticmethod(html_params)

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', self.face)
        kwargs.setdefault('type', self.input_type)
        kwargs.setdefault('value', field.label.text)
        return HTMLString('<button class="'+ self.css_class +'" %s disabled>' % self.html_params(name=field.name, **kwargs))


class Wink(BooleanField):
    widget = InlineButtonWidget('btn btn-default fas fa-grin-wink',"over")
class Engry(BooleanField):
    widget = InlineButtonWidget('btn btn-default fas fa-angry',"under")    
    
class SpentOverForm(FlaskForm):
    submit = Wink('')
class SpentUnderForm(FlaskForm):
    submit = Engry('')    
    