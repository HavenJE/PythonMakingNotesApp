# This file makes the app folder a python package
# This means, we can import from the above folder and run in inside this file

from flask import Flask

# Define a function that creates Flask app


def create_app():
    app = Flask(__name__)  # __name__ represents the name of the file
    # this encrypt the cookies of session data related to our app
    app.config['SECRET_KEY'] = 'MYSECRETKEY'

    # here, we are declaring that we have some Blueprints for our applications
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
