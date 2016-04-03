from flask import Flask, request, render_template
from pymongo import MongoClient
import datetime
from datetime import timedelta
import twilio.twiml
from twilio.rest import TwilioRestClient

app = Flask(__name__)
app.config.from_pyfile('config.py')
client = MongoClient()
db = client.reminders
textClient = TwilioRestClient(app.config["ACCOUNT_SID"], app.config["AUTH_TOKEN"])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        number = request.form['number']
        message = request.form['message']
        offset = request.form['offset']

        if number is None or message is None or offset is None:
            return render_template('error.html')

        end_time = datetime.datetime.utcnow() + timedelta(minutes=int(offset))

        db.test.insert_one({'number': number,
                            'date': end_time,
                            'message': message})

        return render_template('index.html',number=number, message=message)

    return render_template('index.html')

@app.route('/message', methods=['POST'])
def reply():
    if request.method == 'POST':
        body = request.form["Body"]
        word = body.split()

        end_time = datetime.datetime.utcnow() + timedelta(minutes=int(word[1]))
        text = word[2]
        for i in range (3,len(word)):
            text = text + " " +  word[i]
            print text

        db.test.insert_one({'number': word[0],
                            'date': end_time,
                            'message': text})

        resp = twilio.twiml.Response()
        return str(resp.message("Success!"))


if __name__ == '__main__':
    app.debug=True
    app.run()
