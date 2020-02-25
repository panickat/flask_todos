import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

credentials = credentials.ApplicationDefault()
firebase_admin.initialize_app(credentials)

db = firestore.client()

def get_users():
    return db.collection('users').get()

def get_user(user_id):
    return db.collection('users').document(user_id).get()

def user_put(user_data):
    user_ref = db.collection('users').document(user_data.username)
    user_ref.set({'password': user_data.password })

def get_daily(user_id):
    return db.collection('users').document(user_id).collection('daily').get()

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