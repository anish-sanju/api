from flask import request
from app import db
from flask import jsonify

class CRUD():
    #  Get all records
    def get(self, model, schema):
        all_records = model.query.all()
        result = schema(many=True).dump(all_records)
        return jsonify(result)
    # Get a single record
    def getById(self, model, schema, table, id):
        record = model.query.filter_by(table=id).first()
        return jsonify(schema(many=False).dump(record))
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