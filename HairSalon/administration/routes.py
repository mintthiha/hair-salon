''''''
import os
from flask import Blueprint, redirect, render_template, flash, request, url_for
from markupsafe import escape
from werkzeug.utils import secure_filename
from flask_login import current_user
from flask_bcrypt import Bcrypt
from HairSalon.qdb.database_ import db
from HairSalon.config import ConfigDev
from HairSalon.administration.forms import AddAppointmentForm, AddReportForm, AppointmentModificationForm, ReportModificationForm, UserForm, WarningForm
b = Bcrypt()

administration = Blueprint('administration',
                           __name__, 
                           template_folder='templates', 
                           static_folder='static')

@administration.route('/administration/user/home')
def admin_home():
    '''Renders the admin_home.html file '''
    return render_template('admin_home.html')

@administration.route('/administration/user/members')
def members():
    '''Gets all users from the database and displays them using members.html '''
    membersdb = db.get_users()
    return render_template('members.html', members = membersdb)


#All methods for Admin_user and Admin_super:
@administration.route('/administration/user/members/add', methods=['GET', 'POST'])
def add_member():
    ''' This method is to register a new user admin side using the UserForm '''
    user_form = UserForm()
    if request.method == 'POST':
        if user_form.validate_on_submit():
            user_type = user_form.user_type.data
            username = user_form.username.data
            email = user_form.email.data
            password = user_form.password.data
            user_image = user_form.user_image.data
            filename = secure_filename(user_image.filename)
            user_image.save(os.path.join(ConfigDev.UPLOAD_FOLDER, filename))
            hashed_password = b.generate_password_hash(password).decode('utf-8')
            phone_number = user_form.phone_number.data
            address = user_form.address.data
            age = user_form.age.data
            speciality = user_form.speciality.data
            users = db.get_user(user_form.username.data)
            if users == []:
                if(db.add_new_member(user_type, username, email, hashed_password, filename, phone_number, address, age, speciality)):
                    db.update_log_add(current_user._User__user_name, current_user._User__user_type, 'SALON_USER')
                    flash(("You added this user successfully!", "success"))
                    return redirect(url_for('administration.admin_home'))
                else:
                    flash(("One of the fields resulted in an error. Try again!", "error"))
            else:
                flash(("This username is already taken!", "error"))
        else:
            print("Form validation errors:", user_form.errors)
            flash(("Registration failed, try again.", "error"))
    return render_template('add_user_admin.html', user_form = user_form)

        
    
@administration.route('/administration/user/members/delete/<int:user_id>')
def delete_member(user_id):
    '''Deletes the member corresponding to the ID from the databse and updates the log '''
    my_user_id = escape(user_id)
    db.delete_user(my_user_id)
    db.update_log_delete(current_user._User__user_name, current_user._User__user_type, 'SALON_USER')
    flash(("You have deleted a member Successfully!", "success"))
    return render_template('admin_home.html')

@administration.route('/administration/user/block/<int:user_id>')
def block_member(user_id):
    '''Lets the admin block the user corresponding to the ID and updates the log '''
    my_user_id = escape(user_id)
    db.block_user(my_user_id)
    flash(("You have blocked this user successfully!", "success"))
    db.update_log_update(current_user._User__user_name, current_user._User__user_type, 'SALON_USER')
    return render_template('admin_home.html')

@administration.route('/administration/user/unblock/<int:user_id>')
def unblock_member(user_id):
    '''Lets the admin unblock the user corresponding to the ID and updates the log '''
    my_user_id = escape(user_id)
    db.unblock_user(my_user_id)
    flash(("You have unblocked this user successfully!", "success"))
    db.update_log_update(current_user._User__user_name, current_user._User__user_type, 'SALON_USER')
    return render_template('admin_home.html')
    
@administration.route('/administration/user/members/flag/<int:user_id>')
def flag_member(user_id):
    '''Lets the admin flag the user corresponding to the ID and updates the log '''
    my_user_id = escape(user_id)
    db.flag_user(my_user_id)
    db.update_log_update(current_user._User__user_name, current_user._User__user_type, 'SALON_USER')
    flash(("You have flagged this user successfully!", "success"))
    return render_template('admin_home.html')
    

