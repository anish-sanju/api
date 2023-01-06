from flask import Flask, request
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['CORS_HEADERS'] = 'Content-Type'
# configuration of database
app.config.from_object(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

db = SQLAlchemy(app)
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

migrate = Migrate(app, db)
from app import routes