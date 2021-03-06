import json
import datetime
from itertools import groupby
from flask_restful import Resource, request
from SQLConnect import SQLConn
from flask import jsonify


def get_locations(sql, location_ids):
    #query location info
    LOCATION_INFO = "SELECT * FROM `location` WHERE l_id = " + str(
        location_ids[0])
    for location_id in location_ids[1:]:
        LOCATION_INFO += (" OR l_id =" + str(location_id))
    location_info = sql.select_query(LOCATION_INFO)
    return location_info


class Location(Resource):
    def __init__(self):
        self.sql = SQLConn()

    def get(self, l_id):
        location_info = get_locations(self.sql, (l_id))
        return location_info[0]


class LocationQuery(Resource):
    def __init__(self):
        self.sql = SQLConn()

    def get(self):
        SELECT_QUERY = "SELECT * FROM location"
        result = self.sql.select_query(SELECT_QUERY)
        return result
