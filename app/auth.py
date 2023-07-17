from flask import Blueprint

# we have set a Blueprint for our flask app
auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return "<p> My Login Page </p>"


@auth.route('/logout')
def logout():
    return "<p> You are logged out  </p>"


@auth.route('/signup')
def sign_up():
    return "<p> sign-up  </p>"
