# Import flask and template operators
from flask import Flask, render_template, Blueprint
from flask_restful import Resource, Api

# Import SQLAlchemy
#from flask.ext.sqlalchemy import SQLAlchemy
# define db connection
# psql_db = PostgresqlDatabase('aurel', user='aurel')
# psql_db.connect();

# Import a module / component using its blueprint handler variable (mod_core)
from mod_core.controllers import mod_core as core_module

# Define the WSGI application object
app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
# db = SQLAlchemy(app)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Register blueprint(s)
app.register_blueprint(core_module)
# app.register_blueprint(xyz_module)
# ..
app.register_blueprint(api_bp)
# Build the database:
# This will create the database file using SQLAlchemy
# db.create_all()
