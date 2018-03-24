import os
#Imported libraries
from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename
#Imported local files
from login import LoginQuery
from spinbike import SpinBikeQuery
from bike_usage import BikeUsageAll
from checklist import ChecklistQuery
from usage_by_id import UsageByIDSelect
from managers import Managers
from schedule import ScheduleAll, Schedule
from location import Location, LocationQuery
from update_schedule import UpdateSchedule, RemoveSchedule
from bike_logs import BikeLogs
from maintenance import Maintenance
from users import EmailExists, EmailExistsOtherUser, NameExists, NameExistsOtherUser, ReturnUser, ReturnUserNamesAndIDs, CreateUser, EditUser
from hardware import Hardware
from image_transfer import UploadImage

UPLOAD_FOLDER = '/image/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
api = Api(app)
CORS(app)

#Add route to api with functionality in specified class
api.add_resource(BikeUsageAll, '/')
api.add_resource(LoginQuery, '/auth', endpoint='auth')
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
api.add_resource(UploadImage, '/upload_image')
#These route to users.py
api.add_resource(ReturnUserNamesAndIDs, '/users/get_usernames_and_ids')
api.add_resource(ReturnUser, '/users/get_user/<bm_id>')
api.add_resource(EmailExists, '/users/check_email/<email>')
api.add_resource(EmailExistsOtherUser, '/users/check_email/<email>&<bm_id>')
api.add_resource(NameExists, '/users/check_name/<bm_name>')
api.add_resource(NameExistsOtherUser, '/users/check_name/<bm_name>&<bm_id>')
api.add_resource(CreateUser, '/users/create_user')
api.add_resource(EditUser, '/users/edit_user')

if __name__ == '__main__':
    app.run(debug=True)