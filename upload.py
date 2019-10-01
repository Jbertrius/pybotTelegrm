from google.cloud import firestore
import datetime


def save_to_datastore(data):
    db = firestore.Client(project='subae-a205b')
    doc_ref = db.collection('subae').document('fruits')
    log = doc_ref.set(data)
    print(log)

    # Then query for documents
    users_ref = db.collection('subae')
    docs = users_ref.get()

    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))