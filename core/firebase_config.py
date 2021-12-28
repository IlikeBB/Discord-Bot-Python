
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
firebase_config ={
  "type": "service_account",
  "project_id": "discordbot-dfcf6",
  "private_key_id": "e2d4b5f0e8da1a3b977d9b87f74543d4111b240f",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDJrBJBMHVsKoYt\nFHKWmb2sU2irbAqKfww1HNgKGOQ0T6yUpPS+2TR21rPvA2gCSCOt7zA5+q3WEFd3\nqOM6u08BKcnaxoGoIj3ermeAXWGClnho9g2R3sueWRDRjLNx0Us342YjaGFwWWm6\n9QEW/DS3HDuSiZXO9yGZHkdy6uyoYen/YGpGI10L4tSVP6z5OdbIIHely3czKGsW\ncOH9I7XS1Cv/vAVCpDthRxNNsnIHBhyIXRsgfNBzBZ4XvfPKxe3byxB3Gv/saRu/\n0Wng+6PVjux11FpH/57wuVSnK9FXd0WTnawy/IEusQa32pn2ZlcreXpserTccoZy\nFYGQKeRFAgMBAAECggEAZAR9Jyx3x9XNJpVSASOtQEY7jmyuS6KXtM2hzVwr7U+o\nWS34HaCOVvPDWCH51svdOhl6cv7CcPw4zOULEKktlPebHu+9BNw6j/Ix7aUiQ4gJ\nnpCNCU+T72vfnfVoV2XDpquWD7BoRrZpa+mviS06naeYWeP3UqYY2R39tF4TUawf\nfM/+riYYFDRDq3fg51ZLQmV4pEOVtgxvedpPv5wHvEjgRQ3NrvG6fgBcDy/noDKL\nWlkvLCio+R/GK5YbqPj0Wk8PmEkjdP7nXJQ/S/jaPNrYAH42TTcfazXm5d0UUPHg\nRmIIbUj5aX983HscZb9WYdYwv7pYZXxTvWN5SlI/LwKBgQD4oEWGGu/Ks4o+VbJW\n+sFRPPhlkSrr3WwOTQ6OHyav/yZAKW/YDr3h6YuXrs7dPqXBvKMda+V9qMnK2Ces\nX3RQ1AlgukEquJMGIWKwF+U/UdMj1CaaOCL8iIatfmD9d3dUmu+kH5M7RUqjmjNO\ndocWn8mS1jNzoJBlDnNVcjFirwKBgQDPp0uqWf0R1zQHrFrrrYQ1l/EhCzGGGp5y\nsDyXZDTc9kl7ZTV1m5aZLGmMjOldJsfUUwSKS4S27V83EOjnTs07y4r2a8Uv5K4t\nIDm6Gk6PmbAozn5HAOfDOJhFuShRb2P7CQlX20H/DHhUnaPSikJTykGKf1qD75Nn\npO0tVeh1SwKBgFtFoyA/JUaZsKd/mE/cEDn9kwbeSw55o+CAI1bDUtWLaoRlcdy0\nVLrpnMhbcS/BfuJnmM4FPSNrYmEoBzB9flrp7GNpHOFNDxRSD0OsEgmzxTpC+MTm\n1Nk2WZK5cWu7fsA9fLoYqVk579OtmSY11xPUJxDTt+G70SZ4LpjwqfabAoGAPhvZ\nw+Aak4V8qHbi0u8ZRjZmBu4kJ+o6Ti9sUBPGw/heTiwda0nYJ4RjJYjYG+aHingy\nOXMRBO3Gtt+16clmFWZx7/aYChUqC5FB8un/aXAcgngQyQf6SifZU7Fn38Ojceho\nBQEtoi2GqDhmUYjNAebS56vj1OaJfkyULCUv3DUCgYEAlucqC7P3UomQbLcdXaBP\nr0a+GcGcJQTp9wFcv0elBKyIYtbbrdZ5HTAkxN7u3/zcYeNYst4CWrDEa6pWMmVt\nvUuSRpeHHR/vee5Qrawjrn9NwbWnVeiopC5bnATfGG6NFjXIz1pYHfI1XHjrbkhX\n+mU8YNY7KRBIsnK36wU91uM=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-pktxv@discordbot-dfcf6.iam.gserviceaccount.com",
  "client_id": "101074692627987160584",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-pktxv%40discordbot-dfcf6.iam.gserviceaccount.com"
}

DatasbaseUrl = "https://discordbot-dfcf6-default-rtdb.firebaseio.com/"

# Create User ID and Init database


cred = credentials.Certificate(firebase_config)
dbs = firebase_admin.initialize_app(cred, {
                                'databaseURL': DatasbaseUrl
                                })
ref = db.reference(f"/")