@administration.route('/administration/user/members/warn/<int:user_id>', methods=['GET', 'POST'])
def warn_member(user_id):
    '''Lets the admin add a warning message to the user corresponding to the ID
      using the WarningForm and updates the log '''
    my_user_id = escape(user_id)
    warn_form = WarningForm()
    if request.method == 'POST':
        if warn_form.validate_on_submit():
            description = warn_form.message.data
            warned_user_id = my_user_id
            warning_issuer_id = current_user._User__user_id
            db.add_new_warning(warned_user_id, warning_issuer_id, description)
            db.update_log_update(current_user._User__user_name, current_user._User__user_type, 'SALON_USER')
            flash(("Warning Added successfully!", "success"))
            return redirect(url_for('administration.admin_home'))
        else:
            flash(("Something went wrong in the form, try again?", "error"))
            
    return render_template('warning.html', warn_form = warn_form, warned_user_id = my_user_id)

#--------------------

#All methods for Admin_appoint and Admin_super:

@administration.route('/administration/appointments')
def appointments():
    '''Gets all appointments from the database and diplays them using appointments.html '''
    appointmentsdb = db.get_appointments()
    return render_template('appointments.html', appointments = appointmentsdb)

@administration.route('/administration/appointments/select_service_and_user', methods=['GET', 'POST'])
def select_service_and_user():
    '''Allows the Admin to select a user and a service to make an appointment for '''
    services = db.get_services()
    users = db.get_customers()
    if request.method == 'POST':
        service_id = request.form.get('service')
        user_id = request.form.get('user')
        flash(("Selection Completed!", "success"))
        return redirect(url_for('administration.add_appointment', 
                                service_id = service_id, 
                                user_id = user_id))

    return render_template('select_service_and_user.html', services=services, users=users)


@administration.route('/administration/appointments/add/<int:service_id>/<int:user_id>', methods=['GET', 'POST'])
def add_appointment(service_id, user_id):
    '''Lets the admin make an appointment using the AddAppointmentForm and updates the log  '''
    appointment_form = AddAppointmentForm()
    if request.method == 'POST':
        if appointment_form.validate_on_submit():
            date_appoint = appointment_form.date_appoint.data
            slot = appointment_form.slot.data
            venue = appointment_form.venue.data
            my_client_name = db.get_user_id(user_id)[0].get('user_name')
            my_service_name = db.get_service(service_id).get('service_name')
            customer_id = user_id
            db.add_new_appointment(date_appoint, slot, venue, service_id, customer_id, my_service_name, my_client_name)
            db.update_log_add(current_user._User__user_name,
                            current_user._User__user_type,
                            'SALON_APPOINTMENT')
            flash(("Appointment created successfully!", "success"))
            return redirect(url_for('administration.admin_home'))
        else:
            print("Form validation errors:", appointment_form.errors)
            flash(("Adding appointment failed, try again.", "error"))
    return render_template('add_appointment.html', appointment_form = appointment_form, service_id = service_id, user_id = user_id)

@administration.route('/administration/appointments/delete/<int:appointment_id>')
def delete_appointment(appointment_id):
    '''Deletes the appointment corresponding to the ID and updates the log '''
    my_appointment_id = escape(appointment_id)
    db.delete_appointment(my_appointment_id)
    db.update_log_delete(current_user._User__user_name,
                        current_user._User__user_type,
                        'SALON_APPOINTMENT')
    flash(("You deleted an appointment sucessfully!", "success"))
    return redirect(url_for('administration.admin_home'))

@administration.route('/administration/appointments/change/<int:appointment_id>', methods=['GET', 'POST'])
def change_appointment(appointment_id):
    '''Modifies the appointment corresponding to the ID using AppointmentModificationForm
    and updates the log '''
    my_appointment_id = escape(appointment_id)
    my_appointment = db.get_appointment_id(my_appointment_id)[0]
    edited_appointment_form = AppointmentModificationForm()
    if request.method == 'POST':
        if edited_appointment_form.validate_on_submit():
            date_appoint = edited_appointment_form.date_appoint.data
            slot = edited_appointment_form.slot.data
            venue = edited_appointment_form.venue.data
            if slot == '':
                flash(("The slot field cannot be empty!", "error"))
            elif venue == '':
                flash(("The venye field cannot be empty!", "error"))
            else:
                db.update_appointment(my_appointment_id, date_appoint, slot, venue)
                db.update_log_update(current_user._User__user_name, current_user._User__user_type, 'SALON_APPOINTMENT')
                flash(("Appointment updated successfully!", "success"))
                return redirect(url_for('administration.admin_home'))
        else:
            print("Form validation errors:", edited_appointment_form.errors)
            flash(("Appointment updating failed, try again.", "error"))
            
    return render_template('appointment_update.html',
                           edited_appointment_form = edited_appointment_form,
                           old_appointment = my_appointment,
                           appointment_id = appointment_id)

