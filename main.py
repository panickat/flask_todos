from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap

app = Flask(__name__)
#app.config['ENV'] = 'development' #not work
app.config['SECRET_KEY'] = 'super secretow'
bootstrap = Bootstrap(app)

todos = ['Lupita Gallardo', 'Gerardo prensa', 'Lic. Alverto']

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip #response.set_cookie('user_ip',user_ip)
    return response

@app.route('/hello')
def hello():
    user_ip = session.get('user_ip')#request.cookies.get('user_ip')
    context = {'user_ip': user_ip, 'todos': todos}
    return render_template('hello.html',**context)
#export FLASK_APP=main.py
#export FLASK_ENV=development ##export FLASK_DEBUG=1