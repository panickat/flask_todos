import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import date

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

def get_daily(user_id):
    return db.collection('users').document('33').collection('profile').document(today).get()

def put_daily(user_id, description):
    daily_collection_ref = db.collection('users').document(user_id).collection('daily')
    daily_collection_ref.add({'description': description,'done':False})

def delete_daily(user_id, daily_id):
    #daily_ref = db.collection('users').document(user_id).collection('daily').document(daily_id)
    daily_ref = _get_daily_ref(user_id,daily_id)
    daily_ref.delete()

def update_daily(user_id, daily_id, done):
    daily_done = not bool(done)
    daily_ref = _get_daily_ref(user_id,daily_id)
    daily_ref.update({'done': daily_done})

def _get_daily_ref(user_id, daily_id):
    return db.document('users/{}/daily/{}'.format(user_id,daily_id))

# ipc
def put_daily_rate(user_id, user_torate, spent_over, spent_under,well, poor):
    daily_profile_ref = db.collection('users').document('33').collection('profile').document(today).get()
    
    if daily_profile_ref.to_dict() is None:
        daily_profile_ref = db.collection('users').document('33').collection('profile').document(today)
        daily_profile_ref.set({ 'spent_over': False, 'spent_under': False, 'well':well, 'poor':poor })
    else:
        daily_profile_ref = db.collection('users').document('33').collection('profile').document(today)
        daily_profile_ref.update({ 'spent_over': spent_over, 'spent_under': spent_under, 'well':well, 'poor':poor })


