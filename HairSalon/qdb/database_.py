''' Database file'''
import os
import oracledb
from HairSalon.qdb import config_db

class Database:
    '''Database class, contains instance of db and methods relating to db connection management and db querying'''
    def __init__(self, autocommit=True):
        self.__connection = self.__connect()
        self.__connection.autocommit = autocommit

    def __connect(self):
        return oracledb.connect(user=config_db.usr, password=config_db.pw, host=config_db.host,  service_name=config_db.sn)
    def  db_conn (self):
        '''returns the db connection'''
        return self.__connection

    def __run_file(self, file_path):
        '''runs the sql schema file'''
        statement_parts = []
        with self.__connection.cursor() as cursor:
            with open(file_path, 'r') as f:
                for line in f:
                    if line[:2]=='--':
                        continue
                    statement_parts.append(line)
                    if line.strip('\n').strip('\n\r').strip().endswith(';'):
                        statement = "".join( statement_parts).strip().rstrip(';')
                        if statement:
                            try:
                                cursor.execute(statement)
                            except Exception as e:
                                print(e)
                        statement_parts = []

    def close(self):
        '''Closes the connection'''
        if self.__connection is not None:
            self.__connection.close()
            self.__connection = None

    def get_cursor(self):
        '''Returns a cursor instance'''
        for i in range(3):
            try:
                return self.__connection.cursor()
            except Exception as e:
                self.__reconnect()
                print(e)

    def __reconnect(self):
        '''Tries to reconnect to db by closing the connection and connecting again'''
        try:
            self.close()
        except oracledb.Error as f:
            print(f)
        self.__connection = self.__connect()

    def run_sql_script(self, sql_filename):
        '''connects to the db to run a database sql script file'''
        if os.path.exists(sql_filename):
            self.__connect()
            self.__run_file(sql_filename)
            self.close()
        else:
            print('Invalid Path')

