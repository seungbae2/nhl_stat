from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import requests
import os


app = Flask(__name__)
#app._static_folder = os.path.abspath("templates/static/")
mongo = PyMongo(app, uri = 'mongodb://localhost:27017/nhl_db')

@app.route("/")
def home():

	mongo.db.event_data.remove({})
	nhl_data = scrape_mars.event()
	mongo.db.event_data.insert_many(nhl_data)

	mongo.db.stat_summary.remove({})
	stat = scrape_mars.summary()
	print(stat)
	mongo.db.stat_summary.insert(stat)

	return render_template("index.html", data = stat)


@app.route("/scrape")
def scrape():

	mongo.db.collection.remove({})
	nhl_data = scrape_mars.scrape()

	# for data in nhl_data:
	# 	mongo.db.collection.insert({}, data)

	mongo.db.collection.insert_many(nhl_data)
	

	return redirect("/")


if __name__ == "__main__":
	app.run(debug=True)