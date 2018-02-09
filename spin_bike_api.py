#Imported libraries
from flask import Flask
from flask_restful import Resource, Api

#Imported local files
from bike_usage_select import BikeUsageSelectQuery
from login import LoginQuery

app = Flask(__name__)
api = Api(app)

#Add route to api with functionality in specified class
api.add_resource(BikeUsageSelectQuery, '/')
api.add_resource(LoginQuery, '/auth/<username>/<password>')

if __name__ == '__main__':
    app.run(debug=True)