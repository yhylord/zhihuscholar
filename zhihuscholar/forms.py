# TODO Add length validators
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class RegisterForm(FlaskForm):
    name = StringField('name', [DataRequired()])
    email = StringField('email', [DataRequired()])
    password = PasswordField('password', [DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('repeat')