#---------------------------------------------------------------------

    def get_users(self):
        '''queries the db to retrieve all user entries in Salon_User'''
        with self.__connection.cursor() as cur:
            qry = "Select * From Salon_User"
            try:
                r = cur.execute(qry)
                columns = [col[0].lower() for col in cur.description]
                cur.rowfactory = lambda *args: dict(zip(columns, args))
                return r.fetchall()
            except Exception as e:
                print(e)

    def get_user(self, username):
        '''queries the db to retrieve the specific Salon_User entry matching the username'''
        with self.__connection.cursor() as cur:
            qry = "Select * From Salon_User Where user_name=:username"
            try:
                r = cur.execute(qry, [username])
                columns = [col[0].lower() for col in cur.description]
                cur.rowfactory = lambda *args: dict(zip(columns, args))
                return r.fetchall()
            except Exception as e:
                print(e)

    def get_user_id(self, user_id):
        '''queries the db to retrieve the specific Salon_User entry matching the user_id'''
        with self.__connection.cursor() as cur:
            qry = "Select * From Salon_User Where user_id=:user_id"
            try:
                r = cur.execute(qry, [user_id])
                columns = [col[0].lower() for col in cur.description]
                cur.rowfactory = lambda *args: dict(zip(columns, args))
                return r.fetchall()
            except Exception as e:
                print(e)

    def add_new_member(self, user_type, username, email, password, user_image, phone_number, address, age, speciality):
        '''adds a new member inside Salon_User through an Insert statement'''
        try:
            with self.__connection.cursor() as cursor:
                qry = """INSERT INTO Salon_User (user_type, access_level, user_name, email, user_image, password, phone_number, address, age, speciality)
                VALUES (:user_type, :access_level, :username, :email, :user_image, :password, :phone_number, :address, :age, :speciality)"""
                access_lvl = 1
                if(user_type == 'appoint' or user_type == 'user'):
                    access_lvl = 2
                cursor.execute(qry,
                               user_type = user_type,
                               access_level = access_lvl,
                               username = username,
                               email = email,
                               user_image = user_image,
                               password = password,
                               phone_number = phone_number,
                               address = address,
                               age = age,
                               speciality = speciality)
                return True
        except oracledb.Error as e:
            print("Error adding a new Member: ", e)
            return False

    def get_customers(self):
        '''queries the db to retrieve all user entries in Salon_User that are customers'''
        with self.__connection.cursor() as cur:
            qry = "Select * From Salon_User where access_level = 1 AND (user_type = 'client' OR user_type = 'professional')"
            try:
                r = cur.execute(qry)
                columns = [col[0].lower() for col in cur.description]
                cur.rowfactory = lambda *args: dict(zip(columns, args))
                return r.fetchall()
            except Exception as e:
                print(e)

    def get_employees(self):
        '''queries the db to retrieve all user entries in Salon_User that are employees'''
        with self.__connection.cursor() as cur:
            qry = f"Select * From Salon_User where user_type=employee"
            try:
                r = cur.execute(qry)
                columns = [col[0].lower() for col in cur.description]
                cur.rowfactory = lambda *args: dict(zip(columns, args))
                return r.fetchall()
            except Exception as e:
                print(e)

    def get_active_employees(self):
        '''queries the db to retrieve all user entries in Salon_User that are employees and are active'''
        with self.__connection.cursor() as cur:
            qry = f"Select * From Salon_User where is_active=1"
            try:
                r = cur.execute(qry)
                columns = [col[0].lower() for col in cur.description]
                cur.rowfactory = lambda *args: dict(zip(columns, args))
                return r.fetchall()
            except Exception as e:
                print(e)

    def get_appointments(self):
        '''queries the db to retrieve all appointment entries in Salon_Appointment'''
        with self.__connection.cursor() as cur:
            qry = f"Select * From Salon_Appointment"
            try:
                r = cur.execute(qry)
                columns = [col[0].lower() for col in cur.description]
                cur.rowfactory = lambda *args: dict(zip(columns, args))
                return r.fetchall()
            except Exception as e:
                print(e)

    def get_appointment_id(self, appointment_id):
        '''queries the db to retrieve the appointment entry in Salon_Appointment matching the appointment_id'''
        with self.__connection.cursor() as cur:
            qry = "Select * From Salon_Appointment Where appointment_id=:appointment_id"
            try:
                r = cur.execute(qry, [appointment_id])
                columns = [col[0].lower() for col in cur.description]
                cur.rowfactory = lambda *args: dict(zip(columns, args))
                return r.fetchall()
            except Exception as e:
                print(e)

    def get_reports(self):
        '''queries the db to retrieve all report entries in Salon_Report'''
        with self.__connection.cursor() as cur:
            qry = f"Select * From Salon_Report"
            try:
                r = cur.execute(qry)
                columns = [col[0].lower() for col in cur.description]
                cur.rowfactory = lambda *args: dict(zip(columns, args))
                return r.fetchall()
            except Exception as e:
                print(e)

    def get_report_by_appointment_id(self, appointment_id):
        '''queries the db to retrieve the Salon_Report entry that matches the appointment_id'''
        with self.__connection.cursor() as cur:
            qry = "Select * From Salon_Report Where appointment_id = :appointment_id"
            try:
                r = cur.execute(qry, [appointment_id])
                columns = [col[0].lower() for col in cur.description]
                cur.rowfactory = lambda *args: dict(zip(columns, args))
                service = cur.fetchone()
                return service
            except Exception as e:
                print(e)
    

    def get_services(self):
        '''queries the db to retrieve all service entries in Salon_Service'''
        with self.__connection.cursor() as cur:
            qry = f"Select * From Salon_Service"
            try:
                r = cur.execute(qry)
                columns = [col[0].lower() for col in cur.description]
                cur.rowfactory = lambda *args: dict(zip(columns, args))
                return r.fetchall()
            except Exception as e:
                print(e)

    def add_service(self, employee_id, service_name, duration, price, materials):
        '''Adds a new service entry inside Salon_Service through an Insert statement'''
        try:
            with self.__connection.cursor() as cursor:
                qry = """INSERT INTO Salon_Service (employee_id, service_name, duration, price, materials)
                VALUES (:employee_id, :service_name, :duration, :price, :materials)"""
                
                cursor.execute(qry, (employee_id, service_name, duration, price, materials))
        except oracledb.Error as e:
            print("Error adding a new Service: ", e)

    def delete_user(self, user_id):
        '''Deletes the user entry in Salon_User that matches the user_id'''
        try:
            cursor = self.get_cursor()
            cursor.execute(f"Delete From Salon_User Where user_id = {user_id}")
            self.__connection.commit() 
            cursor.close()  
        except oracledb.Error as e:
            print(f"Error removing user: {e}")

    def update_password_user(self, user_id, password):
        '''Upates the password record of the entry in Salon_User that matches the user_id'''
        try:
            cur= self.get_cursor()
            cur.execute(f"Update Salon_User Set password='{password}' Where user_id={user_id}")
            self.__connection.commit()
            cur.close()
        except Exception as e:
            print(f"Error updating password: {e}")

    def add_new_appointment(self, date_appoint, slot, venue, service_id, customer_id, service_name, customer_name):
        '''Adds a new appointment entry in Salon_Appointment through an Insert statement'''
        try:
            with self.__connection.cursor() as cursor:
                qry = """INSERT INTO Salon_Appointment (status, date_appoint, slot, venue, service_id, customer_id, service_name, customer_name)
                VALUES (:status, :date_appoint, :slot, :venue, :service_id, :customer_id, :service_name, :customer_name)"""
                cursor.execute(qry,
                               status = 'requested',
                               date_appoint = date_appoint,
                               slot = slot,
                               venue = venue,
                               service_id = service_id,
                               customer_id = customer_id,
                               service_name = service_name,
                               customer_name = customer_name)
        except oracledb.Error as e:
            print("Error adding a new Appointment: ", e)

    def add_new_report_for_customer(self, appointment_id, feedback_customer):
        '''Adds a new report entry by a customer inside Salon_Report for a specific appointment_id'''
        try:
            with self.__connection.cursor() as cursor:
                qry = """INSERT INTO Salon_Report (appointment_id, status , feedback_customer)
                VALUES (:appointment_id, :status, :feedback_customer)"""
                
                cursor.execute(qry,
                               appointment_id = appointment_id,
                               status = 'pending',
                               feedback_customer = feedback_customer)
        except oracledb.Error as e:
            print("Error adding a new Report: ", e)
            
    def reply_report_for_employee(self, appointment_id, feedback_employee):
        '''Updates the Salon_Report entry matching the appointment_id with the feedback_employee'''
        try:
            with self.__connection.cursor() as cursor:
                qry = """ UPDATE Salon_Report SET feedback_employee = :feedback_employee, status = :status
                WHERE appointment_id = :appointment_id"""
                cursor.execute(qry,
                               appointment_id = appointment_id,
                               status = 'done',
                               feedback_employee = feedback_employee)
        except oracledb.Error as e:
            print("Error replying to the report: ", e)

    def get_service(self, service_id):
        '''queries the db to retrieve the Salon_Service entry that matches the service_id'''
        with self.__connection.cursor() as cur:
            qry = "Select * From Salon_Service Where service_id = :service_id"
            try:
                r = cur.execute(qry, [service_id])
                columns = [col[0].lower() for col in cur.description]
                cur.rowfactory = lambda *args: dict(zip(columns, args))
                service = cur.fetchone()  
                return service
            except Exception as e:
                print(e)
    
    def add_new_warning(self, warned_user_id, warning_issuer_id, description):
        '''Adds a new entry in Salon_Warning through an Insert statement'''
        try:
            with self.__connection.cursor() as cursor:
                qry = """INSERT INTO Salon_Warning (description, warned_user_id, warning_issuer_id)
                VALUES (:description, :warned_user_id, :warning_issuer_id)"""

                cursor.execute(qry,
                               description = description,
                               warned_user_id = warned_user_id,
                               warning_issuer_id = warning_issuer_id)
        except oracledb.Error as e:
            print("Error adding a new warning: ", e)

    def get_warning(self, warned_user_id):
        '''queries the db to retrieve the Salon_Warning entry that matches the warned_user_id'''
        with self.__connection.cursor() as cur:
            qry = "Select * From Salon_Warning Where warned_user_id = :warned_user_id"
            try:
                r = cur.execute(qry, [warned_user_id])
                columns = [col[0].lower() for col in cur.description]
                cur.rowfactory = lambda *args: dict(zip(columns, args))
                service = cur.fetchone()  
                return service
            except Exception as e:
                print(e)


    # def get_warnings_by_user_id(self, warned_user_id, )

    def block_user(self, blocked_user_id):
        '''Updates the entry in Salon_User that matches the blocker_user_id and changes the is_active field'''
        try:
            with self.__connection.cursor() as cursor:
                qry = """UPDATE Salon_User
                SET is_active = 0
                WHERE user_id = :blocked_user_id"""
                cursor.execute(qry,
                               blocked_user_id = blocked_user_id)
        except oracledb.Error as e:
            print("Error blocking a user: ", e)

    def unblock_user(self, blocked_user_id):
        '''Updates the entry in Salon_User that matches the blocker_user_id and changes the is_active field'''
        try:
            with self.__connection.cursor() as cursor:
                qry = """UPDATE Salon_User
                SET is_active = 1
                WHERE user_id = :blocked_user_id"""
                cursor.execute(qry,
                               blocked_user_id = blocked_user_id)
        except oracledb.Error as e:
            print("Error unblocking a user: ", e)

    def flag_user(self, flagged_user_id):
        '''retrieves amount of times the Salon_User entry matching flagged_user_id has been flagged and adds 1'''
        try:
            with self.__connection.cursor() as cursor:
                qry = """Select times_flagged
                FROM Salon_User
                WHERE user_id = :flagged_user_id"""
                r = cursor.execute(qry, [flagged_user_id])
                columns = [col[0].lower() for col in cursor.description]
                cursor.rowfactory = lambda *args: dict(zip(columns, args))
                user_flagged_amount = r.fetchall()[0].get('times_flagged')
                new_amount = user_flagged_amount + 1

                upt_qry = """UPDATE Salon_User
                SET times_flagged = :new_amount
                WHERE user_id = :flagged_user_id"""

                cursor.execute(upt_qry,
                               new_amount = new_amount,
                               flagged_user_id = flagged_user_id)
        except oracledb.Error as e:
            print("Error flagging a user: ", e)
    
    def delete_appointment(self, appointment_id):
        '''Deletes the records in Salon_Report and Salon_Appointment that matches the appointment_id'''
        try:
            cursor = self.get_cursor()
            cursor.execute(f"Delete from Salon_Report WHERE appointment_id = {appointment_id}")
            cursor.execute(f"Delete From Salon_Appointment Where appointment_id = {appointment_id}")
            self.__connection.commit() 
            cursor.close()  
        except oracledb.Error as e:
            print(f"Error removing appointment: {e}")

    def update_appointment(self, appointment_id, new_date_appoint, new_slot, new_venue):
        '''Updates the Salon_Appointment field that matches the appointment_id'''
        try:
            with self.__connection.cursor() as cursor:
                qry = """UPDATE Salon_Appointment
                SET date_appoint = :new_date_appoint,
                slot = :new_slot,
                venue = :new_venue
                WHERE appointment_id = :appointment_id"""
                cursor.execute(qry,
                                new_date_appoint = new_date_appoint,
                                new_slot = new_slot,
                                new_venue = new_venue,
                                appointment_id = appointment_id)

        except oracledb.Error as e:
            print(f"Error updating appointment: {e}")

    def delete_report(self, report_id):
        '''Deletes the Salon_Report entry that matches the report_id'''
        try:
            cursor = self.get_cursor()
            cursor.execute(f"Delete from Salon_Report WHERE report_id = {report_id}")
            self.__connection.commit()
            cursor.close()
        except oracledb.Error as e:
            print(f"Error removing report: {e}")

    def get_report_by_id(self, report_id):
        '''queries the db to retrieve the Salon_Report entry that matches the report_id'''
        with self.__connection.cursor() as cur:
            qry = "Select * From Salon_Report Where report_id = :report_id"
            try:
                r = cur.execute(qry, [report_id])
                columns = [col[0].lower() for col in cur.description]
                cur.rowfactory = lambda *args: dict(zip(columns, args))
                service = cur.fetchone()
                return service
            except Exception as e:
                print(e)

    def update_report(self, report_id, status, date_report, feedback_employee, feedback_customer):
        '''Updates the Salon_Report entry that matches the report_id'''
        try:
            with self.__connection.cursor() as cursor:
                qry = """UPDATE Salon_Report
                SET status = :status,
                date_report = :date_report,
                feedback_employee = :feedback_employee,
                feedback_customer = :feedback_customer
                WHERE report_id = :report_id"""
                cursor.execute(qry,
                                status = status,
                                date_report = date_report,
                                feedback_employee = feedback_employee,
                                feedback_customer = feedback_customer,
                                report_id = report_id)
        except oracledb.Error as e:
            print(f"Error updating report: {e}")

    def add_new_report_for_admin(self, appointment_id, status, date_report, feedback_employee, feedback_customer):
        '''Adds a new record in Salon_Report when an admin accounts wants to add one, sets both customer and employee feedback'''
        try:
            with self.__connection.cursor() as cursor:
                qry = """INSERT INTO Salon_Report (appointment_id, status, date_report, feedback_employee, feedback_customer)
                VALUES (:appointment_id, :status, :date_report, :feedback_employee, :feedback_customer)"""
                cursor.execute(qry,
                               appointment_id = appointment_id,
                               status = status,
                               date_report = date_report,
                               feedback_employee = feedback_employee,
                               feedback_customer = feedback_customer)
        except oracledb.Error as e:
            print("Error adding a new Report: ", e)

    def update_log_add(self, user_name, user_type, table_name):
        '''Adds a Salon_Log entry when a Insert action happens on the db'''
        try:
            with self.__connection.cursor() as cursor:
                qry = """INSERT INTO Salon_Log (user_name, user_type, action_type, table_name)
                VALUES (:user_name, :user_type, :action_type, :table_name)"""
                cursor.execute(qry,
                               user_name = user_name,
                               user_type = user_type,
                               action_type = 'INSERT',
                               table_name = table_name)
        except oracledb.Error as e:
            print("Error adding a new Log (INSERT) : ", e)

    def update_log_delete(self, user_name, user_type, table_name):
        '''Adds a Salon_Log entry when a Delete action happens on the db'''
        try:
            with self.__connection.cursor() as cursor:
                qry = """INSERT INTO Salon_Log (user_name, user_type, action_type, table_name)
                VALUES (:user_name, :user_type, :action_type, :table_name)"""
                cursor.execute(qry,
                               user_name = user_name,
                               user_type = user_type,
                               action_type = 'DELETE',
                               table_name = table_name)
        except oracledb.Error as e:
            print("Error adding a new Log (DELETE) : ", e)

    def update_log_update(self, user_name, user_type, table_name):
        '''Adds a Salon_Log entry when a Update action happens on the db'''
        try:
            with self.__connection.cursor() as cursor:
                qry = """INSERT INTO Salon_Log (user_name, user_type, action_type, table_name)
                VALUES (:user_name, :user_type, :action_type, :table_name)"""
                cursor.execute(qry,
                               user_name = user_name,
                               user_type = user_type,
                               action_type = 'UPDATE',
                               table_name = table_name)
        except oracledb.Error as e:
            print("Error adding a new Log (UPDATE) : ", e)

    def get_logs(self):
        '''queries the db to retrieve all Salon_Log entries'''
        with self.__connection.cursor() as cur:
            qry = "Select * From Salon_Log"
            try:
                r = cur.execute(qry)
                columns = [col[0].lower() for col in cur.description]
                cur.rowfactory = lambda *args: dict(zip(columns, args))
                return r.fetchall()
            except Exception as e:
                print(e)
'''Database instance'''
db = Database()

if __name__ == '__main__':
    db.run_sql_script('schema.sql')
