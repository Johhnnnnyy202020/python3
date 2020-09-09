import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'sample_mflix'
app.config["MONGO_URI"] = "mongodb+srv://Netflix:Netflix@cluster0.7n1lg.mongodb.net/sample_mflix?retryWrites=true&w=majority"

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("movies.html", tasks=mongo.db.movies.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)