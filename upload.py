import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./ServiceAccountKey.json")
app = firebase_admin.initialize_app(cred)


def save_to_datastore(data):
    db = firestore.client()
    doc_ref = db.collection('subae/fruits/{}'.format(str(data['user_id']))).document("{}_{}".format(data['name'], data['num']))

    log = doc_ref.set(data)

    print(log)

    # Then query for documents
    # users_ref = db.collection('subae')
    # docs = users_ref.get()
    #
    # for doc in docs:
    #     print(u'{} => {}'.format(doc.id, doc.to_dict()))

    if log:
        return True
    else:
        return False
