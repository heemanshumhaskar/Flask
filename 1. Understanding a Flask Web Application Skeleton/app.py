# Importing modules from Flask library.
from flask import Flask

# Creating an Object and calling Flask constructor.
app = Flask(__name__)

# Using a decorator to bind a URL.
@app.route('/')
def home():
    return "Welcome to my system! Make yourself comfortable."

# Using a decorator to bind a different URL.
@app.route('/members')
def members():
    return "Hey! Welcome to the inner circle."

if __name__=='__main__':
    app.run(debug=True)