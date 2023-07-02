# Everythingh here is about createing routes and views for the differente tamplates;
# we reuse or inherit code as seen from 'base.html' and the subsequent fetching from those templates.
# Pay attention to the URL linking syntax (Jinja)

# We have install a template to 'static'.
# This template has all necessary dependencies.
# We reuse the original code in there for base.html
# then we use our templates using the {%block/endblock%} syntax
# there we add our own code. That will be matched with the base.html
# remember {% extends "base.html"%} to load base.html and match our pages

import os
import json
from flask import Flask, render_template  # first import Class from module

# instance of the class passing __name__ (provides current module or script)
app = Flask(__name__)


@app.route("/")  # ROUTE help direct the files to Flask | @(decorator)
def index(): # VIEW
    return render_template('index.html') # imported method from flask

@app.route("/about")
def about():
    data = []
    with open('data/characters.json', 'r') as json_data:
        data = json.load(json_data)
    return render_template('about.html', page_title='About', about_content=data)

@app.route('/contact')
def contact():
    return render_template('contact.html', page_title="Contact")

@app.route('/careers')
def careers():
    return render_template('careers.html', page_title="Careers")

# This condition ensures that the subsequent
# code block is only executed when run.py is the main entry point.
if __name__ == "__main__":  # when executed directly
    app.run(
        host=os.environ.get('IP', '0.0.0.0'),  # replace if not found
        port=int(os.environ.get('PORT', '5000')),  # replace if not found
        debug=True  # caution security flaw if True
    )