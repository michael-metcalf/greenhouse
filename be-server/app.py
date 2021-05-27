from dotenv import load_dotenv
import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from .db.models import 

load_dotenv()

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@localhost:5432/test"'
db = SQLAlchemy(app)

