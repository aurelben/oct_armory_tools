# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, session, redirect, url_for

# Import password / encryption helper tools
# from werkzeug import check_password_hash

from flask_restful import Resource, Api

from flask.views import MethodView

# Import module forms
# from app.mod_auth.forms import LoginForm
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Import module models (i.e. User)
from mod_core.models import *

# Define the blueprint: 'core', set its url prefix: app.url/auth
mod_core = Blueprint('core', __name__, url_prefix='/core')

def abort_if_officer_doesnt_exist(officer_id):
    if officer_id not in officer:
        abort(404, message="Officer {} doesn't exist".format(officer_id))

class MyOfficer(MethodView):
    def get(self, officer_id):
        abort_if_officer_doesnt_exist(officer_id)
        return Officer.get(id = officer_id)

    def delete(self, officer_id):
        abort_if_officer_doesnt_exist(officer_id)

class Officers(MethodView):
    '''Get list of all Officers and Add new one'''
    def get(self):
        ''''Get all Officers from db an return response as Json'''
        return Officer.get()

    def post(self):
        ''' Add new officers '''
        args.parser.parse_args()
        new_off = Officer()
        new_off.name =  args['name']
        new_off.save()
        return new_off.get(), 201



# # Set the route and accepted methods
# @mod_core.route('/getofficers', methods=['GET', 'POST'])
# def getofficers():

#     # If sign in form is submitted
#     return 
##
# Add Api routes
# 

api.add_resource(Officers, '/officers')
api.add_resource(MyOfficer, '/officer/<officer_id>')