# Import flask and template operators
from flask import Flask, render_template, redirect, url_for



# cms checks configuration file for all modules
# which should be updated to give updated content
# Content updated approximately daily
# for the home page for now this is just the game 
# from content_mangement import cms, cms_stream
# content = cms.load()
# tweets = cms_stream.load('tweets')

# standin
content = {'games':[['2-24-19','Buffalo', 'Pittsburgh'],
                    ['2-24-19', 'Chicago', 'Philadelphia']]}


# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')


@app.route("/")
def gohome():
    return redirect(url_for('home'))

# by modules and controllers
@app.route("/home")
def home():
    #return render_template('home.html')
    return render_template('home.html', CONTENT=content)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_auth.controllers import mod_auth as auth_module

# Register blueprint(s)
app.register_blueprint(auth_module)
# app.register_blueprint(xyz_module)
# ..


