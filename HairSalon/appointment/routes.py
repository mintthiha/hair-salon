from flask_login import current_user, login_required
from markupsafe import escape
from flask import Blueprint, flash, redirect, render_template, request, url_for
from HairSalon.qdb.database_ import db
from HairSalon.appointment.forms import NewAppointmentForm, NewServiceForm
from HairSalon.administration.forms import AppointmentModificationForm


appointment = Blueprint('appointment', __name__,
                         template_folder='templates', static_folder='static') 

@appointment.route('/appointments/<int:appointment_id>')
def get_appointment_by_id(appointment_id):
    '''Gets a specific appointment by ID and displays all the details if you are logged in'''
    if current_user.is_authenticated:
        appointment_id = escape(appointment_id)
        myappointment = db.get_appointment_id(appointment_id)[0]
        service = db.get_service(myappointment['service_id'])
        employee = db.get_user_id(service['employee_id'])[0]
        return render_template("appointment.html", appointment = myappointment, employee = employee)
    else:
        flash(("You must be logged in to see details", "error"))
        return redirect(url_for("userAuthentication.register"))

@appointment.route('/book/appointment/<int:service_id>/<service_name>', methods=['GET', 'POST'])
def create_appointment(service_id, service_name):
    '''Creates an appointment using the NewAppointmentForm and updates the log '''
    appointment_form = NewAppointmentForm()
    if request.method == 'POST':
        if appointment_form.validate_on_submit():
            date_appoint = appointment_form.date_appoint.data
            slot = appointment_form.slot.data
            venue = appointment_form.venue.data
            customer_id = current_user._User__user_id
            customer_name = current_user._User__user_name
            db.add_new_appointment(date_appoint, slot, venue, service_id, customer_id, service_name, customer_name)
            db.update_log_add(current_user._User__user_name, current_user._User__user_type, 'SALON_APPOINTMENT') 
            flash(("Appointment created successfully!", "success"))
            
        else:
            print("Form validation errors:", appointment_form.errors)
            flash(("Appointment booking failed, try again.", "error"))
    return render_template('book_appointment.html', appointment_form = appointment_form, service_id = service_id, service_name = service_name)

@appointment.route('/modify/appointment/<int:appointment_id>', methods=['GET', 'POST'])
def modify_appointment(appointment_id):
    '''Modifies the appointment corresponding to the ID using the AppointmentModificationForm '''
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
                flash(("The venue field cannot be empty!", "error"))
            else:
                db.update_appointment(my_appointment_id, date_appoint, slot, venue)
                db.update_log_update(current_user._User__user_name, current_user._User__user_type, 'SALON_APPOINTMENT')
                flash(("Appointment updated successfully!", "success"))
                return redirect(url_for('main.home'))
        else:
            print("Form validation errors:", edited_appointment_form.errors)
            flash(("Appointment updating failed, try again.", "error"))
            
    return render_template('modify_appointment.html',
                           edited_appointment_form = edited_appointment_form,
                           old_appointment = my_appointment,
                           appointment_id = appointment_id)

@appointment.route('/remove/appointment/<int:appointment_id>')
def remove_appointment(appointment_id):
    '''Deletes the appointment corresponding to the ID from the database and updates log '''
    my_appointment_id = escape(appointment_id)
    db.delete_appointment(my_appointment_id)
    db.update_log_delete(current_user._User__user_name, current_user._User__user_type, 'SALON_APPOINTMENT')
    flash(("You deleted an appointment sucessfully!", "success"))
    return redirect(url_for('main.home'))

@appointment.route('/services/<int:service_id>')
def get_service_by_id(service_id):
    '''Gets a specific service corresponding to the ID '''
    services = db.get_services()
    for service in services:
        if service['service_id'] == service_id:
            return escape(str(service))  
    return redirect(url_for('all_services'))  

@appointment.route('/services')
def all_services():
    '''Gets all services for the database and displays them in service.html '''
    servicesdb = db.get_services()
    services = []
    for s in servicesdb:
        if s.get('employee_id') is not current_user._User__user_id:
            services.append(s)
    return render_template('service.html', services = services)

@appointment.route('/services/create', methods=['GET', 'POST'])
@login_required
def create_service():
    '''Creates a service using the NewServiceForm if the user is a professional '''
    if current_user._User__user_type != "professional":
        flash(("Only employees can create services!", "error"))
        return redirect(url_for('appointment.all_services')) 
    form = NewServiceForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            service_name = form.service_name.data
            duration = form.duration.data
            price = form.price.data
            materials = form.materials.data
            employee_id = current_user._User__user_id
            db.add_service(employee_id, service_name, duration, price, materials)
            flash(("Service created successfully!", "success"))
            return redirect(url_for('appointment.all_services'))
    return render_template('service_form.html', form = form)

@appointment.route('/service/employee/<int:employee_id>')
def get_employee(employee_id):
    '''Gets the employee corresponding to the ID and displays it using service_provider.html '''
    employee = db.get_user_id(employee_id)
    return render_template('service_provider.html', employee = employee[0])
