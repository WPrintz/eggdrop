# Reference: https://pythonhow.com/building-a-website-with-python-flask/

# from flask import Flask, render_template
from flask import Flask, request, session, render_template, url_for, flash, redirect
from forms import EntryForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '4d612c2badbe0325280051d8ee4dc6'

# @app.route('/')
# def home():
#     return render_template('home.html')

@app.route("/", methods=['GET', 'POST'])
def home():
    form = EntryForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            form_data = {"input": form}
            session[data] = form_data
            return redirect(url_for('go'))
    elif request.method == 'GET':
        return render_template('home.html', form=form)

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
