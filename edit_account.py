import json
import datetime

from flask import request
from flask_restful import Resource
from SQLConnect import SQLConn

class EditAccount(Resource):

    def __init__(self):
        self.sql = SQLConn()

    def get(self):
        GET_NAMES="SELECT bm_name FROM `bike_manager`"
        result=self.sql.select_query(GET_NAMES)
        return result