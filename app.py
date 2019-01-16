# http://flask.pocoo.org/
from flask import Flask, render_template, jsonify, redirect
# https://flask-pymongo.readthedocs.io/en/latest/
from flask_pymongo import PyMongo
# https://pypi.org/project/scraper/
import scraper

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"

mongo = PyMongo(app)

@app.route('/')
def index():
	mars=mongo.db.mars.find_one()
	return render_template("index.html", mars=mars)
	
@app.route('/scrape')
def scrape():
	mars=mongo.db.mars
	data=scrape_mars.scrape()
	mars.update(
		{},
		data,
		upsert=True)
	return redirect("/", code=302)
	
if __name__ == "__main__":
	app.run(debug=True)