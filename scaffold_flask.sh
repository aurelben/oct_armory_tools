#!/bin/bash

echo "set up dirs and files"
mkdir ./app
mkdir ./app/templates
mkdir ./app/static

touch run.py
touch config.py
touch ./app/__init__.py

echo "start virutual env"
virtualenv env

echo "install flask, sqlalchemy and flask-wtform"
env/bin/pip install flask
env/bin/pip install flask-sqlalchemy
env/bin/pip install flask-wtf

echo Create a HTTP 404 Error page
touch ./app/templates/404.html

