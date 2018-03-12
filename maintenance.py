import json
import datetime
from datetime import timedelta
from itertools import groupby
from flask_restful import Resource, request
from SQLConnect import SQLConn


def datetime_converter(date):
    if isinstance(date, datetime.datetime):
        return date.__str__()


#functions that convert a datetime type in a dictionnay into a string to be returnable in json
def convert_dict_datetime_str(list_dict, dict_key):
    for dict_to_change in list_dict:
        dict_to_change[dict_key] = datetime_converter(dict_to_change[dict_key])

class Maintenance(Resource):
    def __init__(self):
        self.sql = SQLConn()

    def get(self, bm_id):
        SELECT_SCHEDULE = "SELECT * FROM `maintenance` WHERE `bm_id`={bm_id}".format(
            bm_id=bm_id)
        schedule_of_manager = self.sql.select_query(SELECT_SCHEDULE)
        convert_dict_datetime_str(
            schedule_of_manager, 'maintenance_time')  #cast date type to str for json

        return schedule_of_manager
