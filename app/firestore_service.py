from datetime import datetime

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud import firestore as gcloud_firestore


credentials = credentials.ApplicationDefault()
firebase_admin.initialize_app(credentials)

db = firestore.client()

def today():
    #today = date.today().strftime("%d%m%y")
    #import calendar | calendar.monthrange(year, month)[1]
    now = datetime.now()
    return datetime.timestamp(datetime(now.year, now.month, now.day, 0, 0, 1, 0)) #convert to datetime use->fromtimestamp()  | Marca de tiempo del servidor 'timestamp': firestore.SERVER_TIMESTAMP

def get_users():
    return db.collection('users').get()

def get_user(user_id):
    return db.collection('users').document(user_id).get()

def user_put(user_data):
    user_ref = db.collection('users').document(user_data.username)
    user_ref.set({'password': user_data.password })

def edit_profile(user_id,dict_set,dict_update,return_get):
    dict_set['user']=user_id

    ref = db.document( 'users/{}/profile/{}'.format(user_id,today()) )
    get = ref.get()

    if get.exists:
        if dict_update: ref.update(dict_update)
    else:
        ref.set(dict_set)
        if return_get: get = ref.get()
    
    if return_get: return get
    
def get_daily(user_id):
    return edit_profile(return_get=True, user_id=user_id, dict_update=None, dict_set={ 'spent_over': False, 'spent_under': False, 'day': today()})

def update_qualify(user_id, user_torate, event):
    _spent(user_id, event)
    _point(user_id, user_torate, event)

def _spent(user_id,event):

    if event == 'over': 
        dict_set = { 'spent_over': True, 'spent_under': False, 'day': today()} 
    else:
        dict_set = { 'spent_over': False, 'spent_under': True, 'day': today()} 

    edit_profile(
        user_id=user_id,
        return_get=False,
        dict_update={ 'spent_'+event: True },
        dict_set=dict_set
        )

def _point(user_id, user_torate, event):
    def switch_event(event):
        return {
            'over': 'under',
            'under': 'over'
            }[event]

    edit_profile(
        return_get=False,
        user_id=user_torate,
        dict_update={ 'point_'+event: gcloud_firestore.Increment(1), event+'_by': gcloud_firestore.ArrayUnion([user_id]) },
        #dict_set={ 'spent_over': False, 'spent_under': False, 'point_'+event: 1,'point_'+switch_event(event): 0, event+'_by': gcloud_firestore.ArrayUnion([user_id]), 'day': today() }
        dict_set={ 'spent_over': False, 'spent_under': False, 'point_'+event: 1, event+'_by': gcloud_firestore.ArrayUnion([user_id]), 'day': today() } #remove 0
    )

def this_month(user_id):
    now = datetime.now()
    from_timestamp = datetime.timestamp(datetime(now.year, now.month, 1, 0, 0, 1, 0))
    return db.collection('users/{}/profile'.format(user_id)).where('day','>=',from_timestamp).where('day', '<=',today()).stream()

def all_time(user_id):
    #return db.collection('users/{}/profile'.format(user_id)).where('day', '<=',today()).stream()
    return db.collection_group('profile').stream()
