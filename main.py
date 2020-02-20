from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
#app.config['ENV'] = 'development' #not work
app.config['SECRET_KEY'] = 'super secretow'
bootstrap = Bootstrap(app)

todos = ['Lupita Gallardo', 'Gerardo prensa', 'Lic. Alverto']

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip #response.set_cookie('user_ip',user_ip)
    return response

@app.route('/hello', methods=['GET','POST'])
def hello():
    user_ip = session.get('user_ip')#request.cookies.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')

    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login_form': login_form,
        'username': username
        }
    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        flash('User name registered successfully')

        return redirect(url_for('index'))

    return render_template('hello.html',**context)
#export FLASK_APP=main.py
#export FLASK_ENV=development ##export FLASK_DEBUG=1

