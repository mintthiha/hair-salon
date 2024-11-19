from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, SelectField, IntegerField, SubmitField, FileField
from wtforms.validators import DataRequired


class NewUserForm(FlaskForm):
    '''Form that inputs user to create a new account '''
    user_type = SelectField('User Type', choices = [('client', 'Client'), ('professional', 'Professional')])
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    user_image = FileField('Upload File',  validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()]) 
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    age = IntegerField('Integer Field', validators=[DataRequired()])
    speciality = StringField('Speciality', validators=[DataRequired()])
    submit = SubmitField('Register!', validators=[DataRequired()])

class LoginForm(FlaskForm):
    '''Form that inputs user their account credentials to log in the website '''
    user_name = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In', validators=[DataRequired()])

class PasswordModifForm(FlaskForm):
    '''Form that inputs user a new password to replace the old one '''
    password = StringField('New Password', validators=[DataRequired()])
    submit = SubmitField('Update Password', validators=[DataRequired()])