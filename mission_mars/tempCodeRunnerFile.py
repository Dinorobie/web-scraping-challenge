#Import flask
from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrap_mars
import os
import pymongo
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app,uri="mongodb://localhost:27017/sc_mars")

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scrap_mars.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return "Done"

if __name__ == "__main__":
    app.run()