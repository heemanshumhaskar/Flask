# Importing modules from Flask library.
from flask import Flask, redirect, url_for

# Creating an Object and calling Flask constructor.
app = Flask(__name__)

# Using a decorator to bind a URL.
@app.route('/')
def home():
    return "Welcome to the system."

# Using a decorator to bind a dynamic URL.
@app.route('/pass/<int:score>')
def passed(score):
    # Displays a message with the score.
    return f"Congratulations! You have passed with a score of {score}."

@app.route('/fail/<int:score>')
def failed(score):
    return f"Sorry, you didn't make it. :("

@app.route('/result/<int:score>')
def result(score):
    result = ""
    if score > 40:
        result = "passed"
        # Displaying/redirecting the user to a different page.
        return redirect(url_for(result, score = score))
    else:
        result = 'failed'
        return redirect(url_for(result, score = score))

if __name__ == "__main__":
    app.run(debug = True)