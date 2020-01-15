# Reference: https://pythonhow.com/building-a-website-with-python-flask/

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/reset/')
def reset():
    #TODO: Figure out how to clear memory
    return render_template('home.html')

@app.route('/go/')
def go():
    return render_template('go.html')

@app.route('/results/')
def results():
    return render_template('results.html')


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
    # app.run(debug=True, host='0.0.0.0')
