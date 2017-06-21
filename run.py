from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import os
basedir = os.path.abspath(os.path.dirname(__file__))

# create and config app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# create db object and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# sample User. A list of all objects, relationships, and properties are in the schema.
class User(Base):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(128), index=True)
    lastName = db.Column(db.String(128), index=True)
    username = db.Column(db.String(128), index=True, unique=True)

    # relationships go here
    
    def __repr__(self):
        return "<User (name='%s', username='%s'>" % (
            self.firstName + self.lastName, self.username)