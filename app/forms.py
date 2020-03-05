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
    listSearch = StringField('', validators=[DataRequired()],render_kw={"placeholder": ""})

class InlineButtonWidget(object):
    def __init__(self, css_class):
        self.css_class =css_class
    """
    Render a basic ``<button>`` field.
    """
    input_type = 'submit'
    html_params = staticmethod(html_params)

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('type', self.input_type)
        kwargs.setdefault('value', field.label.text)
        return HTMLString('<button class="'+ self.css_class +'" %s>' % self.html_params(name=field.name, **kwargs))


class Wink(BooleanField):
    widget = InlineButtonWidget('btn btn-default fas fa-grin-wink')
class Engry(BooleanField):
    widget = InlineButtonWidget('btn btn-default fas fa-angry')    
    
class SpentOverForm(FlaskForm):
    submit = Wink('')
class SpentUnderForm(FlaskForm):
    submit = Engry('')    
    