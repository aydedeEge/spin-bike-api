import json
import datetime

from flask_restful import Resource, request
from flask_httpauth import HTTPBasicAuth
from SQLConnect import SQLConn
from flask import jsonify

class LocationQuery(Resource):
    
    def __init__(self):
        self.sql = SQLConn()

    def get(self):
        SELECT_QUERY="SELECT * FROM location"
        result = self.sql.select_query(SELECT_QUERY)  
        return result



