import os
import flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"


