# -------------------------------------------------------------------------- #
# Imports
# -------------------------------------------------------------------------- #
import logging
import os
from envs import env
from logging import Formatter, FileHandler

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from config import Config
from blueprints import venue, show, artist

# -------------------------------------------------------------------------- #
# App Config.
# -------------------------------------------------------------------------- #

from app import app

from models import Artist,Show,Venue
# -------------------------------------------------------------------------- #
# Blueprints register.
# -------------------------------------------------------------------------- #

app.register_blueprint(artist)
app.register_blueprint(venue)
app.register_blueprint(show)


# -------------------------------------------------------------------------- #
# Filters.
# -------------------------------------------------------------------------- #




# -------------------------------------------------------------------------- #
# Controllers.
# -------------------------------------------------------------------------- #

@app.route('/')
def index():
    return render_template('pages/home.html')


# -------------------------------------------------------------------------- #
# Errors and Logs.
# -------------------------------------------------------------------------- #

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('logs/app/error.log')
    file_handler.setFormatter(Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

# -------------------------------------------------------------------------- #
# Launch.
# -------------------------------------------------------------------------- #

if __name__ == '__main__':
    app.run(
        debug=env('DEBUG', False),
        host='0.0.0.0',
        port=env('APP_PORT', 5000)
    )
