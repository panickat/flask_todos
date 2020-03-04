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

# def get_daily(user_id):
#     ref = db.collection('users').document(user_id).collection('profile').document(today).get()
#     if ref 
#         return ref
#     else:
#         pass


def _get_profile(user_torate):
    return db.document('users/{}/profile/{}'.format(user_torate,today)) # db.collection('users').document(user_torate).collection('profile').document(today)
    
# ipc
def put_daily_rate(user_id, user_torate, spent_over, spent_under, well, poor):
    exist = db.document('users/{}/profile/{}'.format(user_torate,today)).get()
    profile = _get_profile(user_torate)
    if exist.to_dict() is None:
        profile.set({ 'spent_over': False, 'spent_under': False, 'well':False, 'poor':False })
    else:
        spent_over = not bool(spent_over)
        profile.update({ 'spent_over': spent_over, 'spent_under': spent_under, 'well':well, 'poor':poor })
    return db.document('users/{}/profile/{}'.format(user_torate,today)).get()


