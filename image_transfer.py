import json
import os
from flask_restful import Resource, request
from SQLConnect import SQLConn
from flask import jsonify

UPLOAD_FOLDER = 'images/'


class UploadImage(Resource):
    def __init__(self):
        self.sql = SQLConn()

    def post(self):
        file = request.files['image']
        f = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(f)
        return True
