from app import db

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
