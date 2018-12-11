from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_heroku import Heroku

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Sup?</h>"

if __name__ == '__main__':
    app.debug = True
    app.run()