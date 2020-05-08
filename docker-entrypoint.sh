#!/bin/bash

export TERM=xterm

if [ ! -d 'logs' ]; then
    mkdir -p logs
    mkdir -p logs/nginx
    mkdir -p logs/app
fi

python3 migrate.py db upgrade

if [ $ENVIRONMENT == 'DEV'] ; then
    sudo cp docker/nginx-dev.conf /etc/nginx/nginx.conf
    screen -dmS APP bash -c 'python3 app.py'
else

    sudo cp docker/nginx-uwsgi.conf /etc/nginx/nginx.conf
    screen -dmS APP bash -c 'uwsgi uwsgi.ini'
fi

sudo nginx

tail -f logs/nginx/access.log -f logs/nginx/error.log
