from app import app, db

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

