import json
import datetime

from flask_restful import Resource, request
from flask_httpauth import HTTPBasicAuth
from SQLConnect import SQLConn
from flask import jsonify

class Hardware(Resource):

    def __init__(self):
        self.sql = SQLConn()

    def get(self):

        args = request.args
        time_add = datetime.datetime.now()
        sb_id = args['sb_id']
        duration = args['duration']

        # insert into mainteance table
        INSERT_QUERY = "INSERT INTO sbg_db.bike_usage VALUES ({sb_id},'{datetime}', {duration})".format(
            sb_id=sb_id,
            datetime=time_add,
            duration=duration)
        
        result = self.sql.insert_query(INSERT_QUERY)