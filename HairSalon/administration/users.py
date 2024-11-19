from flask_login import UserMixin
from HairSalon.qdb.database_ import db
class User (UserMixin):
    '''User object with all of the fields '''
    def __init__ (self, user_name):
        #user_name = 1
        user = db.get_user(user_name)
        if not user:
            user = db.get_user_id(user_name)[0]
        else:
            user = user[0]
        self.__user_id = user['user_id']
        self.__is_active = user['is_active']
        self.__user_type = user['user_type']
        self.__access_level = user['access_level']
        self.__user_name = user['user_name']
        self.__email = user['email']
        self.__user_image = user['user_image']
        self.__password = user['password']
        self.__phone_number = user['phone_number']
        self.__address = user['address']
        self.__age = user['age']
        self.__pay_rate = user['pay_rate']
        self.__speciality = user['speciality']
        self.__times_flagged = user['times_flagged']


    def __str__ (self):
        return f'{self.__user_name}, {self.__email}, {self.__phone_number}, {self.__age}'
    
    def is_authenticated(self):
        '''Called to determine if user has been authenticated '''
        return True
    
    def is_active(self):
        '''Called to determine if user is active '''
        if (self.__is_active == 1):
            return True
        else :
            return False
    
    def is_anonymous(self):
        '''Called to determine if user is anonymous '''
        return False
          
    def get_id(self):
        return str(self.__user_id)
    # def get_username(self):
    #     return self.__user_name
