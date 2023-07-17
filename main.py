# The file we run to start the app by importing the app folder package and grab the create_app function that we defined and use it to create a flask app and run it. 

from app import create_app

app = create_app()

# only if we run this file, then execute the app.run line 
if __name__ == '__main__':
    app.run(debug=True) # This line runs our flask app 