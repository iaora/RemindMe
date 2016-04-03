from twilio.rest import TwilioRestClient
from pymongo import MongoClient
from app import app
import time, datetime

db = MongoClient().reminders
textClient = TwilioRestClient(app.config["ACCOUNT_SID"], app.config["AUTH_TOKEN"])

TIME_BREAK = 10

while(True):
    query = {
        'date' : { "$lte": datetime.datetime.utcnow() }
        }
    for expired in db.test.find(query):
        textClient.messages.create(to='+1'+expired['number'],
                                from_='+18623079011',
                                body=expired['message'])
        db.test.remove(expired)


    time.sleep(TIME_BREAK)

