drop table Salon_Report cascade constraints;
drop table Salon_Appointment cascade constraints;
drop table Salon_Service cascade constraints;
drop table Salon_Warning cascade constraints;
drop table Salon_Log cascade constraints;
drop table Salon_User cascade constraints;

create table Salon_User (
    user_id number(4) generated always as identity constraint salon_user_pk primary key,
    is_active number(1) default (1),
    user_type varchar2(15),
    access_level number(1),
    user_name varchar2(30) not null unique,
    email varchar2(120) not null unique,
    user_image varchar2(100),
    password varchar2(80) not null,
    phone_number varchar2(15),
    address varchar2(30),
    age number(4),
    pay_rate number(5, 2),
    speciality varchar2(30),
    times_flagged number(2) default (0)
);

--------------  super -----------------
INSERT INTO SALON_USER ( user_type ,access_level , user_name   ,email , user_image,  password, phone_number, address, age, pay_rate, speciality )
      VALUES ('super',3,'nasr','nasrs@email.com', 'userPlaceholder.png', '$2y$07$5s1QoaGOaayTyJg5DiB/jugUx96uDZcw6v0LndbVGX1s8IUqleOKu', '514-1234567', 'addr1', 50, 25, 'admin appoint stuff' ); 
--------------  admins -----------------
INSERT INTO Salon_User (user_type , access_level,  user_name, email , user_image, password, phone_number, address, age, pay_rate, speciality)
      VALUES ('user', 2, 'user_manager1','usermanager1@email.com', 'userPlaceholder.png','$2a$12$hE0/RCjyP7rOfrQGOQd7Z.ne89M0hT3MrUUd.my8wSyZe2YtH1qfK', '123-456-7890', '0 street', 43, 25.6, 'super admin stuff'); 
      
INSERT INTO SALON_USER ( user_type ,access_level , user_name   ,email , user_image,  password, phone_number, address, age, pay_rate, speciality )
      VALUES ('appoint',2,'appoint_manager1','appointmanager@email.com', 'userPlaceholder.png',  '$2y$10$rs.PcMNstCgzNO/ii0cJv.6ep0ospfNi.rrAufGxBk1uNjKkYQ6em', '514-1234567', 'addr3', 18, 25, 'admin appoint stuff' ); 

-- INSERT INTO SALON_USER ( user_type ,access_level , user_name   ,email , user_image,  password, phone_number, address, age, pay_rate, speciality )
--       VALUES ('appoint',2,'badr','badr@email.com', 'images/userPlaceholder.png',  '$2b$12$gqsQ8F1vZRxuRj.k2PM57eL/NA.Y/b6FxJ0SfihztJdlcPw7q2E9G', '514-1234567', 'addr2', 18, 25, 'admin user stuff' ); 
-- The email is the same, resulting to an error

----------- Clients (customers) ---------------------------[3 6]  
INSERT INTO SALON_USER ( user_type ,access_level , user_name   ,email , user_image,  password, phone_number, address, age )
      VALUES ('client',1,'client1','client1@email.com', 'userPlaceholder.png',  '$2b$12$X6WVyVmfu98fH7KxjDYSCuPCqAnJa/o.RHaPxZi6Ojgq0u4ZXo6Vm', '514-1234567', 'laval',22 ); 
INSERT INTO SALON_USER ( user_type ,access_level , user_name   ,email , user_image,  password, phone_number, address, age )
  VALUES ('client',1,'client2','client2@email.com', 'userPlaceholder.png',  '$2b$12$X6WVyVmfu98fH7KxjDYSCuPCqAnJa/o.RHaPxZi6Ojgq0u4ZXo6Vm', '514-1234567', 'laval',23 ); 
  INSERT INTO SALON_USER ( user_type ,access_level , user_name   ,email , user_image,  password, phone_number, address, age )
      VALUES ('client',1,'client3','client3@email.com', 'userPlaceholder.png',  '$2b$12$X6WVyVmfu98fH7KxjDYSCuPCqAnJa/o.RHaPxZi6Ojgq0u4ZXo6Vm', '514-1234567', 'laval',22 ); 
INSERT INTO SALON_USER ( user_type ,access_level , user_name   ,email , user_image,  password, phone_number, address, age )
  VALUES ('client',1,'client4','client4@email.com', 'userPlaceholder.png',  '$2b$12$X6WVyVmfu98fH7KxjDYSCuPCqemployeeAnJa/o.RHaPxZi6Ojgq0u4ZXo6Vm', '514-1234567', 'laval',23 ); 
