from dotenv import load_dotenv
import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy.engine import create_engine
from sqlalchemy_utils import database_exists, create_database

###
#
# Initial Database Config
#
###

load_dotenv()

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost:5432/test'
db = SQLAlchemy(app)


###
#
# Creating the database
#
###

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost:5432/test")
if not database_exists(engine.url):
    create_database(engine.url)

###
#
# Defining the models/tables
#
###


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(65), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)
    eco_goals = db.relationship("Eco_Goal", backref="users", lazy=True, cascade="all, delete", nullable=True)
    eco_actions = db.relationship("Eco_Action", backref="users", lazy=True, cascade="all, delete", nullable=True)
    categories = db.relationship("Category", backref="users", lazy=True, cascade="all, delete", nullable=False)
    expenses = db.relationship("Expense", backref="users", lazy=True, cascade="all, delete", nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    last_modified = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        return '<User %r>' % self.username

class Eco_Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    goal_name = db.Column(db.Text, nullable=False)
    eco_actions = db.relationship("Eco_Action", backref="eco_goal", lazy=True, cascade="all, delete", nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    def __repr__(self):
        return '<Eco Goal %r>' % self.goal_name

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    category_name = db.Column(db.String(60), nullable=False)
    category_description = db.Column(db.Text, nullable=True)
    expenses = db.relationship("Expense", backref="category", lazy=True, cascade="all, delete", nullable=True)

    def __repr__(self):
        return '<Category %r>' % self.category_name

class Eco_Action(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    eco_goal_id = db.Column(db.Integer, db.ForeignKey("eco_goal.id"), nullable=False)
    expense_id = db.Column(db.Integer, db.ForeignKey("expense.id"), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        return '<Eco Action %r>' % self.id

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    expense_description = db.Column(db.Text, nullable=True)
    eco_actions = db.relationship("Eco_Action", backref="expense", lazy=True, cascade="all, delete", nullable=True)
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    last_modified = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        return '<Expense %r>' % self.id


###
#
# Creating the tables
#
###

table_check = sqlalchemy.inspect(engine)
if table_check.has_table("users") and table_check.has_table("eco_goal") and table_check.has_table("category") and table_check.has_table("eco_action") and table_check.has_table("expense"):
    pass
else:
    db.create_all()

###
#
# Defining the endpoints
#
###

@app.route("/")
def index():
    return "<p>Hello World</p>"


# russell = Users(username="Russell", password="123", email="123")

query = Users.query.filter_by(username="Russell")

username = query.username

print(f"THE USERNAME IS:{username}")