import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./ServiceAccountKey.json")
app = firebase_admin.initialize_app(cred)


def save_to_datastore(data):
    db = firestore.client()
    doc_ref = db.collection('subae').document('fruits')
    log = doc_ref.set(data)
    print(log)

    # Then query for documents
    users_ref = db.collection('subae')
    docs = users_ref.get()

    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))