@administration.route('/administration/reports')
def reports():
    '''Gets all reports from the database and dislays it using reports.html '''
    reportsdb = db.get_reports()
    return render_template('reports.html', reports = reportsdb)

@administration.route('/administration/reports/delete/<int:report_id>')
def delete_report(report_id):
    '''Deletes the report corresponding to the ID and updates the log '''
    my_report_id = escape(report_id)
    db.delete_report(my_report_id)
    db.update_log_delete(current_user._User__user_name, current_user._User__user_type, 'SALON_REPORT')
    flash(("You deleted a report sucessfully!", "success"))
    return redirect(url_for('administration.admin_home'))

@administration.route('/administration/reports/change/<int:report_id>', methods=['GET', 'POST'])
def change_report(report_id):
    '''Modifies the report corresponding to the ID using ReportModificationForm and updates the log '''
    my_report_id = escape(report_id)
    my_report = db.get_report_by_id(my_report_id)
    edited_report_form = ReportModificationForm()
    if request.method == 'POST':
        if edited_report_form.validate_on_submit():
            status = edited_report_form.status.data
            date_report = edited_report_form.date_report.data
            feedback_employee = edited_report_form.feedback_employee.data
            feedback_customer = edited_report_form.feedback_customer.data

            if status == '':
                flash(("The status field cannot be empty!", "error"))
            elif feedback_employee == '':
                flash(("The feedback employee field cannot be empty!", "error"))
            elif feedback_customer == '':
                flash(("The feedback customer field cannot be empty!", "error"))
            else:
                db.update_report(report_id, status, date_report, 
                                 feedback_employee, 
                                 feedback_customer)
                db.update_log_update(current_user._User__user_name, 
                                     current_user._User__user_type, 
                                     'SALON_REPORT')
                flash(("Report updated successfully!", "success"))
                return redirect(url_for('administration.admin_home'))
        else:
            print("Form validation errors:", edited_report_form.errors)
            flash(("Appointment updating failed, try again.", "error"))

    return render_template('report_update.html',
                           edited_report_form = edited_report_form,
                           old_report = my_report,
                           report_id = report_id)
    
@administration.route('/administration/reports/add/select_appointment/')
def select_appointment():
    '''Admin selection of appointments to add a report about'''
    appointmentsdb = db.get_appointments()
    return render_template('select_appointment.html', appointments = appointmentsdb)

@administration.route('/administration/reports/add/<int:appointment_id>', methods=['GET', 'POST'])
def add_report(appointment_id):
    '''Admin method to add a new report'''
    report_form = AddReportForm()
    if request.method == 'POST':
        if report_form.validate_on_submit():
            status = report_form.status.data
            date_report = report_form.date_report.data
            feedback_employee = report_form.feedback_employee.data
            feedback_customer = report_form.feedback_customer.data

            db.add_new_report_for_admin(appointment_id,
                                        status,
                                        date_report,
                                        feedback_employee,
                                        feedback_customer)

            db.update_log_add(current_user._User__user_name,
                              current_user._User__user_type,
                              'SALON_REPORT')

            flash(("Report created successfully!", "success"))
            return redirect(url_for('administration.admin_home'))
        else:
            print("Form validation errors:", report_form.errors)
            flash(("Adding report failed, try again.", "error"))
    return render_template('add_report.html', 
                           report_form = report_form, 
                           appointment_id = appointment_id)

@administration.route('/administration/logs')
def logs():
    '''Gets all the logs from the database and displays it using logs.html '''
    logsdb = db.get_logs()
    return render_template('logs.html', logs = logsdb)