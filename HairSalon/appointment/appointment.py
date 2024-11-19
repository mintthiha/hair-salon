class Appointment:
    '''Appointment object with all of the fields  '''
    def __init__ (self, status, approved, date_appoint, slot, venue, 
                  service_id, customer_id, service_name, customer_name):
        
        self.status = status
        self.approved = approved
        self.date_appoint = date_appoint
        self.slot = slot
        self.venue = venue
        self.service_id = service_id
        self.customer_id = customer_id
        self.service_name = service_name
        self.customer_name = customer_name

    def __str__ (self):
        return f'{self.status}, {self.approved}, {self.date_appoint}, {self.slot}, {self.venue}'
