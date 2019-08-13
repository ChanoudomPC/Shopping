import os
import json
from bson.json_util import dumps

# import requests, re
from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

#Database Connection
MONGO_URI = 'mongodb://sixsixone5:42577400Vj@ds133137.mlab.com:33137/heroku_mck6pbmw'
mongo = MongoClient(MONGO_URI)
mydb = mongo.heroku_mck6pbmw

#Collection Name
message = mydb["products_548501935686874"]

@app.route("/api/menu", methods = ['GET'])
def show():
    page_id = request.args.get('pageid')
    print("==> ", page_id)
    try:

        food = mydb.products_548501935686874.find()

        data = {
            'Menu': food,
        }
    except Exception as e:
        print(e)
        return dumps("There is a problem")
    return dumps(data)

@app.route('/')
def search():
    # phones = mydb.customer_phones.find().limit(100)

    list_food = list(message.find())
        # print("-=-> ", phone_numbers)
    return render_template('index.html', food=list_food)


@app.route('/')
def hello():
    # phones = mydb.customer_phones.find().limit(100)
    list_food = list(message.find())
        # print("-=-> ", phone_numbers)
    return render_template('index.html', food=list_food)

if __name__ == '__main__':
    app.run(debug=True)


