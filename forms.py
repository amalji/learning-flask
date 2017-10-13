from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
    first_name = StringField('First Name', validators=[DataRequired("Please enter your First Name")])
    last_name = StringField('Last Name', validators=[DataRequired("Please enter your Last Name")])
    email = StringField('Email', validators=[DataRequired("Please enter your email"), Email("Please enter your email in the correct format!")])
    password = PasswordField('Password', validators=[DataRequired("Please enter your password"), Length(min=8, message="Password should be atleast 8 characters long.")])
    submit = SubmitField('Sign Up')

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired("Please enter your email"), Email("Please enter your email in the correct format")])
    password = PasswordField('Password', validators=[DataRequired("Please enter your password")])
    submit = SubmitField('Signin')
