from flask_restful import Resource, request
from flask_httpauth import HTTPBasicAuth
from SQLConnect import SQLConn
from flask import jsonify

class SpinBikeQuery(Resource):
    
    def __init__(self):
        self.sql = SQLConn()

    def get(self):
        SELECT_QUERY="SELECT sb_id, make, l_id, model, data_collector FROM spin_bikes"
        result = self.sql.select_query(SELECT_QUERY)  
        return result