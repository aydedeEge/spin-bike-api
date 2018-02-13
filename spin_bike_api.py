#Imported libraries
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

#Imported local files
from bike_usage_select import BikeUsageSelectQuery
from login import LoginQuery
from account_creation_insert import AccountCreationInsertQuery

app = Flask(__name__)
api = Api(app)
CORS(app)

#Add route to api with functionality in specified class
api.add_resource(BikeUsageSelectQuery, '/')
api.add_resource(LoginQuery, '/auth', endpoint='auth')
api.add_resource(AccountCreationInsertQuery, '/create')

if __name__ == '__main__':
    app.run(debug=True)