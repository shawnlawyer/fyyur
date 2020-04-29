#!/bin/bash

# For logs
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

nginx
