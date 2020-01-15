# Reference: https://pythonhow.com/building-a-website-with-python-flask/

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/stuff/')
def stuff():
    return render_template('stuff.html')


if __name__ == '__main__':
    app.run(debug=True)
