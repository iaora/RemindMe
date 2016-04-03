from flask import render_template
from pymongo import MongoClient
from app import app, textClient
import time, datetime
import twilio

db = MongoClient().reminders
#textClient = TwilioRestClient(app.config["ACCOUNT_SID"], app.config["AUTH_TOKEN"])

TIME_BREAK = 50

while(True):
    query = {
        'date' : { "$lte": datetime.datetime.utcnow() }
        }
    for expired in db.test.find(query):
        try:
            textClient.messages.create(to='+1'+expired['number'],
                                    from_='+18623079011',
                                    body=expired['message'])
        except twilio.TwilioRestException as e:
            return render_template('error.html')


        db.test.remove(expired)


    time.sleep(TIME_BREAK)

