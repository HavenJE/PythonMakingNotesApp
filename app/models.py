# This where we create our database models
# we need a db model of 1. user 2.notes

# to import the db object from the app package (which is the app folder) where we store our package in the __init_.py file
from . import db
# this is a customer class that help us log users in
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # we storing a foreign key for the child object that reference the parent object
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# db.model is a layout/blueprint for an object that is going to be stored in your database


class User(db.Model, UserMixin):
    # here we define all the columns in this table
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    # building a relationship with the Class Notes to enable a user showing his notes
    notes = db.relationship('Note')
