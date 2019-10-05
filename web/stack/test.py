# https://stackoverflow.com/questions/42601478/flask-calling-python-function-on-button-onclick-event

from flask import Flask, render_template, request, redirect, url_for
import numpy as np
from getdata import getdata

import os

DATA_FOLDER = os.path.join('static', 'images')

app = Flask(__name__)


app.config['DATA_FOLDER'] = DATA_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/SomeFunction')
def SomeFunction():
    print('** Running SomeFunction')
    t, s = getdata.get()
    print('{} == {}'.format(t, s))
    return index()

@app.route('/handle_data', methods=['POST'])
def handle_data():
    print('** Running handle_data')
    form_input = request.form['form_input']
    print(form_input)
    n = np.zeros((5,5))
    filename = 'Hello World'  # TODO: replace filename with underscores
    # TODO: Call recording methods
    # np.savetxt('form_input-{}.txt'.format(form_input), n)  # TODO: Replace with saved output
    return render_template('recording.html', filename=form_input)

@app.route('/show_results', methods=['GET'])
def show_results():
    print('** Running show_results')
    full_filename = os.path.join(app.config['DATA_FOLDER'], 'rocket.jpg')
    return render_template('results.html', results_image=full_filename)
    # return redirect(url_for('results.html', results_image=full_filename))

@app.route('/reset', methods=['GET'])
def reset():
    print('** Running reset')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
