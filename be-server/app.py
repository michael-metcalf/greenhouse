from dotenv import load_dotenv
import os
from flask import Flask, request, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy.engine import create_engine
from sqlalchemy_utils import database_exists, create_database
from .controllers import *

###
#
# Initial Database Config
#
###

load_dotenv()

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_CONNECTION = os.environ.get("DB_CONNECTION")

app = Flask(__name__, static_url_path='')
CORS(app, origins=["http://localhost:8080", "http://localhost:5000"])
# app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost:5432/greenhouse'
app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql://{DB_CONNECTION}'
db = SQLAlchemy(app)

###
#
# Creating the database
#
###

# engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost:5432/greenhouse")
engine = create_engine(f"postgresql://{DB_CONNECTION}")
if not database_exists(engine.url):
    create_database(engine.url)

###
#
# Defining the models/tables
#
###


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(65), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    last_modified = db.Column(db.DateTime, default=db.func.now()) 


    eco_goals = db.relationship("Eco_Goal", back_populates="user", lazy=True, cascade="all, delete")
    eco_actions = db.relationship("Eco_Action", back_populates="user", lazy=True, cascade="all, delete")
    categories = db.relationship("Category", back_populates="user", lazy=True, cascade="all, delete")
    expenses = db.relationship("Expense", back_populates="user", lazy=True, cascade="all, delete")
    budget = db.relationship("Budget", back_populates="user", lazy=True, cascade="all, delete")

    def __repr__(self):
        return '<User %r>' % self.username

class Eco_Goal(db.Model):
    __tablename__ = "eco_goal"
    id = db.Column(db.Integer, primary_key=True)
    goal_name = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship("Users", back_populates="eco_goals", lazy=True, cascade="all, delete")
    eco_actions = db.relationship("Eco_Action", back_populates="eco_goal", lazy=True, cascade="all, delete")
    
    def __repr__(self):
        return '<Eco Goal %r>' % self.goal_name

class Eco_Action(db.Model):
    __tablename__ = "eco_action"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    eco_goal_id = db.Column(db.Integer, db.ForeignKey("eco_goal.id"), nullable=False)
    expense_id = db.Column(db.Integer, db.ForeignKey("expense.id"), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.now())

    user = db.relationship("Users", back_populates="eco_actions", lazy=True, cascade="all, delete")
    eco_goal = db.relationship("Eco_Goal", back_populates="eco_actions", lazy=True, cascade="all, delete")
    expense = db.relationship("Expense", back_populates="eco_action", lazy=True, cascade="all, delete")

    def __repr__(self):
        return '<Eco Action %r>' % self.id

class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    category_name = db.Column(db.String(60), nullable=False)
    category_description = db.Column(db.Text, nullable=True)

    expenses = db.relationship("Expense", back_populates="category", lazy=True, cascade="all, delete")
    user = db.relationship("Users", back_populates="categories", lazy=True, cascade="all, delete")

    def __repr__(self):
        return '<Category %r>' % self.category_name

class Expense(db.Model):
    __tablename__ = "expense"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    expense_description = db.Column(db.Text, nullable=True)
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    last_modified = db.Column(db.DateTime, default=db.func.now())
   
    user = db.relationship("Users", back_populates="expenses", lazy=True, cascade="all, delete")
    category = db.relationship("Category", back_populates="expenses", lazy=True, cascade="all, delete")
    eco_action = db.relationship("Eco_Action", back_populates="expense", lazy=True, cascade="all, delete")

    def __repr__(self):
        return '<Expense %r>' % self.id

class Budget(db.Model):
    __tablename__ = "budget"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    monthly_budget = db.Column(db.Float, nullable=False)
    groceries_alloc = db.Column(db.Float, nullable=False)
    bills_alloc = db.Column(db.Float, nullable=False)
    transport_alloc = db.Column(db.Float, nullable=False)
    misc_alloc = db.Column(db.Float, nullable=False)
    savings_target = db.Column(db.Float, nullable=False)
    monthly_income = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

    user = db.relationship("Users", back_populates="budget", lazy=True, cascade="all, delete")


###
#
# Creating the tables
#
###

table_check = sqlalchemy.inspect(engine)
if table_check.has_table("users") and table_check.has_table("eco_goal") and table_check.has_table("category") and table_check.has_table("eco_action") and table_check.has_table("expense") and table_check.has_table("budget"):
    pass
else:
    db.create_all()

###
#
# Defining the endpoints
#
###

@app.route("/greeting")
def greeting():
  return {"greeting": "Hello from Flask!"}

@app.route('/app')
def root():
    return send_from_directory('static', 'index.html')

# @app.route("/")
# def index():
#     return "<p>Hello World</p>"

@app.route("/api/user/create", methods=["POST"])
def createuser():
    data = controller_create_user(db, Users, request.json)
    return data

@app.route("/api/user/<id>")
def getuser(id):
    data = controller_get_user(Users, id)
    return data

@app.route("/api/user/<id>/user_budget")
def get_budget(id):
    data = controller_get_budget(Users, Budget, id)
    return data

@app.route("/api/user/<id>/expenses")
def get_expenses(id):
    data = controller_get_expenses(Users, Expense, id)
    return data

@app.route("/api/user/<id>/eco_goals")
def get_eco_goals(id):
    data = controller_get_eco_goals(Users, Eco_Goal, id)
    return data

@app.route("/api/user/<id>/expenses/<expense_id>")
def get_expense(id, expense_id):
    data = controller_get_expense(Users, Expense, id, expense_id)
    return data

@app.route("/api/user/<id>/user_budget", methods=["PATCH"])
def update_user_budget(id):
    data = controller_update_user_budget(db, Users, Budget, id, request.json)
    return data