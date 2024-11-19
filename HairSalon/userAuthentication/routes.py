import os
from flask_bcrypt import Bcrypt
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.utils import secure_filename
from HairSalon.administration.users import User
from HairSalon.userAuthentication.forms import LoginForm, NewUserForm, PasswordModifForm
from HairSalon.qdb.database_ import db
from HairSalon.config import ConfigDev

b = Bcrypt()
userAuthentication = Blueprint('userAuthentication', __name__,
                                template_folder='templates', static_folder='static')


@userAuthentication.route("/register", methods=['GET', 'POST'])
def register():
    ''' This method is to register a new user '''
    user_form = NewUserForm()
    if request.method == 'POST':
        if user_form.validate_on_submit():
            user_type = user_form.user_type.data
            username = user_form.username.data
            email = user_form.email.data
            password = user_form.password.data
            user_image = user_form.user_image.data
            filename = secure_filename(user_image.filename)
            user_image.save(os.path.join(ConfigDev.UPLOAD_FOLDER, filename))
            hashed_password = b.generate_password_hash(password).decode('utf-8')
            phone_number = user_form.phone_number.data
            address = user_form.address.data
            age = user_form.age.data
            speciality = user_form.speciality.data
            users = db.get_user(user_form.username.data)
            if users == []:
                if(db.add_new_member(user_type, username, email, hashed_password, filename, phone_number, address, age, speciality)):
                    user = User(username)
                    login_user(user)
                    flash(("You registered successfully!", "success"))
                    return redirect(url_for('userAuthentication.user_profile'))
                else:
                    flash(("One of the fields resulted in an error. Try again!", "error"))
            else:
                flash(("This username is already taken!", "error"))
        else:
            print("Form validation errors:", user_form.errors)
            flash(("Registration failed, try again.", "error"))
    return render_template('register.html', user_form = user_form)

@userAuthentication.route("/login", methods=['GET', 'POST'])
def login():
    '''Logs an account to the website using the LoginFrom and 
    by performing the necessary validations '''
    login_form = LoginForm()
    if login_form.validate_on_submit():
        users = db.get_user(login_form.user_name.data)
        if users:
            myUser = users[0]
            if myUser['is_active'] == 0:
                flash(('Account is blocked! Cannot Log in', 'error'))
                return redirect(url_for('userAuthentication.register'))
            user_password = myUser['password']
            if b.check_password_hash(user_password, login_form.password.data):
                user = User(myUser['user_name'])
                login_user(user)
                flash(('Logged in successfully', 'success'))
                return redirect(url_for('userAuthentication.user_profile'))
            else :
                flash(('Password is incorrect', 'error'))
        else :
            flash(('Username did not match existing users', 'error'))
    return render_template('login.html', form=login_form)

@userAuthentication.route("/user/profile")
@login_required
def user_profile():
    '''Displays the current user's profile and their warning if they have one using profile.html '''
    warning = db.get_warning(current_user._User__user_id)
    context_data = {"page_title":"Profile Page", 
                    "main_heading":f"User: {current_user._User__user_name}"}
    context_data.update({"name":f"{current_user._User__user_name}",
                         "email":f"{current_user._User__email}", 
                         "picture":f"{current_user._User__user_image}",
                         "flags":f"{current_user._User__times_flagged}",
                         "address":f"{current_user._User__address}",
                         "age":f"{current_user._User__age}"})
    return render_template("profile.html", context=context_data, warning = warning)

@userAuthentication.route("/user/profile/passwordchange", methods=['GET', 'POST'])
@login_required
def user_change_password():
    '''Modifies the current user's password using the PasswordModifForm '''
    form = PasswordModifForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            password = form.password.data
            hashed_password = b.generate_password_hash(password).decode('utf-8')
            user_id = current_user._User__user_id
            db.update_password_user(user_id, hashed_password)
            flash(('Password changed successfully!', 'success'))
            return redirect(url_for('userAuthentication.user_profile'))
    return render_template("pwchange.html", form=form)

@userAuthentication.route("/user/logout")
@login_required
def logout():
    '''Logs the current user out of the website and redirects to the login page '''
    logout_user()
    flash(('Logged Out successfully', 'success'))
    return redirect(url_for('userAuthentication.login'))