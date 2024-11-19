''' This is the main app that runs the application! '''
from HairSalon import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(port = 5015, debug = True)
