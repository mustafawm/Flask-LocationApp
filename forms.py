from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(Form):
    # inherits From class
    firstname = StringField('First name', validators=[DataRequired()])
    lastname = StringField('Last name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email('Please enter a valid email address')])
    password = PasswordField('Password', validators=[DataRequired('Please enter a strong password'), Length(min=6, message="Password must be 6 or more charachters long")])
    submit = SubmitField('Sign up')
