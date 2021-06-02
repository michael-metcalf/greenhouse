from app import app
from controllers import *
from app import db
from app.models import Users, Budget, Expense, Eco_Goal
from flask import request, send_from_directory


@app.route("/")
def index():
    return "<p>Hello World</p>"

@app.route('/app')
def root():
    return send_from_directory('static', 'index.html')

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

@app.route("/api/user/<id>/user_budget", methods=["PATCH"])
def update_expense(id):
    data = controller_update_expense(db, Users, Expense, id, request.json)
    return data

