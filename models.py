from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60),nullable=False)
    firstname = db.Column(db.String(60))
    bookingdetails = db.relationship('Bookingdetails', backref='user', lazy=True)    

class Bookingdetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bookingdate = db.Column(db.String(150))
    bookingtime = db.Column(db.String(150))
    destination = db.Column(db.String(150))
    phoneno = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
        