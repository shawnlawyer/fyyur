from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
import babel
import dateutil.parser

from .config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from .blueprints import *

app.register_blueprint(core)
app.register_blueprint(artist)
app.register_blueprint(venue)
app.register_blueprint(show)


@app.before_first_request
def before_first_request_func():

    pass

@app.before_request
def before_request():

    pass
    #db.session.open()

@app.after_request
def after_request(response):

    return response

@app.teardown_request
def teardown_request(error=None):

    db.session.close()

    if error:

        if not app.debug:

            file_handler = FileHandler('logs/app/error.log')
            file_handler.setFormatter(Formatter(
                '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
            app.logger.setLevel(logging.INFO)
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)
            app.logger.info('errors')

def format_datetime(value, format='medium'):
    date = dateutil.parser.parse(str(value))
    if format == 'full':
        format = "EEEE MMMM, d, y 'at' h:mma"
    elif format == 'medium':
        format = "EE MM, dd, y h:mma"
    return babel.dates.format_datetime(date, format, locale='en')


app.jinja_env.filters['datetime'] = format_datetime
