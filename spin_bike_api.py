#Imported libraries
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

#Imported local files
from bike_usage import BikeUsageAll
from login import LoginQuery
from account_creation_insert import AccountCreationInsertQuery
from usage_by_id import UsageByIDSelect

app = Flask(__name__)
api = Api(app)
CORS(app)

#Add route to api with functionality in specified class
api.add_resource(BikeUsageAll, '/')
api.add_resource(LoginQuery, '/auth', endpoint='auth')
api.add_resource(AccountCreationInsertQuery, '/create')
api.add_resource(UsageByIDSelect, '/usage/<bike_id>')

if __name__ == '__main__':
    app.run(debug=True)