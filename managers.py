import json
from flask_restful import Resource
from SQLConnect import SQLConn
from itertools import groupby


class Managers(Resource):

    CARETAKER = "caretaker"
    ADMIN = "admin"

    def __init__(self):
        self.sql = SQLConn()

    def get(self):
        #obtain all managers from database
        ALL_MANAGERS = "SELECT * FROM `bike_manager`"
        all_managers_entries = self.sql.select_query(ALL_MANAGERS)

        #group managers by caretakers or admin
        managers_dict = {}
        for role, g in groupby(all_managers_entries, lambda x: x['role']):
            managers_dict[role] = list(g)

        return managers_dict
