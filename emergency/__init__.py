from flask import Flask
from emergency.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    with app.app_context():
#   from blueprints.patients.routes import patients
#   from blueprints.doctors.routes import doctors
        from emergency.blueprints.main.routes import main
        from emergency.blueprints.rooms.routes import emergency
#   from blueprints.errors.handlers import errors
#   from blueprints.admin.routes import admin

#   app.register_blueprint(patients)
#   app.register_blueprint(doctors)
        app.register_blueprint(main)
#   app.register_blueprint(errors)
        app.register_blueprint(emergency)
#   app.register_blueprint(admin)

    return app
