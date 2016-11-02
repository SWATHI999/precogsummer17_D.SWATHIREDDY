import json
from flask import Flask,request
from flask.ext.pymongo import PyMongo,pymongo
from bson.json_util import dumps
app=Flask(__name__)


app.config['MONGO_DBNAME']='precog'
app.config['MONGO_URI']='mongodb://swathi:swateja@ds031257.mlab.com:31257/precog'

mongo=PyMongo(app)

@app.route('/')
def add():
	user=mongo.db.precog_collection
	output=user.find()
	return dumps(output)

		

if __name__=='__main__':
	app.run(debug=True)

