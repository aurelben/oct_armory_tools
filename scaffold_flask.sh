#!/bin/bash

echo "set up dirs and files"
mkdir ./project
mkdir ./project/templates
mkdir ./project/static

touch ./project/run.py
touch ./project/config.py
touch ./project/__init__.py
touch setup.py
touch requirements.txt

echo "start virutual env"
virtualenv env

echo "install flask, sqlalchemy and flask-wtform"
env/bin/pip install flask
env/bin/pip install flask-sqlalchemy
env/bin/pip install flask-wtf

echo Create a HTTP 404 Error page
touch ./project/app/templates/404.html

