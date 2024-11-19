from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NewReportForm(FlaskForm):
    '''Form that inputs user to create a report '''
    feedback_customer = StringField('Customer feedback', validators=[DataRequired()]) 
    submit = SubmitField('Submit!', validators=[DataRequired()])

class EmployeeRespondReportForm(FlaskForm):
    '''Form that inputs professional to reply a report '''
    feedback_employee = StringField('Employee feedback', validators=[DataRequired()]) 
    submit = SubmitField('Submit!', validators=[DataRequired()])
