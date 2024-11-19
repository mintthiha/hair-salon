''' This module is used to create the get, put and delete method requests for appointments '''
import ast
import datetime
from flask import request
from flask_restful import Resource, abort
import oracledb
from HairSalon.qdb.database_ import db

class Appointments(Resource):
    '''All appoinments class'''
    def get(self):
        ''' method to use to get all appointments '''  
        appointments = db.get_appointments()
        for appointment in appointments:
            appointment['date_appoint'] = appointment['date_appoint'].isoformat()
        return appointments, 200

class Appointment(Resource):
    ''' Single appointment class '''
    def get(self, appointment_id):
        ''' get method to get 1 appointment by id '''
        try:
            my_appointment = db.get_appointment_id(appointment_id)[0]
        except oracledb.Error:
            abort(404, message="This appointment does not exist in the db!")
        if not my_appointment:
            abort(404, message="Appointment not in the db!")
        my_appointment['date_appoint'] = my_appointment['date_appoint'].isoformat()
        return my_appointment, 200

    def put(self, appointment_id):
        ''' put method to update an appointment by id '''
        my_appointment = request.json
        int_tuple = ast.literal_eval(my_appointment.get('date_appoint'))
        mydate = datetime.date(*(int_tuple))
        if my_appointment:
            db.update_appointment(appointment_id,
                                  mydate,
                                  my_appointment.get('slot'),
                                  my_appointment.get('venue'))
            return "You updated an appointment Successfully!", 201
        abort(505)

    def delete(self, appointment_id):
        ''' delete method to delete an appointment by id'''
        try:
            db.delete_appointment(appointment_id)
            return "You deleted the appointment Successfully!", 200
        except oracledb.Error as e:
            return "Error in database: " + e, 500

class FilterAppointmentByStatus(Resource):
    ''' Class to filter an appointment by status '''
    def get(self, status):
        ''' get filtered appointments by status '''
        filtered_appointments = []
        my_appointments = db.get_appointments()
        for appointment in my_appointments:
            if appointment['status'] == status:
                appointment['date_appoint'] = appointment['date_appoint'].isoformat()
                filtered_appointments.append(appointment)
        if len(filtered_appointments) == 0:
            return "There are no appointments with that status!", 404

        return filtered_appointments, 200

class FilterAppointmentBySlot(Resource):
    ''' Class to filter an appointment by slot '''
    def get(self, slot):
        ''' get filtered appointments by slot '''
        filtered_appointments = []
        my_appointments = db.get_appointments()
        for appointment in my_appointments:
            if appointment['slot'] == slot:
                appointment['date_appoint'] = appointment['date_appoint'].isoformat()
                filtered_appointments.append(appointment)
        if len(filtered_appointments) == 0:
            return "There are no appointments with that slot!", 404
        return filtered_appointments, 200

class FilterAppointmentByVenue(Resource):
    ''' Class to filter an appointment by venue '''
    def get(self, venue):
        ''' get filtered appointments by venue '''
        filtered_appointments = []
        my_appointments = db.get_appointments()
        for appointment in my_appointments:
            if appointment['venue'] == venue:
                appointment['date_appoint'] = appointment['date_appoint'].isoformat()
                filtered_appointments.append(appointment)
        if len(filtered_appointments) == 0:
            return "There are no appointments with that venue!", 404
        return filtered_appointments, 200

class SearchAppointmentByCustomerName(Resource):
    ''' Class to search appointment by customer name '''
    def get(self, customer_name):
        '''search appointments by customer name'''
        filtered_appointments = []
        my_appointments = db.get_appointments()
        for appointment in my_appointments:
            if appointment['customer_name'] == customer_name:
                appointment['date_appoint'] = appointment['date_appoint'].isoformat()
                filtered_appointments.append(appointment)
        if len(filtered_appointments) == 0:
            return "There are no appointments with that customer name!", 404
        return filtered_appointments, 200

class SearchAppointmentByServiceName(Resource):
    ''' Class to search appointment by service name '''
    def get(self, service_name):
        '''search appointments by customer name'''
        filtered_appointments = []
        my_appointments = db.get_appointments()
        for appointment in my_appointments:
            if appointment['service_name'] == service_name:
                appointment['date_appoint'] = appointment['date_appoint'].isoformat()
                filtered_appointments.append(appointment)
        if len(filtered_appointments) == 0:
            return "There are no appointments with that service name!", 404
        return filtered_appointments, 200

class SearchAppointmentByServiceID(Resource):
    ''' Class to search appointment by service id '''
    def get(self, service_id):
        '''search appointments by service id '''
        filtered_appointments = []
        my_appointments = db.get_appointments()
        for appointment in my_appointments:
            if appointment['service_id'] == service_id:
                appointment['date_appoint'] = appointment['date_appoint'].isoformat()
                filtered_appointments.append(appointment)
        if len(filtered_appointments) == 0:
            return "There are no appointments with that service id!", 404
        return filtered_appointments, 200

class SearchAppointmentByCustomerID(Resource):
    ''' Class to search appointment by customer id '''
    def get(self, customer_id):
        '''search appointments by customer id '''
        filtered_appointments = []
        my_appointments = db.get_appointments()
        for appointment in my_appointments:
            if appointment['customer_id'] == customer_id:
                appointment['date_appoint'] = appointment['date_appoint'].isoformat()
                filtered_appointments.append(appointment)
        if len(filtered_appointments) == 0:
            return "There are no appointments with that customer id!", 404
        return filtered_appointments, 200
