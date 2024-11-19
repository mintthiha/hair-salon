from flask_login import current_user
from flask import Blueprint, flash, render_template, request
from HairSalon.qdb.database_ import db
from HairSalon.report.forms import NewReportForm, EmployeeRespondReportForm


report = Blueprint('report', __name__, template_folder='templates', static_folder='static')


@report.route('/create/report/<int:appointment_id>/<int:customer_id>', methods=['GET', 'POST'])
def create_report(appointment_id, customer_id):
    '''Creates a report using the NewReportForm if the appointment belongs to the user'''
    report_form = NewReportForm()
    if request.method == 'POST':
        if report_form.validate_on_submit() and current_user._User__user_id == customer_id:
            feedback_customer = report_form.feedback_customer.data
            db.add_new_report_for_customer(appointment_id, feedback_customer)
            db.update_log_add(current_user._User__user_name,
                              current_user._User__user_type,
                              'SALON_REPORT') 
            flash(("report created successfully!", "success"))
            
        else:
            print("Form validation errors:", report_form.errors)
            flash(("This appointment doesn't belong to you", "error"))
     
    return render_template('create_report.html', report_form = report_form, appointment_id = appointment_id, customer_id = customer_id)

@report.route('/reply/report/<int:appointment_id>/<int:service_id>', methods=['GET', 'POST'])
def reply_report(appointment_id, service_id):
    '''Replies to a customer's report using the EmployeeRespondReportForm 
    for professionals that provided the service and updates the log'''
    report = db.get_report_by_appointment_id(appointment_id)
    report_form = EmployeeRespondReportForm()
    service = db.get_service(service_id)
    if request.method == 'POST':
        if report_form.validate_on_submit() and current_user._User__user_id == service['employee_id']:
            feedback_employee = report_form.feedback_employee.data
            db.reply_report_for_employee(appointment_id, feedback_employee)
            db.update_log_update(current_user._User__user_name, 
                                     current_user._User__user_type, 
                                     'SALON_REPORT') 
            flash(("replied successfully!", "success"))
            
        else:
            print("Form validation errors:", report_form.errors)
            flash(("This report is not dedicated to you", "error"))
     
    return render_template('reply_report.html', report_form = report_form, appointment_id = appointment_id, service_id = service_id, report = report)

@report.route('/reports')
def all_reports():
    '''Gets all reports from the database and displays them using report.html'''
    reports = db.get_reports()
    return render_template('report.html', reports = reports, current_user = current_user)

@report.route('/appointments')
def all_appointments():
    '''Gets all appointments from the database and displays them using all_appointments.html'''
    appointments = db.get_appointments()
    return render_template('all_appointments.html',appointments=appointments,current_user=current_user)