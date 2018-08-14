from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField, validators
from flask import request

class ContactForm(Form):
    name=StringField("name", [validators.DataRequired("Please enter your name.")])
    email=StringField("email", [validators.DataRequired("Please enter your email address."), [validators.Email("Please enter your email address.")]])
    subject=StringField("subject", [validators.DataRequired("Please enter a subject.")])
    message=TextAreaField("message", [validators.DataRequired("Please enter a message.")])
    submit = SubmitField("send")