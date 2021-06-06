from app import app
from controllers import *
from app import db
from app.models import Users, Budget, Expense, Eco_Goal, Eco_Action, Category
from flask import request, send_from_directory


@app.route("/")
def index():
    return "<p>Hello World</p>"

@app.route('/app')
def root():
    return send_from_directory('static', 'index.html')


#########
#
# Users
#
#########

@app.route("/api/user/create", methods=["POST"])
def createuser():
    data = controller_create_user(db, Users, Budget, request.json)
    return data

@app.route("/api/user/login", methods=["POST"])
def loginuser():
    data = controller_login_user(Users, request.json)
    return data

@app.route("/api/user/<id>")
def getuser(id):
    data = controller_get_user(Users, id)
    return data

#########
#
# Budgets
#
#########

@app.route("/api/user/<id>/user_budget")
def get_budget(id):
    data = controller_get_budget(Budget, id)
    return data

@app.route("/api/user/<id>/user_budget", methods=["PATCH"])
def update_user_budget(id):
    data = controller_update_user_budget(db, Budget, id, request.json)
    return data

@app.route("/api/user/<id>/user_budget", methods=["POST"])
def create_user_budget(id):
    data = controller_create_user_budget(db, Budget, id, request.json)
    return data

#########
#
# Expenses
#
#########

@app.route("/api/user/<id>/expenses")
def get_expenses(id):
    data = controller_get_expenses(Expense, id)
    return data

@app.route("/api/user/<id>/expenses/<expense_id>")
def get_expense(id, expense_id):
    data = controller_get_expense(Expense, expense_id)
    return data

@app.route("/api/user/<id>/expenses", methods=["PATCH"])
def update_expense(id):
    data = controller_update_expense(db, Expense, id, request.json)
    return data

@app.route("/api/user/<id>/expenses", methods=["POST"])
def create_expense(id):
    data = controller_create_expense(db, Expense, id, request.json)
    return data

#########
#
# Eco Goals / Actions
#
#########

@app.route("/api/user/<id>/eco_goals")
def get_eco_goals(id):
    data = controller_get_eco_goals(Eco_Goal, id)
    return data

@app.route("/api/user/<id>/eco_actions")
def get_eco_actions(id):
    data = controller_get_eco_actions(Eco_Action, id)
    return data

#########
#
# Categories
#
#########

@app.route("/api/user/<id>/categories")
def get_categories(id):
    data = controller_get_categories(Category, id)
    return data