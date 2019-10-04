# https://stackoverflow.com/questions/42601478/flask-calling-python-function-on-button-onclick-event

from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

import numpy as np
from getdata import getdata

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/SomeFunction')
def SomeFunction():
    t, s = getdata.get()
    print('{} == {}'.format(t, s))
    return "Nothing"


@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['projectFilepath']
    print(projectpath)
    n = np.zeros((5,5))
    np.savetxt('projectpath-{}.txt'.format(projectpath), n)
    return render_template('index.html')


if __name__ == '__main__':
   app.run()
