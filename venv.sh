#/bin/bash

set -x

virtualenv venv --python=/usr/bin/python3
source venv/bin/activate
pip3 install uwsgi
pip3 install flask
pip3 install Flask-WTF
