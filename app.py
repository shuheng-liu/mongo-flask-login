import os
import flask
from flask import Flask
from flask import send_from_directory

app = Flask(__name__)


@app.route("/")
def home():
    return "Home"


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )
