from marshmallow import Schema

# Admin Schema
class AdminSchema(Schema):
    class Meta:
        fields = ('admin_id', 'admin_name', 'admin_email', 'admin_password')

# Customer Schema
class CustomerSchema(Schema):
    class Meta: 
        fields = ('customer_id', 'customer_name', 'customer_email', 'customer_password', 'customer_phone')

# Food Schema
class FoodSchema(Schema):
    class Meta:
        fields = ('food_id', 'name', 'description')

# Order_food Schema
class Order_foodSchema(Schema):
    class Meta:
        fields = ('order_id', 'time', 'price')


# Review Schema
class ReviewSchema(Schema):
    class Meta:
        fields = ('review_id', 'customer_id', 'food_id', 'rating', 'comment')

