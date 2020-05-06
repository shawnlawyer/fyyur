import os
from envs import env

basedir = env('HOME')


class Config(object):
    """Flask config variables"""

    DEBUG = env('DEBUG')

    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
        env('POSTGRES_USER'),
        env('POSTGRES_PASSWORD'),
        env('POSTGRES_HOST'),
        env('POSTGRES_PORT'),
        env('POSTGRES_DB')
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = ('SQLALCHEMY_TRACK_MODIFICATIONS')

    SECRET_KEY = env('APP_SECRET_KEY')

    SESSION_COOKIE_SECURE = env('SESSION_COOKIE_SECURE')

    SESSION_COOKIE_NAME = env('SESSION_COOKIE_NAME')

    WTF_CSRF_TIME_LIMIT = env('CSRF_TIME_LIMIT')
