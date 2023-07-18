from flask import Blueprint, render_template

# we have set a Blueprint for our flask app
views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('home.html')


# @views.route('/login')
# def login():
#     return render_template('login.html')


# @views.route('/signup')
# def sign_up():
#     return render_template('sign_up.html')
