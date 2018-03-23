#Imported libraries
from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api

#Imported local files
from login import LoginQuery
from spinbike import SpinBikeQuery
from bike_usage import BikeUsageAll
from checklist import ChecklistQuery
from usage_by_id import UsageByIDSelect
from account_creation_insert import AccountCreationInsertQuery
from managers import Managers
from schedule import ScheduleAll, Schedule
from location import Location, LocationQuery
from update_schedule import UpdateSchedule, RemoveSchedule
from bike_logs import BikeLogs
from maintenance import Maintenance
from edit_account import EditAccount, EditAccountUser
from user_validation import EmailExists, EmailExistsOtherUser, NameExists, NameExistsOtherUser
from hardware import Hardware

app = Flask(__name__)
api = Api(app)
CORS(app)

#Add route to api with functionality in specified class
api.add_resource(BikeUsageAll, '/')
api.add_resource(LoginQuery, '/auth', endpoint='auth')
api.add_resource(AccountCreationInsertQuery, '/create')
api.add_resource(ChecklistQuery, '/checklist')
api.add_resource(LocationQuery, '/location')
api.add_resource(SpinBikeQuery, '/spinbike')
api.add_resource(UsageByIDSelect, '/usage/<bike_id>')
api.add_resource(Managers, '/managers')
api.add_resource(ScheduleAll, '/schedule_all')
api.add_resource(Schedule, '/schedule/<bm_id>')
api.add_resource(Location, '/location/<l_id>')
api.add_resource(UpdateSchedule, '/update_schedule')
api.add_resource(RemoveSchedule, '/delete_schedule')
api.add_resource(BikeLogs, '/bikelogs/<start_date>&<end_date>')
api.add_resource(Maintenance, '/maintenance/<bm_id>')
api.add_resource(EditAccount, '/edit')
api.add_resource(EditAccountUser, '/edit/<bm_id>')
api.add_resource(EmailExists, '/check_email/<email>')
api.add_resource(EmailExistsOtherUser, '/check_email/<email>&<bm_id>')
api.add_resource(NameExists, '/check_name/<bm_name>')
api.add_resource(NameExistsOtherUser, '/check_name/<bm_name>&<bm_id>')
api.add_resource(Hardware, '/hardware')

if __name__ == '__main__':
    app.run(debug=True)