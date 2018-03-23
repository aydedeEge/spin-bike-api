import json
import datetime

from flask import request
from flask_restful import Resource
from SQLConnect import SQLConn

class EditAccount(Resource):

    def __init__(self):
        self.sql = SQLConn()

    def get(self):
        GET_NAMES="SELECT bm_name, bm_id FROM `bike_manager`"
        result=self.sql.select_query(GET_NAMES)
        users = []
        for user in result:
            jsonUser = {
                "bm_name" : user['bm_name'],
                "bm_id" : user['bm_id']
                }
            jsonUser = json.dumps(jsonUser)
            users.append(jsonUser)
        return users
    
class EditAccountUser(Resource):

    def __init__(self):
        self.sql = SQLConn()

    def get(self, bm_id):
        GET_USER="SELECT * FROM `bike_manager` WHERE bm_id='" +bm_id +"'"
        result=self.sql.select_query(GET_USER)
        user=json.dumps(result[0])
        return user
