# Reference: https://pythonhow.com/building-a-website-with-python-flask/

# from flask import Flask, render_template
import matplotlib as mpl
mpl.use('Agg')
from flask import Flask, request, render_template, url_for, make_response
import string
from time import strftime, localtime
from raspberry import collectdata, saveimage

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/setcookie/', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
       name = request.form['nm']
       s = name.translate(str.maketrans(',.!', 3*' ')).replace(' ', '_')
       ctime = strftime("%Y_%m_%d-%H_%M_%S", localtime())
   resp = make_response(render_template('go.html'))
   resp.set_cookie('filename', ctime+'_'+s)
   resp.set_cookie('name', name)
   return resp

@app.route('/go/')
def go():
    name = request.cookies.get('name')
    return render_template('go.html', name=name)

@app.route('/start/')
def start():
    name = request.cookies.get('name')
    filename = request.cookies.get('filename')
    collectdata(filename)
    saveimage(name, filename)
    return render_template('start.html', name=name, filename=filename)

@app.route('/results/')
def results():
    name = request.cookies.get('name')
    filename = request.cookies.get('filename')
    return render_template('results.html', name=name, filename=filename)



if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    # app.run(debug=True)
    app.run(debug=True, host='0.0.0.0')