----------- client eng ---------------------------  [7]
INSERT INTO SALON_USER ( user_type ,access_level , user_name   ,email , user_image,  password, phone_number, address, age )
  VALUES ( 'client',1,'client10eng','client10eng@email.com', 'userPlaceholder.png',  '$2b$12$X6WVyVmfu98fH7KxjDYSCuPCqAnJa/o.RHaPxZi6Ojgq0u4ZXo6Vm', '514-4567890', 'Montreal', 24  ); 
----------- Phy clients ---------------------------  [8]
INSERT INTO SALON_USER ( user_type ,access_level , user_name   ,email , user_image,  password, phone_number, address, age )
  VALUES ( 'client',1,'client1phy','client1phy@email.com', 'userPlaceholder.png',  '$2b$12$X6WVyVmfu98fH7KxjDYSCuPCqAnJa/o.RHaPxZi6Ojgq0u4ZXo6Vm', 'phy', 'Sce', 2022 ); 
----------  employees (professionals) ------------------------------- [9 11, 12 13, 14 15]
INSERT INTO SALON_USER ( user_type ,access_level , user_name   ,email , user_image, password, phone_number, address, age, pay_rate, speciality )
  VALUES ('professional',1,'employee1','employee1@email.com', 'userPlaceholder.png',  '$2b$12$X6WVyVmfu98fH7KxjDYSCuPCqAnJa/o.RHaPxZi6Ojgq0u4ZXo6Vm', '514-1234567', 'laval', 22, 15, 'employee' ); 
INSERT INTO SALON_USER ( user_type ,access_level , user_name   ,email , user_image,  password, phone_number, address, age, pay_rate, speciality )
  VALUES ('professional',1,'employee2','employee2@email.com', 'userPlaceholder.png',  '$2b$12$X6WVyVmfu98fH7KxjDYSCuPCqAnJa/o.RHaPxZi6Ojgq0u4ZXo6Vm', '514-1234567', 'laval', 22, 15, 'employee' ); 
INSERT INTO SALON_USER ( user_type ,access_level , user_name   ,email , user_image,  password, phone_number, address, age, pay_rate, speciality )
  VALUES ('professional',1,'employee3','employee3@email.com', 'userPlaceholder.png',  '$2b$12$X6WVyVmfu98fH7KxjDYSCuPCqAnJa/o.RHaPxZi6Ojgq0u4ZXo6Vm', '514-1234567', 'laval', 22 , 15, 'employee'); 
--------------------------------------------
INSERT INTO SALON_USER ( user_type ,access_level , user_name   ,email , user_image,  password, phone_number, address, age, pay_rate, speciality )
  VALUES ('professional',1,'employee4','employee4@email.com', 'userPlaceholder.png', '$2b$12$X6WVyVmfu98fH7KxjDYSCuPCqAnJa/o.RHaPxZi6Ojgq0u4ZXo6Vm', '514-4567890', 'Montreal', 24, 20, 'employee'  ); 
INSERT INTO SALON_USER ( user_type ,access_level , user_name   ,email , user_image,  password, phone_number, address, age, pay_rate, speciality )
  VALUES ('professional',1,'employee5','employee5@email.com', 'userPlaceholder.png',  '$2b$12$X6WVyVmfu98fH7KxjDYSCuPCqAnJa/o.RHaPxZi6Ojgq0u4ZXo6Vm', '514-4567890', 'Montreal', 24, 20, 'employee'  ); 
--------------------------------------------
INSERT INTO SALON_USER ( user_type ,access_level , user_name   ,email , user_image,  password, phone_number, address, age, pay_rate, speciality )
  VALUES ('professional',1,'employee6','employee6@email.com', 'userPlaceholder.png', '$2b$12$X6WVyVmfu98fH7KxjDYSCuPCqAnJa/o.RHaPxZi6Ojgq0u4ZXo6Vm', '438-12345678', 'ottawa', 28, 20, 'employee' ); 
INSERT INTO SALON_USER ( user_type ,access_level , user_name   ,email , user_image,  password, phone_number, address, age, pay_rate, speciality )
  VALUES ('professional',1,'employee7','employee7@email.com',  'userPlaceholder.png','$2b$12$X6WVyVmfu98fH7KxjDYSCuPCqAnJa/o.RHaPxZi6Ojgq0u4ZXo6Vm', '438-12345678', 'ottawa', 28, 25, 'employee' );
 
