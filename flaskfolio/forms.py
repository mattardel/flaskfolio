from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField, validators
from flask import request

class ContactForm(Form):
    name=StringField("name", [validators.DataRequired()])
    email=StringField("email", [validators.Email("Please enter a valid email address.")])
    subject=StringField("subject", [validators.DataRequired()])
    message=TextAreaField("message", [validators.DataRequired()])
    submit = SubmitField("send")