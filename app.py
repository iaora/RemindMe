from flask import Flask, request, render_template
from pymongo import MongoClient
import datetime
from datetime import timedelta

app = Flask(__name__)
app.config.from_pyfile('config.py')
client = MongoClient()
db = client.reminders

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        number = request.form['number']
        message = request.form['message']
        offset = request.form['offset']

        end_time = datetime.datetime.utcnow() + timedelta(minutes=int(offset))

        db.test.insert_one({'number': number,
                            'date': end_time,
                            'message': message})

        print "yay it added"
        return render_template('index.html',number=number, message=message)

    return render_template('index.html')

if __name__ == '__main__':
    app.debug=True
    app.run()
