from flask_wtf import FlaskForm
from wtforms import DateField, FileField, PasswordField, StringField, SubmitField, EmailField, IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired

#May need more fields later
class UserForm(FlaskForm):
    '''Form that inputs user to create a new account '''
    user_type = SelectField('User Type', choices = [('client', 'Client'), ('professional', 'Professional'), ('user', 'Admin_User'), ('appoint', 'Admin_Appoint')])
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    user_image = FileField('Upload File',  validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()]) 
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    age = IntegerField('Integer Field', validators=[DataRequired()])
    speciality = StringField('Speciality', validators=[DataRequired()])
    submit = SubmitField('Add!', validators=[DataRequired()])

class WarningForm(FlaskForm):
    '''Form that inputs user to create a new warning '''
    message = TextAreaField('Enter Warning Message', validators=[DataRequired()])
    submit = SubmitField('Warn')

class AppointmentModificationForm(FlaskForm):
    '''Form that inputs user to modify an appointment '''
    date_appoint = DateField('Appointment Date', validators=[DataRequired()], format='%Y-%m-%d')
    slot = SelectField('Slot', choices=[('', 'Select a slot')] + [('9-10', '9-10'), ('10-11', '10-11'), ('11-12', '11-12'), ('12-13', '12-13'), ('13-14', '13-14'), ('14-15', '14-15'), ('15-16', '15-16'), ('16-17', '16-17')], coerce=str)
    venue = SelectField('Venue', choices=[('', 'Select a venue')] + [('Room 1', 'Room 1'), ('Room 2', 'Room 2'), ('Room 3', 'Room 3'), ('Room 4', 'Room 4'), ('Room 5', 'Room 5')], coerce=str)
    submit = SubmitField('Update!')


class AddAppointmentForm(FlaskForm):
    '''Form that inputs user to add a new appointment '''
    date_appoint = DateField('Appointment Date', validators=[DataRequired()], format='%Y-%m-%d')
    slot = SelectField('Slot', choices=[('', 'Select a slot')] + [('9-10', '9-10'), ('10-11', '10-11'), ('11-12', '11-12'), ('12-13', '12-13'), ('13-14', '13-14'), ('14-15', '14-15'), ('15-16', '15-16'), ('16-17', '16-17')], coerce=str)
    venue = SelectField('Venue', choices=[('', 'Select a venue')] + [('Room 1', 'Room 1'), ('Room 2', 'Room 2'), ('Room 3', 'Room 3'), ('Room 4', 'Room 4'), ('Room 5', 'Room 5')], coerce=str)
    submit = SubmitField('Add Appointment!')
    
class ReportModificationForm(FlaskForm):
    '''Form that inputs user to modify a report '''
    status = StringField('Status', validators=[DataRequired()])
    date_report = DateField('Appointment Date', validators=[DataRequired()], format='%Y-%m-%d')
    feedback_employee = StringField('Employee Feedback', validators=[DataRequired()])
    feedback_customer = StringField('Customer Feedback', validators=[DataRequired()])
    submit = SubmitField('Update Report!')
    
class AddReportForm(FlaskForm):
    '''Form that inputs user to add a new report '''
    status = StringField('Status', validators=[DataRequired()])
    date_report = DateField('Appointment Date', validators=[DataRequired()], format='%Y-%m-%d')
    feedback_employee = StringField('Employee Feedback', validators=[DataRequired()])
    feedback_customer = StringField('Customer Feedback', validators=[DataRequired()])
    submit = SubmitField('Add this Report')
