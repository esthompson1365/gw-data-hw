from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import misiontomarsscrape


app = Flask(__name__)


mongo = PyMongo(app, uri="mongodb://localhost:27017/surfing_app")


@app.route('/')
def index():
    marsapp = mongo.db.marsapp.find_one()
    return render_template('index.html', marsapp=marsapp)


@app.route('/marsscrape')
def marsscrape():
    marsapp = mongo.db.marsapp
    data = misiontomarsscrape.scrape()
    marsapp.update(
        {},
        data,
        upsert=True
    )
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)



