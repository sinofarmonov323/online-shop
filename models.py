from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=True)
    username = db.Column(db.String(100), unique=True, nullable=True)
    password = db.Column(db.String(100), nullable=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), unique=True, nullable=False)
    image = db.Column(db.String(255), nullable=False)
    price = db.Column(db.String(100), nullable=False)
    short_description = db.Column(db.String(300), nullable=False)