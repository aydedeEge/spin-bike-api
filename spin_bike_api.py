#Imported libraries
from flask import Flask
from flask_restful import Resource, Api

#Imported local files
from bike_usage_select import BikeUsageSelectQuery

app = Flask(__name__)
api = Api(app)

#Add route to api with functionality in specified class
api.add_resource(BikeUsageSelectQuery, '/')

if __name__ == '__main__':
    app.run(debug=True)