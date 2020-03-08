import unittest
from flask import request, make_response, redirect, render_template, session, url_for, flash
from flask_login import login_required, current_user

from app import create_app

from app.forms import SpentOverForm, SpentUnderForm, searchUserForm
from app.firestore_service import get_daily, update_qualify, get_users, profiles

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
    response = make_response(redirect('/company'))
    return response

@app.route('/company', methods=['GET','POST'])
@login_required
def company():

    user_torate = '33'
    daily = get_daily(user_id=current_user.id)

    if daily.to_dict()['spent_over'] and daily.to_dict()['spent_under']: # pending try builtins.KeyError -> KeyError: 'spent_over' when field spen_x not exist but document whether
        flash("Ya no tienes puntos para gastar")
        return redirect(url_for('no_points'))   

    context = {
    'users': get_users(),
    'spentover_form': SpentOverForm(),
    'spentunder_form': SpentUnderForm(),
    'searchuser_form': searchUserForm(), 
    'daily': daily
    }
    return render_template('company.html',**context)

@app.route('/no_points', methods=['GET'])
def no_points():
    return render_template('no_points.html')

@app.route('/daily/update_qualify/<event>/<user_torate>', methods=['POST'])
def qualify(event,user_torate):
    update_qualify(user_id=current_user.id, user_torate=user_torate, event=event)
    return redirect(url_for('company'))

#settings.py
#export FLASK_APP=main.py && export FLASK_ENV=development && export FLASK_DEBUG=1 && export GOOGLE_APPLICATION_CREDENTIALS=/Users/panic/Documents/_pk/milieu.json && WERKZEUG_DEBUG_PIN=off
print("main run ^,..,^")

@app.route('/debug', methods=['get'])
def debug():
    count = profiles(current_user.id)
    print("########### main count: ", count)


    return render_template('debug.html')