from app import app, db
from datetime import datetime

# Admin table
class Admin(db.Model):
    __tablename__ = 'admin'

    admin_id = db.Column(db.Integer, primary_key=True)
    admin_name = db.Column(db.String(30), nullable=False)
    admin_email = db.Column(db.String(30), unique = True, nullable=False)
    admin_password = db.Column(db.String(30), nullable=False)


    def __init__(self, email, password, name):
        self.admin_email = email
        self.admin_password = password
        self.admin_name = name

# Customer table
class Customer(db.Model):
    __tablename__ = 'customer'

    customer_id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(30), nullable=False)
    customer_email = db.Column(db.String(30), unique = True, nullable=False)
    customer_password = db.Column(db.String(30), nullable=False)
    customer_phone = db.Column(db.String(30), nullable=False)

    def __init__(self, email, password, name, phone):
        self.customer_email = email
        self.customer_password = password
        self.customer_name = name
        self.customer_phone = phone

# Food table
class Food(db.Model):
    __tablename__ = 'food'

    admin_id = db.Column(db.Integer, db.ForeignKey('admin.admin_id'), nullable=False)
    food_id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(30), nullable=False)
    food_description = db.Column(db.String(30), nullable=False)

    def __init__(self, name, description):
        self.food_name = name
        self.food_description = description


# Order_food table
class Order_food(db.Model):
    __tablename__ = 'order_food'

    food_id = db.Column(db.Integer, db.ForeignKey('food.food_id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)
    order_id = db.Column(db.Integer, primary_key=True)
    order_time = db.Column(db.DateTime, default=datetime.utcnow)
    order_price = db.Column(db.Integer, nullable=False)

    def __init__(self, price):
        self.order_price = price

# Review table
class Review(db.Model):
    __tablename__ = 'review'

    order_id = db.Column(db.Integer, db.ForeignKey('order_food.order_id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)
    review_id = db.Column(db.Integer, primary_key=True)
    review_text = db.Column(db.Text, nullable=False)
    review_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, text):
        self.review_text = text

