# Reference: https://pythonhow.com/building-a-website-with-python-flask/

# from flask import Flask, render_template
from flask import Flask, request, render_template, url_for, redirect, make_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/setcookie/', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
       experiment = request.form['nm']
       #TODO: Add date to experiment name
   resp = make_response(render_template('go.html'))
   resp.set_cookie('name', experiment)
   return resp

@app.route('/reset/')
def reset():
    #TODO: Figure out how to clear memory
    return render_template('home.html')

@app.route('/go/')
def go():
    name = request.cookies.get('name')
    return render_template('go.html', name=name)

@app.route('/start/')
def start():
    name = request.cookies.get('name')
    #TODO: Kickoff measurement
    return render_template('start.html', name=name)

@app.route('/results/')
def results():
    return render_template('results.html')


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
    # app.run(debug=True, host='0.0.0.0')
