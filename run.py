#!/usr/bin/env
'''
   https://www.digitalocean.com/community/tutorials/
   how-to-structure-large-flask-applications#our-
   choices-in-this-article
'''

from app import app
if (__name__ == '__main__'):
    app.run(host='127.0.0.1', port=80, debug=True)
