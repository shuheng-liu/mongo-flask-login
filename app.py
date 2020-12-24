import os
import flask
import pymongo
from flask import Flask
from flask import send_from_directory
from flask import render_template

app = Flask(__name__)

# Database
client = pymongo.MongoClient('localhost', 27017)
db = client.user_login_system

# Routes
from user import routes


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/dashboard/")
def dashboard():
    return render_template("dashboard.html")


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )
