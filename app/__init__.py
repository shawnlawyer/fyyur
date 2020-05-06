from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from .config import Config

import babel
import dateutil.parser

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from .blueprints import *

app.register_blueprint(core)
app.register_blueprint(artist)
app.register_blueprint(venue)
app.register_blueprint(show)


def format_datetime(value, format='medium'):
    date = dateutil.parser.parse(str(value))
    if format == 'full':
        format = "EEEE MMMM, d, y 'at' h:mma"
    elif format == 'medium':
        format = "EE MM, dd, y h:mma"
    return babel.dates.format_datetime(date, format, locale='en')


app.jinja_env.filters['datetime'] = format_datetime

