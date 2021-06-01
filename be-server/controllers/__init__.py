from flask import json
from services import *

def controller_create_user(db, user_object, json_data):
    try:
        data = service_create_user(db, user_object, json_data)
        return data

    except Exception as e:
        return str(e)

def controller_get_user(user_object, id):
    try:
        data = service_get_user(user_object, id)
        return data
    except Exception as e:
        return str(e)

def controller_get_budget(user_object, budget_object, id):
    try:
        data = service_get_budget(user_object, budget_object, id)
        return data
    except Exception as e:
        return str(e)

def controller_get_expenses(user_object, expense_object, id):
    try:
        data = service_get_expenses(user_object, expense_object, id)
        return data
    except Exception as e:
        return str(e)

def controller_get_expense(user_object, expense_object, id, expense_id):
    try:
        data = service_get_expense(user_object, expense_object, id, expense_id)
        return data
    except Exception as e:
        return str(e)


def controller_get_eco_goals(user_object, eco_goal_object, id):
    try:
        data = service_get_eco_goals(user_object, eco_goal_object, id)
        return data
    except Exception as e:
        return str(e)

def controller_update_user_budget(db, user_object, budget_object, id, json_body):
    try:
        data = service_update_user_budget(db, user_object, budget_object, id, json_body)
        return data
    except Exception as e:
        return str(e)