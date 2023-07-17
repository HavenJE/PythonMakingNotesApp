from flask import Blueprint

# we have set a Blueprint for our flask app
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h5> My Home Page </h5>"