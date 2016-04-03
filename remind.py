#!/usr/local/bin/

import os
import pymongo
from pymongo import MongoClient
import datetime

client = MongoClient()
db = client.reminders

#while(True):
#    input = raw_input('your_prompt$ ')
#    input = input.split()
#    if input[0] == 'remind':

db.test.insert_one({'number': '19737389532',
                    'date': datetime.datetime.utcnow(),
                    'message': 'hello'})
