class Report:
    '''Report object with all of the fields '''
    def __init__ (self, appointment_id, status, date_report, feedback_employee, feedback_customer):
        
        self.appointment_id = appointment_id
        self.status = status
        self.date_report = date_report
        self.feedback_employee = feedback_employee
        self.feedback_customer = feedback_customer

    def __str__ (self):
        return f'{self.status}, {self.date_report}, {self.feedback_employee}, {self.feedback_customer}'