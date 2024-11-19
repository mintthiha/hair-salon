from flask_wtf import FlaskForm
from wtforms import DecimalField, IntegerField, StringField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired


class NewAppointmentForm(FlaskForm):
    '''Form that inputs user to create an appointment '''
    date_appoint = DateField('Appointment Date', validators=[DataRequired()], format='%Y-%m-%d')
    slot = SelectField('Slot', choices=[('', 'Select a slot')] + [('9-10', '9-10'), 
    ('10-11', '10-11'), ('11-12', '11-12'), ('12-13', '12-13'),('13-14', '13-14'), 
    ('14-15', '14-15'), ('15-16', '15-16'), ('16-17', '16-17')], coerce=str)
    venue = SelectField('Venue', choices=[('', 'Select a venue')] + [('Room 1', 'Room 1'), 
    ('Room 2', 'Room 2'), ('Room 3', 'Room 3'), ('Room 4', 'Room 4'), ('Room 5', 'Room 5')],
    coerce=str)
    submit = SubmitField('Book!', validators=[DataRequired()])

class NewServiceForm(FlaskForm):
    '''Form that inputs a professional to create a service '''
    service_name = StringField('Service Name', validators=[DataRequired()])
    duration = IntegerField('Duration (hours)', validators=[DataRequired()])
    price = DecimalField('Price', places=2, validators=[DataRequired()])
    materials = StringField('Materials', validators=[DataRequired()])
    submit = SubmitField('Create!', validators=[DataRequired()])