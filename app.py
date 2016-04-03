from flask import Flask, request, render_template
from pymongo import MongoClient
import datetime

app = Flask(__name__)
client = MongoClient()
db = client.reminders

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        number = request.form['number']
        message = request.form['message']
        datetime = request.form['datetime']

        db.test.insert_one({'number': number,
                            'date': datetime,
                            'message': message})
        print "yay it added"
        return render_template('base.html')

    return render_template('base.html')

if __name__ == '__main__':
    app.debug=True
    app.run()
