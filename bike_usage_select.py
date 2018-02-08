import json
import datetime

from flask_restful import Resource
from SQLConnect import SQLConn

class BikeUsageSelectQuery(Resource):

    def __init__(self):
        self.sql = SQLConn()

    def datetime_converter(self, date):
        if isinstance(date, datetime.datetime):
            return date.__str__()

    def get(self):
        ALL_BIKE_USAGE="SELECT * FROM `bike_usage`"
        result = self.sql.select_query(ALL_BIKE_USAGE)
        result = json.dumps(result, default=self.datetime_converter)
        return result