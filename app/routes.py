from flask import request, jsonify
from app import db, app
from app.models import Admin, Customer, Food, Order_food
from app.marsh_schema import AdminSchema, CustomerSchema, FoodSchema, Order_foodSchema
from app.crud import CRUD
import os

crud = CRUD()

# Create a route for the home page
@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to the API'})

# Routes for Admin
@app.route('/admin', methods=['GET', 'POST'])
def get_post_admin():
    if request.method == 'GET':
        return crud.get(Admin, AdminSchema)
    elif request.method == 'POST':
        return crud.post(Admin, AdminSchema)
    
@app.route('/admin/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_put_delete_admin(id):
    if request.method == 'GET':
        return crud.getById(Admin, AdminSchema, id)
    elif request.method == 'PUT':
        return crud.put(Admin, AdminSchema, id)
    elif request.method == 'DELETE':
        return crud.delete(Admin, AdminSchema, id)

# Route for getting admin by name
@app.route('/admin/<string:admin_name>', methods=['GET'])
def get_admin_by_name(admin_name):
    return crud.get_by_name(Admin, AdminSchema, 'admin_name', admin_name)

# Routes for Customer
@app.route('/customer', methods=['GET', 'POST'])
def get_post_customer():
    if request.method == 'GET':
        return crud.get(Customer, CustomerSchema)
    elif request.method == 'POST':
        return crud.post(Customer, CustomerSchema)

# Route for getting customer by name
@app.route('/customer/<string:customer_name>', methods=['GET'])
def get_customer_by_name(customer_name):
    return crud.get_by_name(Customer, CustomerSchema, 'customer_name', customer_name)

# Routes for Food
@app.route('/food', methods=['GET', 'POST'])
def get_post_food():
    if request.method == 'GET':
        return crud.get(Food, FoodSchema)
    elif request.method == 'POST':
        return crud.post(Food, FoodSchema)

@app.route('/food/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_put_delete_food(id):
    if request.method == 'GET':
        return crud.getById(Food, FoodSchema, id)
    elif request.method == 'PUT':
        return crud.put(Food, FoodSchema, id)
    elif request.method == 'DELETE':
        return crud.delete(Food, FoodSchema, id)

# Routes for Order_food
@app.route('/order_food', methods=['GET', 'POST'])
def get_post_order_food():
    if request.method == 'GET':
        return crud.get(Order_food, Order_foodSchema)
    elif request.method == 'POST':
        return crud.post(Order_food, Order_foodSchema)

@app.route('/order_food/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_put_delete_order_food(id):
    if request.method == 'GET':
        return crud.getById(Order_food, Order_foodSchema, id)
    elif request.method == 'PUT':
        return crud.put(Order_food, Order_foodSchema, id)
    elif request.method == 'DELETE':
        return crud.delete(Order_food, Order_foodSchema, id)

# Routes for Review
@app.route('/review', methods=['GET', 'POST'])
def get_post_review():
    if request.method == 'GET':
        return crud.get(Review, ReviewSchema)
    elif request.method == 'POST':
        return crud.post(Review, ReviewSchema)

@app.route('/review/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_put_delete_review(id):
    if request.method == 'GET':
        return crud.getById(Review, ReviewSchema, id)
    elif request.method == 'PUT':
        return crud.put(Review, ReviewSchema, id)
    elif request.method == 'DELETE':
        return crud.delete(Review, ReviewSchema, id)


# http://127.0.0.1:5000/admin throws 503 error
# How to fix it?
