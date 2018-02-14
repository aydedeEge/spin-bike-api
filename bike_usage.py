import json
import datetime
from itertools import groupby
from flask_restful import Resource
from SQLConnect import SQLConn


class BikeUsageAll(Resource):
    def __init__(self):
        self.sql = SQLConn()

    def datetime_converter(self, date):
        if isinstance(date, datetime.datetime):
            return date.__str__()

    def get_bikes(self, bike_ids):
        #query bikes info
        BIKE_INFO = "SELECT * FROM `spin_bikes` WHERE sb_id =" + str(
            bike_ids[0])
        for bike_id in bike_ids[1:]:
            BIKE_INFO += (" OR sb_id =" + str(bike_id))
        bikes_info = self.sql.select_query(BIKE_INFO)
        return bikes_info

    def get_locations(self, location_ids):
        #query location info
        LOCATION_INFO = "SELECT * FROM `location` WHERE l_id = " + str(
            location_ids[0])
        for location_id in location_ids[1:]:
            LOCATION_INFO += (" OR l_id =" + str(location_id))
        location_info = self.sql.select_query(LOCATION_INFO)
        return location_info

    def get(self):
        #obtain total usage right away and goes backwards to locations
        ALL_BIKE_USAGE = "SELECT * FROM `bike_usage`"
        bike_usage_entries = self.sql.select_query(ALL_BIKE_USAGE)

        #group usage entries by bike_id to know which bikes need to be queried
        bike_usage_dict = {}
        for b_id, g in groupby(bike_usage_entries, lambda x: x['sb_id']):
            bike_usage_dict[b_id] = list(g)
        bikes_ids = list(bike_usage_dict.keys())

        bikes_info = self.get_bikes(bikes_ids)  #get the needed bikes

        #group bikes by location id to know which locations need to be queried
        location_dict = {}
        for l_id, g in groupby(bikes_info, lambda x: x['l_id']):
            location_dict[l_id] = list(g)
        location_ids = list(location_dict.keys())

        location_info = self.get_locations(
            location_ids)  #get the needed locations

        #Build the dictionnary object to dump to a json object
        for bike in bikes_info:
            bike['usage'] = bike_usage_dict[bike[
                'sb_id']]  # add the bike usage to the bike dictionnary

        for location in location_info:
            location['bikes'] = location_dict[location[
                'l_id']]  # add the bikes to the location dictionnary

        bike_usage_entries = json.dumps(
            location_info, default=self.datetime_converter)
        return bike_usage_entries
