import json
import datetime

from flask import request
from flask_restful import Resource
from SQLConnect import SQLConn

class AccountCreationInsertQuery(Resource):

    def __init__(self):
        self.sql = SQLConn()

    #Form data must be in the form:
    # {"key": "value", "key": "value", ...} 
    def put(self):
        INSERT_USER = "INSERT INTO `bike_manager` (`email`, `pwd`, `bm_name`, `role`) VALUES ('{email}' ,'{pwd}', '{bm_name}', '{role}')"
        data = request.form['data']
        data = json.loads(data)
        #Do check to make sure not already in db
        try:
            self.sql.insert_query(INSERT_USER.format(
                email=data["email"],
                pwd=data["pwd"],
                bm_name=data["bm_name"],
                role=data["role"]
            ))
        except Exception as e:
            return False
        return True