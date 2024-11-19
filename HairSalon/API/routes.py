''' This module is used to create the URLs for the API, 
and also some methods for the buttons in the API page'''
from flask import Blueprint, render_template
from flask_restful import Api
from HairSalon.appointment.appointment_ressource import Appointment, Appointments, FilterAppointmentByStatus, FilterAppointmentBySlot, FilterAppointmentByVenue, SearchAppointmentByServiceName, SearchAppointmentByServiceID, SearchAppointmentByCustomerID, SearchAppointmentByCustomerName

# Suggestion 1: Use a more descriptive name for the Blueprint
api_blueprint = Blueprint('api', __name__, template_folder='templates')
api = Api(api_blueprint)

# Suggestion 2: Use trailing slashes in API endpoints for consistency
api.add_resource(Appointments, '/api/appointments/')
api.add_resource(Appointment, '/api/appointments/<string:appointment_id>')
api.add_resource(FilterAppointmentByStatus, '/api/appointments/filter-by-status/<string:status>')
api.add_resource(FilterAppointmentBySlot, '/api/appointments/filter-by-slot/<string:slot>')
api.add_resource(FilterAppointmentByVenue, '/api/appointments/filter-by-venue/<string:venue>')
api.add_resource(SearchAppointmentByServiceName, '/api/appointments/search-by-service-name/<string:service_name>')
api.add_resource(SearchAppointmentByServiceID, '/api/appointments/search-by-service-id/<int:service_id>')
api.add_resource(SearchAppointmentByCustomerName, '/api/appointments/search-by-client-name/<string:customer_name>')
api.add_resource(SearchAppointmentByCustomerID, '/api/appointments/search-by-client-id/<int:customer_id>')

# Suggestion 3: Consider adding a root endpoint for API documentation or a welcome message
@api_blueprint.route('/api')
def api_root():
    ''' The root of the API '''
    return render_template('api.html')

@api_blueprint.route('/api/appointments-button')
def get_appointments_button():
    ''' returns the url and the response for getting all appointments '''
    return render_template('api.html', url = "/api/appointments/", response = 200,
                           category = "success")

@api_blueprint.route('/api/specific-appointment-button')
def get_appointment_button():
    ''' returns the url and the response for getting a single appointment '''
    return render_template('api.html', url = "/api/appointments/2", response = 200,
                           category = "success")

@api_blueprint.route('/api/specific-appointment-button-not-found')
def get_appointment_button_not_found():
    ''' returns the url and the response for failing to get an appointment '''
    return render_template('api.html', url = "/api/appointments/999", response = 404,
                           category = "error")

@api_blueprint.route('/api/appointments-filter-status-button')
def get_appointments_filter_status_button():
    ''' returns the url and the response for filtering an appointment by status'''
    return render_template('api.html', url = "/api/appointments/filter-by-status/requested",
                           response = 200,
                           category = "success")

@api_blueprint.route('/api/appointments-filter-slot-button')
def get_appointments_filter_slot_button():
    ''' returns the url and the response for filtering an appointment by the slot'''
    return render_template('api.html', url = "/api/appointments/filter-by-slot/3-4", response = 200,
                           category = "success")

@api_blueprint.route('/api/appointments-filter-venue-button')
def get_appointments_filter_venue_button():
    ''' returns the url and the response for filtering an appointment by the venue'''
    return render_template('api.html', url = "/api/appointments/filter-by-venue/room1",
                           response = 200,
                           category = "success")

@api_blueprint.route('/api/appointments/search-service-name-button')
def get_appointments_search_service_name_button():
    ''' returns the url and the response for searching an appointment by service name'''
    return render_template('api.html', url = "/api/appointments/search-by-service-name/braids",
                           response = 200,
                           category = "success")

@api_blueprint.route('/api/appointments/search-by-service-id-button')
def get_appointments_search_service_id_button():
    ''' returns the url and the response for searching an appointment by service id'''
    return render_template('api.html', url = "/api/appointments/search-by-service-id/1",
                           response = 200,
                           category = "success")

@api_blueprint.route('/api/appointments/search-client-name-button')
def get_appointments_search_client_name_button():
    ''' returns the url and the response for searching an appointment by client name'''
    return render_template('api.html', url = "/api/appointments/search-by-client-name/client1",
                           response = 200,
                           category = "success")

@api_blueprint.route('/api/appointments/search-client-id-button')
def get_appointments_search_client_id_button():
    ''' returns the url and the response for searching an appointment by client id'''
    return render_template('api.html', url = "/api/appointments/search-by-client-id/3",
                           response = 200,
                           category = "success")

@api_blueprint.route('/api/appointments/delete-appointment')
def get_appointments_deleted_appointment_button():
    ''' returns the url and the response for deleting an appointment by it's id'''
    return render_template('api.html', url = "/api/appointments/2", response = 204, category = "error")

@api_blueprint.route('/api/appointments/update-appointment')
def get_appointments_updated_appointment_button():
    ''' returns the url, the request body the response for updating an appoinment, specifically
    the date, the slot and the venue!'''
    request_body = """{
    "date_appoint": "(12,12,12)", "slot": "20-21", "venue": "Room 4"
    }"""
    return render_template('api.html', url = "/api/appointments/2",
                           request_body = request_body,
                           response = 200,
                           category = "success")
