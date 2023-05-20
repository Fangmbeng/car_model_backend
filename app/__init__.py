# Import the Flask Class from the flask module - will be main object
from flask import Flask
# Import SQLAlchemy and Migrate from their modules
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
# Import the Config class from the config module - will have all of the app's configurations
from config import Config
from .api.routes import api
from .authentication.routes import auth
from .site.routes import site
from .models import db as root_db, login, ma
# Create an instance of the Flask Class called app
app = Flask(__name__)
app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)
# Configure the app using the Config class
app.config.from_object(Config)
app.config['SECRET_KEY'] = "Anything"

# Create an instance of SQLAlchemy to represent our database
root_db.init_app(app)
# Create an instance of Migrate to represent our migration engine
migrate = Migrate(app, root_db)
ma.init_app(app)
# Create an instance of LoginManager to set up login functionality
login.init_app(app)
# Set the login view to redirect unauthorized users
login.login_view = 'login'
login.login_message = 'You must be logged in to perform this action'
login.login_message_category = 'danger'


# import all of the routes from the routes file into the current folder
