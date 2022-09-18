from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pass/<int:score>')
def result(score):
    res = ''
    if score>=40:
        res = 'Passed'
    else:
        res = 'Failed'
    exp = {'Score': score, 'Result': res}
    return render_template('result_new.html', marks = exp)

@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        physics = float(request.form['physics'])
        chemistry = float(request.form['chemistry'])
        maths = float(request.form['maths'])
        english = float(request.form['english'])
        computer_science = float(request.form['computer science'])
        total_score = (physics+chemistry+maths+english+computer_science)/5
    
    return redirect(url_for('result', score = total_score))


if __name__ == "__main__":
    app.run(debug = True)