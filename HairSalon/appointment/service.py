class Service:
    '''Service object with all of the fields '''
    def __init__ (self, employee_id, service_name, duration, price, materials):
        
        self.employee_id = employee_id
        self.service_name = service_name
        self.duration = duration
        self.price = price
        self.materials = materials

    def __str__ (self):
        return f'{self.service_name}, {self.duration}, {self.price}, {self.materials}'