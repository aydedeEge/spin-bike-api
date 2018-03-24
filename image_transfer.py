import json

from flask_restful import Resource, request
from SQLConnect import SQLConn
from flask import jsonify


class UploadImage(Resource):
    def __init__(self):
        self.sql = SQLConn()

    def get(self):
        return 'tabarnak val'
