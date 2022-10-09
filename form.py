from ast import Sub
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class Registration(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password1 = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=20)])
    password2 = PasswordField('Type password again', validators=[DataRequired(), EqualTo('password1')])
    #role = SelectField('Role', choices=[(1, 'User'), (2, 'Admin')], validators=[DataRequired()])
    submit = SubmitField('Sign up')

class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=20)])
    submit = SubmitField('Sign in')