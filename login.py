import json
import datetime

from flask_restful import Resource, request
from flask_httpauth import HTTPBasicAuth
from SQLConnect import SQLConn
from flask import jsonify

class LoginQuery(Resource):
    
    def __init__(self):
        self.sql = SQLConn()

    def get(self):
        args = request.args
        username = args['username']
        password = args['pwd']
        #form request to db
        GET_PASSWORD="SELECT pwd FROM `bike_manager` WHERE bm_name='"+username+"'"
        result = self.sql.select_query(GET_PASSWORD)  
        #check if user exista and password matches
        if(len(result) == 1):
            if(result[0]['pwd'] == password):
                return True
        return False




    