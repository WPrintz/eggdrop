from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class EntryForm(FlaskForm):
    text = StringField('Experiment Description',
                        validators=[DataRequired()])
    submit = SubmitField('Submit')
