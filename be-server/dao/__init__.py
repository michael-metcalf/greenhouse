from sqlalchemy.sql import extract

#########
#
# Users
#
#########

def dao_create_user(db, user_object, username, email, password):
    new_user = user_object(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

def dao_get_user(user_object, id):
    result = user_object.query.filter_by(id=id).first()
    return result

def dao_get_username(user_object, username):
    result = user_object.query.filter_by(username=username).first()
    return result

#########
#
# Budget
#
#########

def dao_get_budget(budget_object, user_id):
    result = budget_object.query.filter_by(user_id=user_id).first()
    return result

def dao_update_budget(db, budget_object, user_id, monthly_budget, groceries_alloc, bills_alloc, transport_alloc, misc_alloc, savings_target, monthly_income):
    result = budget_object.query.filter_by(user_id=user_id).update(dict(monthly_budget=monthly_budget, groceries_alloc=groceries_alloc, bills_alloc=bills_alloc, transport_alloc=transport_alloc, misc_alloc=misc_alloc, savings_target=savings_target, monthly_income=monthly_income))
    db.session.commit()
    return result

def dao_create_user_budget(db, budget_object, user_id, monthly_budget, groceries_alloc, bills_alloc, transport_alloc, misc_alloc, savings_target, monthly_income):
    new_budget = budget_object(user_id=user_id, monthly_budget=monthly_budget, groceries_alloc=groceries_alloc, bills_alloc=bills_alloc, transport_alloc=transport_alloc, misc_alloc=misc_alloc, savings_target=savings_target, monthly_income=monthly_income)
    db.session.add(new_budget)
    db.session.commit()

#########
#
# Expense
#
#########

def dao_create_expense(db, expense_object, user_id, category_id, expense_description, amount):
    new_expense = expense_object(user_id=user_id, category_id=category_id, expense_description=expense_description, amount=amount)
    db.session.add(new_expense)
    db.session.commit()

def dao_get_expenses(expense_object, user_id, year, month):
    result = expense_object.query.filter_by(user_id=user_id).filter(extract('year', expense_object.created_at) == year, extract('month', expense_object.created_at) == month).all()
    return result

def dao_get_expense(expense_object, expense_id):
    result = expense_object.query.filter_by(id=expense_id).first()
    return result

def dao_get_expense_by_expense_description(expense_object, expense_description):
    result = expense_object.query.filter_by(expense_description=expense_description).first()
    return result

def dao_update_expense(db, expense_object, user_id, category_id, expense_description, amount, modified_at):
    result = expense_object.query.filter_by(user_id=user_id).update(dict(category_id=category_id, expense_description=expense_description, amount=amount, modified_at=modified_at))
    db.session.commit()
    return result

#########
#
# Eco Goals / Actions
#
#########

def dao_get_eco_goals(eco_goal_object, user_id):
    result = eco_goal_object.query.filter_by(user_id=user_id).all()
    return result

def dao_get_eco_actions(eco_action_object, user_id):
    result = eco_action_object.query.filter_by(user_id=user_id).all()
    return result

#########
#
# Eco Goals / Actions
#
#########

def dao_get_categories(category_object, user_id):
    result = category_object.query.filter_by(user_id=user_id).all()
    return result