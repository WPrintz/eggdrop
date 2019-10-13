# https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog/03-Forms-and-Validation

from flask import Flask, render_template, url_for, flash, redirect
from forms import EntryForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/recording/")
def recording(form):
    return render_template('recording.html', form=form)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = EntryForm()
    if form.validate_on_submit():
        return redirect(url_for('recording', form=form))
        # if form.text.data == '1234':
        #     flash('Thats the ticket!', 'success')
        #     return redirect(url_for('home'))
        # else:
        #     flash('Starting recording', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0')
