This is our Hair Salon project.

Visitors can visit the website, but have limited interaction with the interface (can't view details of appointments for example). They can register as a client member or a professional member.

Members are registered users (customers or employees) and they can see apointment details. They can create, update and delete their own appointment. They can check their profile and modify their password. They can also create a new report only on appointments that belong to them. Professional members can also create a service. They cannot create a report, but they can reply to reports only addressed to them.

The Admin_User can Delete, Warn, Block or Flag member accounts, but not other admin accounts. They can also add a member. They can also access the audit logs.

The Admin_Appoint can Modify or delete existing appointments and existing reports. They can also add an appointment and a report. They can also access the audit logs.

The Admin_Super can do the same things as the Admin_User, but he can also Delete, Warn, Block or flag Admin accounts as well. He can do the same operations as the Admin_Appoint as well.

Every user type other than visitor can login and logout, has a profile with their information and their profile picture.

Username, user type and profile picture are always shown in the top right.

There is also an API tab for accessing the API and trying the different requests to accecss/modify the information.

To run the project:
1 - Make sure to have the correct environment variables set up for db connection
2 - activate your virtual environment and "pip install -r requirements.txt"
3 - cd into ./HairSalon/qbd and run the command "python database_.py" to run schema.sql
(Will have to modify import statement in database_.py "from HairSalon.qdb import config_db" to "import config_db"  for it to run)
4 - Once ran, restore import statement to "from HairSalon.qdb import config_db"
5 - cd ../../
6 - run "python app.py"


