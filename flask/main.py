from http import client
from flask import Flask, render_template, request
import json
from pymongo import MongoClient
from bson.json_util import dumps,loads
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
client = MongoClient('localhost',27017)
db = client.flask_db_country
country = db.country

# please visit the first route to get the db created and get data added to it

@app.route('/',methods=['GET','POST'])
def hello_world():
    f= open('country.json')
    data = json.load(f)
    for i in  data:
        dict = {}
        print(i['Code'],i['Name'])
        dict['iso2Code'] = i['Code']
        dict['name'] = i['Name']
        country.insert_one(dict)
    return render_template('index.html')


@app.route('/country',methods= ['GET'])
def countryName():
    data = country.find()
    cur = list(data)
    res = dumps(cur,indent=2)
    return res


