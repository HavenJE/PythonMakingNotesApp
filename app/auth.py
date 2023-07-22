from flask import Blueprint, render_template, request, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

# we have set a Blueprint for our flask app
auth = Blueprint('auth', __name__)

# we need to make sure the login & sign_up routes both accept GET & POST requests, so we use => methods=['GET', 'POST']


@auth.route('/login', methods=['GET', 'POST'])
def login():
    # data = request.form  # To get the info we sent on the login form page.
    # print(data)
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return "<p> You are logged out  </p>"


@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        email = request.form.get('email')
        password = request.form.get('password')

        if len(firstName) < 3:
            flash("Your First Name must be greater than 2 characters!",
                  category='error')
        elif len(lastName) < 3:
            flash("Your Last Name must be greater than 2 characters!",
                  category='error')
        elif len(email) < 4:
            flash("Your email must be greater than 3 characters!", category='error')
        elif len(password) < 4:
            flash("Your Password must be greater than 3 characters!",
                  category='error')
        else:
            # To create a new user 
            new_user = User(firstName=firstName, lastName=lastName, email=email, password=password)
            # add user to data base
            flash("Account created!", category='success')
    return render_template('sign_up.html')