----------------------------------------------------
create table Salon_Service (
    service_id number(4) generated always as identity constraint salon_service_pk primary key,
    employee_id number(4),
    service_name varchar2(30),
    duration number(1),
    price number(5, 2),
    materials varchar2(35),
    constraint fk_service_appointment
        foreign key (employee_id)
        references Salon_User (user_id)
);

INSERT INTO SALON_SERVICE (employee_id, service_name , duration , price, materials) VALUES  (10, 'haircut', 1, 35, 'scissors, comb, clippers' );
INSERT INTO SALON_SERVICE (employee_id, service_name , duration , price, materials) VALUES  (11, 'beard trim + haircut', 1, 50, 'scissors, comb, clippers' );
INSERT INTO SALON_SERVICE (employee_id, service_name , duration , price, materials) VALUES  (12, 'manicure', 1, 25, 'manicure set');
INSERT INTO SALON_SERVICE (employee_id, service_name , duration , price, materials) VALUES  (13, 'braids', 1, 40, 'no equipments' );


create table Salon_Appointment (
    appointment_id number(4) generated always as identity constraint salon_appointment_pk primary key,
    status varchar2(10),
    approved number(1) default (0),
    date_appoint Date default SYSDATE,
    slot varchar2(10) default ('9-10'),
    venue varchar2(20) default ('cmn_room'),
    service_id number(4),
    customer_id number(4),
    service_name varchar2(30) not null,
    customer_name varchar2(30) not null,
    constraint fk_service_serviceid
        foreign key (service_id)
        references Salon_Service (service_id),
    constraint fk_appointment_customerid
        foreign key (customer_id)
        references Salon_User (user_id)
);

INSERT INTO SALON_APPOINTMENT (status , slot ,venue , service_id, customer_id, service_name, customer_name)  VALUES 
            ('requested', '10-11', 'room1', 1, 4, 'haircut', 'client1');
INSERT INTO SALON_APPOINTMENT (status , slot ,venue , service_id, customer_id, service_name, customer_name)  VALUES 
            ('requested', '9-10', 'room2', 2, 4, 'beard trim + haircut', 'client1');
INSERT INTO SALON_APPOINTMENT (status , slot ,venue , service_id, customer_id, service_name, customer_name) VALUES  
            ('requested', '3-4', 'chair1', 3, 5, 'manicure', 'client2');
INSERT INTO SALON_APPOINTMENT (status , slot ,venue , service_id, customer_id, service_name, customer_name) VALUES  
            ('requested', '3-4', 'chair2', 4, 6, 'braids', 'client3');

create table Salon_Report (
    report_id number(4) generated always as identity constraint salon_report_pk primary key,
    appointment_id number(4),
    status varchar2(10) default ('inactive'),
    date_report Date default SYSDATE,
    feedback_employee varchar2(500),
    feedback_customer varchar2(500),
    constraint fk_report_appointment
        foreign key (appointment_id)
        references Salon_Appointment (appointment_id)
);

INSERT INTO SALON_REPORT (appointment_id, status ,feedback_employee ,feedback_customer) VALUES  
  (1, 'closed', 'was a good hour', 'any time' );
INSERT INTO SALON_REPORT (appointment_id, status ,feedback_employee ,feedback_customer) VALUES  
  (2, 'grieve', 'Discrimination', 'any thing from this entitled client!' );
INSERT INTO SALON_REPORT (appointment_id, status ,feedback_employee ,feedback_customer) VALUES 
 (3, 'closed', 'nice job', 'thanks!' );
INSERT INTO SALON_REPORT (appointment_id, status ,feedback_employee ,feedback_customer) VALUES 
   (4, 'done', 'ok', 'ok??' );


CREATE TABLE Salon_Warning (
  warning_id number(4) generated always as identity constraint salon_warning_pk primary key,
  description varchar2(500),
  warned_user_id number(4),
  warning_issuer_id number(4),
  constraint fk_warning_warned_user_id
        foreign key (warned_user_id)
        references Salon_User (user_id),
  constraint fk_warning_warning_issuer_id
        foreign key (warning_issuer_id)
        references Salon_User (user_id)
);

CREATE TABLE Salon_Log (
  log_id NUMBER(4) GENERATED ALWAYS AS IDENTITY CONSTRAINT salon_log_pk PRIMARY KEY,
  user_name varchar2(30) not null,
  user_type varchar2(15),
  action_time DATE DEFAULT SYSDATE,
  action_type VARCHAR2(10),
  table_name VARCHAR2(30)
);

COMMIT;

SELECT * FROM Salon_Appointment;
SELECT * FROM Salon_Report;
SELECT * FROM Salon_Service;
SELECT * FROM Salon_User;