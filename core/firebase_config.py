
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
firebase_config ={

}

DatasbaseUrl = ""

# Create User ID and Init database


cred = credentials.Certificate(firebase_config)
dbs = firebase_admin.initialize_app(cred, {
                                'databaseURL': DatasbaseUrl
                                })
ref = db.reference(f"/")
