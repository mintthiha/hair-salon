from flask import Flask
from flask_login import LoginManager
from HairSalon.config import ConfigDev
from HairSalon.administration.users import User
from HairSalon.administration.routes import administration
from HairSalon.appointment.routes import appointment
from HairSalon.main.routes import main
from HairSalon.report.routes import report
from HairSalon.userAuthentication.routes import userAuthentication
from HairSalon.api.routes import api_blueprint

login_manager = LoginManager()

def create_app():
    ''' Registers all blueprints '''
    app = Flask(__name__)
    app.config.from_object(ConfigDev)

    app.register_blueprint(administration)
    app.register_blueprint(appointment)
    app.register_blueprint(main)
    app.register_blueprint(report)
    app.register_blueprint(userAuthentication)
    app.register_blueprint(api_blueprint)

    login_manager.init_app(app)
    return app

@login_manager.user_loader
def load_user(user_id):
    ''' Loads the current user '''
    user = User(user_id)
    return user
