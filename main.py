import unittest
from flask import request, make_response, redirect, render_template, session, url_for, flash
from flask_login import login_required, current_user

from app import create_app
from app.forms import dailyForm, DeletedailyForm, UpdatedailyForm
from app.firestore_service import update_daily, get_daily, put_daily, delete_daily, update_daily

app = create_app()

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip 
    return response

@app.route('/hello', methods=['GET','POST'])
@login_required
def hello():
    user_ip = session.get('user_ip')
    username = current_user.id
    daily_form = dailyForm()
    delete_form = DeletedailyForm()
    update_form = UpdatedailyForm()

    context = {
        'user_ip': user_ip,
        'daily': get_daily(user_id=username),
        'username': username,
        'daily_form': daily_form,
        'delete_form': delete_form,
        'update_form': update_form 
        }

    if daily_form.validate_on_submit():
        put_daily(user_id=username, description=daily_form.description.data)
        flash('El reporte se creo con exito')

        return redirect(url_for('hello'))           

    return render_template('hello.html',**context)

@app.route('/daily/delete/<daily_id>', methods=['POST'])
def delete(daily_id):
    user_id = current_user.id
    delete_daily(user_id=user_id, daily_id=daily_id)

    return redirect(url_for('hello'))

@app.route('/daily/update/<daily_id>/<int:done>', methods=['POST'])
def update(daily_id, done):
    user_id = current_user.id

    update_daily(user_id=user_id, daily_id=daily_id, done=done)
    return redirect(url_for('hello'))

#export FLASK_APP=main.py && export FLASK_ENV=development && export FLASK_DEBUG=1
print(":S")