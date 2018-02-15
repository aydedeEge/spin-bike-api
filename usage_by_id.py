import json
import datetime
from itertools import groupby
from flask_restful import Resource
from SQLConnect import SQLConn

class UsageByIDSelect(Resource):

    def __init__(self):
        self.sql = SQLConn()

    def to_serializable(self, val):
        if isinstance(val, datetime.datetime):
            return val.isoformat()

    def get(self, bike_id):
        SELECT = "SELECT * FROM `bike_usage` WHERE `sb_id`={bike_id}".format(bike_id=bike_id)
        result = self.sql.select_query(SELECT)
        result = json.dumps(result, default=self.to_serializable)
        return results