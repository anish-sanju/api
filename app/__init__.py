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
migrate = Migrate(app, db)
from app import routes