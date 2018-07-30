import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(__name__)
Bootstrap(app)

@app.route('/')
def get_index():
    return render_template('index.html')

@app.route('/layout')
def get_layout():
    return render_template('base.html')

@app.route('/about')
def get_about():
    return render_template('about.html')

@app.route('/contact')
def get_contact():
    return render_template('contact.html')

@app.route('/sites')
def get_sites():
    return render_template('sites.html')

if __name__=='__main__':
    app.run(debug=True)