import json
import datetime

from flask import request
from flask_restful import Resource
from SQLConnect import SQLConn

class AccountCreationInsertQuery(Resource):

    def __init__(self):
        self.sql = SQLConn()

    

    def get_usernames(self):
		GET_PASSWORD="SELECT bm_name FROM `bike_manager`"
		result = self.sql.select_query(GET_PASSWORD)
		for name in result:
			print(name)
		