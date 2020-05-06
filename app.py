# -------------------------------------------------------------------------- #
# Imports
# -------------------------------------------------------------------------- #

import logging
from logging import Formatter, FileHandler
from envs import env
from app import app, db

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

# -------------------------------------------------------------------------- #
# Launch.
# -------------------------------------------------------------------------- #

if __name__ == '__main__':
    app.run(
        debug=env('DEBUG', False),
        host='0.0.0.0',
        port=env('APP_PORT', 5000)
    )
