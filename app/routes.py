from flask import request, jsonify
from app import app, db
from app.models import Admin
from app.marsh_schema import AdminSchema
import os

@app.route('/register', methods=['POST'])
def register():
    if request.is_json:
        data = request.get_json()
        userData = Admin(
            email= data['email'],
            password= data['password'],
            name= data['name']
        )
        db.session.add(userData)
        db.session.commit()
        return {"message": f'{userData.admin_name} has been registered successfully.' }
    else:
        raise Exception("The request payload is not in JSON format")