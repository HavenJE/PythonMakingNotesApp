# This file makes the app folder a python package
# This means, we can import from the above folder and run in inside this file

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# To define a database where db is an object
db = SQLAlchemy()
# To name the db
DB_NAME = "database.db"

# Define a function that creates Flask app


def create_app():
    app = Flask(__name__)  # __name__ represents the name of the file
    # this encrypt the cookies of session data related to our app
    app.config['SECRET_KEY'] = 'MYSECRETKEY'
    # We are saying to flask that our SQLALCHEMY database is stored in this location
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)  # now we initialize our database with our flask app

    # here, we are declaring that we have some Blueprints for our applications
    from .views import views
    from .auth import auth

    # Registering our blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    # create_database(app)
    with app.app_context():
        db.create_all()

    return app

# function to create a database if not created yet


# def create_database(app):
#     # using the path model to check if the database exists, if not, then create it
#     if not path.exists('app/' + DB_NAME):
#         db.create_all(app=app)
#         print('Created Database!')
