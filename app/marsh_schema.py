from marshmallow import Schema

class AdminSchema(Schema):
    class Meta:
        fields = ('admin_id', 'name', 'email', 'password')