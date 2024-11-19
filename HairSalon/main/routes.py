from flask import Blueprint, render_template
from flask_login import current_user
from HairSalon.qdb.database_ import db

main = Blueprint('main', __name__, template_folder='templates', static_folder='static')

@main.route("/")
def home():
    '''This renders the home page'''
    appointmentsdb = db.get_appointments()

    if current_user.is_authenticated:
        # The user is logged in
        return render_template('home.html', appointments=appointmentsdb,
                                current_user_id=current_user._User__user_id)
    else:
        # The user is not logged in
        return render_template('home.html', appointments=appointmentsdb)
    
@main.route("/about")
def about_page():
    '''Renders about_page.html '''
    return render_template('about_page.html')
