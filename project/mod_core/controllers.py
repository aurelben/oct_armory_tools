# Import flask dependencies
from flask import Blueprint

# Import password / encryption helper tools
# from werkzeug import check_password_hash
from mod_core.models import *
from flask_restful import Api

from flask.views import MethodView

# Import module forms
# from app.mod_auth.forms import LoginForm
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Import module models (i.e. User)


# Define the blueprint: 'core', set its url prefix: app.url/auth
mod_core = Blueprint('core', __name__, url_prefix='/core/v1')
mode_core_api = Api(mod_core)


def abort_if_officer_doesnt_exist(officer_id):
    if officer_id not in Officer.get():
        abort(404, message="Officer {} doesn't exist".format(officer_id))


def abort_if_plan_doesnt_exist(officer_id):
    if plan_id not in Plan.get():
        abort(404, message="Plan {} doesn't exist".format(plan_id))


class MyOfficer(MethodView):
    def get(self, officer_id):
        abort_if_officer_doesnt_exist(officer_id)
        return Officer.get(id=officer_id)

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
        new_off.name = args['name']
        new_off.save()
        return new_off.get(), 201


class MyPlan(MethodView):
    def get(self, plan_id):
        abort_if_plan_doesnt_exist(officer_id)
        return Plan.get(id=officer_id)

    def delete(self, plan_id):
        abort_if_plan_doesnt_exist(officer_id)


class Plans(MethodView):
    '''Get list of all Officers and Add new one'''
    def get(self):
        ''''Get all Officers from db an return response as Json'''
        return Officer.get()

    def post(self):
        ''' Add new officers '''
        args.parser.parse_args()
        new_off = Officer()
        new_off.name = args['name']
        new_off.save()
        return new_off.get(), 201


# # Set the route and accepted methods
# @mod_core.route('/getofficers', methods=['GET', 'POST'])
# def getofficers():

#     # If sign in form is submitted
#     return

##
# Add Api routes

mode_core_api.add_resource(Officers, '/officers')
mode_core_api.add_resource(MyOfficer, '/officer/<officer_id>')
