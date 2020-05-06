from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField
from wtforms import DateTimeField, BooleanField
from wtforms.validators import DataRequired, URL, NumberRange

class form(FlaskForm):
    artist_id = StringField(
        'artist_id', validators=[DataRequired(), NumberRange()]
    )
    venue_id = StringField(
        'venue_id', validators=[DataRequired(), NumberRange()]
    )
    start_date = DateTimeField(
        'start_date'
    )
    start_time = DateTimeField(
        'start_time'
    )
