from app import db
from app import app
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)

    fname = db.Column(db.String(128), index = True, unique = False)
    lname = db.Column(db.String(128), index = True, unique = False)
    nickname = db.Column(db.String(128), index = True, unique = False)

    username = db.Column(db.String(128), index = True, unique = False)
    password = db.Column(db.String(1024), index = True, unique = False)

    email = db.Column(db.String(1024), index = True, unique = False)

    permissions = db.Column(db.String(1024), index = True, unique = False)

    def set_password(self, pwd):
        self.password = generate_password_hash(pwd)
        db.session.commit()

    def check_password(self, pwd):
        return check_password_hash(self.password, pwd)

    def add_permission(self, permission):
        if not self.check_permission(permission):
            self.permissions += permission + ','
        db.session.commit()

    def remove_permission(self, permission):
        self.permissions = self.permissions.replace(',' + permission + ',', ',')
        db.session.commit()

    def check_permission(self, permission):
        contains_permission = False
        for p in self.permissions.split(','):
            contains_permission = contains_permission or (p == permission)
        return contains_permission
    
