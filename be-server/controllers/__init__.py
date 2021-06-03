from flask import json
from services import *


#########
#
# Users
#
#########

def controller_create_user(db, user_object, json_data):
    try:
        data = service_create_user(db, user_object, json_data)
        return data

    except Exception as e:
        return str(e)

def controller_login_user(user_object, json_data):
    try:
        data = service_login_user(user_object, json_data)
        return data
    except Exception as e:
        return str(e)

def controller_get_user(user_object, id):
    try:
        data = service_get_user(user_object, id)
        return data
    except Exception as e:
        return str(e)

#########
#
# Budgets
#
#########

def controller_get_budget(budget_object, id):
    try:
        data = service_get_budget(budget_object, id)
        return data
    except Exception as e:
        return str(e)

def controller_update_user_budget(db, budget_object, id, json_body):
    try:
        data = service_update_user_budget(db, budget_object, id, json_body)
        return data
    except Exception as e:
        return str(e)

#########
#
# Expenses
#
#########

def controller_create_expense(db, expense_object, id, json_data):
    try:
        data = service_create_expense(db, expense_object, id, json_data)
        return data
    except Exception as e:
        return str(e)

def controller_get_expenses(expense_object, id):
    try:
        data = service_get_expenses(expense_object, id)
        return data
    except Exception as e:
        return str(e)

def controller_get_expense(expense_object, expense_id):
    try:
        data = service_get_expense(expense_object, expense_id)
        return data
    except Exception as e:
        return str(e)

def controller_update_expense(db, expense_object, id, json_body):
    try:
        data = service_update_expense(db, expense_object, id, json_body)
        return data
    except Exception as e:
        return str(e)

#########
#
# Eco Goals / Actions
#
#########

def controller_get_eco_goals(eco_goal_object, id):
    try:
        data = service_get_eco_goals(eco_goal_object, id)
        return data
    except Exception as e:
        return str(e)

def controller_get_eco_actions(eco_action_object, id):
    try:
        data = service_get_eco_actions(eco_action_object, id)
        return data
    except Exception as e:
        return str(e)

def controller_get_eco_actions(eco_action_object, id):
    try:
        data = service_get_eco_actions(eco_action_object, id)
        return data
    except Exception as e:
        return str(e)

#########
#
# Categories
#
#########

def controller_get_categories(category_object, id):
    try:
        data = service_get_categories(category_object, id)
        return data
    except Exception as e:
        return str(e)