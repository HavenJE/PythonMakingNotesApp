from flask import Blueprint, render_template

# we have set a Blueprint for our flask app
auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return "<p> You are logged out  </p>"


@auth.route('/signup')
def sign_up():
    return render_template('sign_up.html')
