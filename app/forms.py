from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    email = StringField('Email Address:', validators=[DataRequired(), Email()])
    password = PasswordField('Password:', validators=[DataRequired()])
    password2 = PasswordField('Re-Enter Password:', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register!')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Invalid Username!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('You already registered!')


class EditProfileForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    about_me = TextAreaField('About Me:', validators=[Length(min=0, max=250)])
    submit = SubmitField('Update Profile!')
