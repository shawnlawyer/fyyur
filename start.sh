#!/bin/bash

export TERM=xterm

if [ ! -d 'logs' ]; then
    mkdir -p logs
fi

# For Nginx logs
if [ ! -d 'logs/nginx' ]; then
    mkdir -p logs/nginx
fi

# For app logs
if [ ! -d 'logs/app' ]; then
    mkdir -p logs/app
fi

python3 migrate.py db upgrade

screen -dmS APP bash -c 'python3 app.py'

nginx

tail -f logs/nginx/access.log -f logs/nginx/error.log
