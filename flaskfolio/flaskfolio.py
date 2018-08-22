import os
import sqlite3

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask_bootstrap import Bootstrap
#from flaskfolio.forms import ContactForm
from flask_mail import Message, Mail
from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField, validators

mail = Mail()

app = Flask(__name__)
app.config.from_object(__name__)
Bootstrap(app)
app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.zoho.com',
    MAIL_PORT = 465,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'matt@mattardel.com',
    MAIL_PASSWORD = 'H0pp3rla$4dayZ',
    MAIL_DEFAULT_SENDER = 'matt@mattardel.com'
))

app.secret_key = 'flask_form_2010'

MAIL_DEFAULT_SENDER = 'matt@mattardel.com'

mail.init_app(app)

class ContactForm(Form):
    name=StringField("name", [validators.DataRequired()])
    email=StringField("email", [validators.Email("Please enter a valid email address.")])
    subject=StringField("subject", [validators.DataRequired()])
    message=TextAreaField("message", [validators.DataRequired()])
    submit = SubmitField("send")

@app.route('/')
def get_index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm(request.form)

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required to send a message!')
            return render_template('contact.html', form=form)
        else:
            msg = Message(form.subject.data, recipients=["matt@mattardel.com"])
            msg.body = """
                 From: %s <%s>
                 %s
                 """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return render_template('contact.html', success=True)
    elif request.method == 'GET':
        return render_template('contact.html', form=form)

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
    app.run(host='0.0.0.0', debug=True)