#Imported libraries
from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api

#Imported local files
from login import LoginQuery
from bike_usage import BikeUsageAll
from checklist import ChecklistQuery
from usage_by_id import UsageByIDSelect
from bike_usage_select import BikeUsageSelectQuery
from account_creation_insert import AccountCreationInsertQuery

app = Flask(__name__)
api = Api(app)
CORS(app)

#Add route to api with functionality in specified class
api.add_resource(BikeUsageAll, '/')
api.add_resource(LoginQuery, '/auth', endpoint='auth')
api.add_resource(AccountCreationInsertQuery, '/create')
api.add_resource(ChecklistQuery, '/checklist')
api.add_resource(UsageByIDSelect, '/usage/<bike_id>')


if __name__ == '__main__':
    app.run(debug=True)