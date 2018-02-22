import json
import datetime

from flask_restful import Resource, request
from flask_httpauth import HTTPBasicAuth
from SQLConnect import SQLConn
from flask import jsonify

class SpinBikeQuery(Resource):
    
    def __init__(self):
        self.sql = SQLConn()

    def get(self):
        args = request.args

