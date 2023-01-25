from flask import request
from app import db
from flask import jsonify

class CRUD():
    #  Get all records
    def get(self, model, schema):
        all_records = model.query.all()
        result = schema(many=True).dump(all_records)
        return jsonify(result)
    
    # Get a record by name
    def get_by_name(self, model, schema, entity, name):
        if entity == 'admin_name':
            record = model.query.filter_by(admin_name=name).first()
        elif entity == 'customer_name':
            record = model.query.filter_by(customer_name=name).first()
        elif entity == 'food_name':
            record = model.query.filter_by(food_name=name).first()
        elif entity == 'order_id':
            record = model.query.filter_by(order_id=name).first()
        elif entity == 'review_id':
            record = model.query.filter_by(review_id=name).first()
        result = schema().dump(record)
        return jsonify(result)
    
    # Get a record by id
    def get_by_id(self, model, schema, id):
        record = model.query.get_or_404(id)
        result = schema().dump(record)
        return jsonify(result)
    
    # Create a record
    def post(self, model, schema):
        if request.is_json:
            data = request.get_json()
            record = model(**data)
            db.session.add(record)
            db.session.commit()
            return { "message": f'{record} has been created successfully.' }
    # Update a record
    def put(self, model, schema, id):
        if request.is_json:
            data = request.get_json()
            record = model.query.get_or_404(id)
            record.update(data)
            db.session.add(record)
            db.session.commit()
            return { "message": f'{record} has been updated successfully.' }
    # Delete a record
    def delete(self, model, schema, id):
        record = model.query.get_or_404(id)
        db.session.delete(record)
        db.session.commit()
        return { "message": f'{record} has been deleted successfully.' }