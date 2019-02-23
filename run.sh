#!/bin/bash                                                                                  

source venv/bin/activate
sudo uwsgi --http :80 --wsgi-file run.py --callable app --py-autoreload=2

