import json
import datetime

from flask_restful import Resource
from flask import jsonify
from flask_httpauth import HTTPBasicAuth
from SQLConnect import SQLConn

class LoginQuery(Resource):
    
    def __init__(self):
        self.sql = SQLConn()

    def get(self, username, password):
        GET_PASSWORD="SELECT pwd FROM `bike_manager` WHERE bm_name='"+username+"'"
        print(GET_PASSWORD)
        result = self.sql.select_query(GET_PASSWORD)  
        if(len(result) == 1):
            print(type(result[0]))
            if(result[0]['pwd'] == password):
                return 'yes'
        return 'no'




    