import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import date
from google.api_core.exceptions import NotFound

credentials = credentials.ApplicationDefault()
firebase_admin.initialize_app(credentials)

db = firestore.client()
today = date.today().strftime("%d%m%y")

def get_users():
    return db.collection('users').get()

def get_user(user_id):
    return db.collection('users').document(user_id).get()

def user_put(user_data):
    user_ref = db.collection('users').document(user_data.username)
    user_ref.set({'password': user_data.password })

def profile(user_id):
    return db.document('users/{}/profile/{}'.format(user_id,today)) # db.collection('users').document(user_torate).collection('profile').document(today)
    
def get_daily(user_id):
    ref = profile(user_id)
    _get = ref.get()
    if _get.exists:
        return _get
    else:
        ref.set({ 'spent_over': False, 'spent_under': False})
        return ref.get()

def update_qualify(user_id, user_torate, event):
    _spent(user_id,event)
    _point(user_torate,event)

def _spent(user_id,event):
    try:
        ref = profile(user_id)
        ref.update({ 'spent_'+event: True })
    except NotFound: #https://google-cloud-python.readthedocs.io/en/0.32.0/_modules/google/api_core/exceptions.html#NotFound
        ref.set({ 'spent_over': True, 'spent_under': False}) if event == 'over' else ref.set({ 'spent_over': False, 'spent_under': True})

def _point(user_torate,event):
    try:
        ref = profile(user_torate)
        ref.update({ 'point_'+event: 1 })
    except NotFound:
        ref.set({ 'spent_over': False, 'spent_under': False, 'point_'+event: 1 })