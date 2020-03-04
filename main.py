import unittest
from flask import request, make_response, redirect, render_template, session, url_for, flash
from flask_login import login_required, current_user

from app import create_app

from app.forms import DeletedailyForm, UpdatedailyForm, SpentOverForm, SpentUnderForm, dailyForm
from app.firestore_service import get_daily, update_qualify

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

    user_torate = '33'
    spentover_form = SpentOverForm()
    spentunder_form = SpentUnderForm()

    daily_form = dailyForm()
    delete_form = DeletedailyForm()
    update_form = UpdatedailyForm()

    context = {
        'user_ip': user_ip,

        'spentover_form': spentover_form,
        'spentunder_form': spentunder_form,        
        'daily': get_daily(user_id=current_user.id),
        'daily_form': daily_form,
        'delete_form': delete_form,
        'update_form': update_form 
        }

    if daily_form.validate_on_submit(): # change name to usert_torate
        #description=daily_form.description.data)
        flash('El reporte se creo con exito')
        return redirect(url_for('hello'))           

    return render_template('hello.html',**context)

@app.route('/daily/update_qualify/<user_torate>/<event>', methods=['POST'])
def qualify(user_torate,event):
    update_qualify(user_id=current_user.id, user_torate=user_torate, event=event)
    return redirect(url_for('hello'))

#export FLASK_APP=main.py && export FLASK_ENV=development && export FLASK_DEBUG=1 && export GOOGLE_APPLICATION_CREDENTIALS=/Users/panic/Documents/_pk/milieu.json
print(":S")