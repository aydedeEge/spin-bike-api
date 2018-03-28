import json
import os
from os import walk
from flask_restful import Resource, request
from SQLConnect import SQLConn
from flask import jsonify
from flask import send_file
from PIL import Image
from io import BytesIO
import base64

UPLOAD_FOLDER = 'images/'


class UploadImage(Resource):
    def __init__(self):
        self.sql = SQLConn()

    def post(self):
        try:
            data = request.form['data']
            data = json.loads(data)
            data_file = data['base']
            print(data_file)
            im = Image.open(BytesIO(base64.b64decode(data_file)))

            im.save(UPLOAD_FOLDER + " image.gif")
            return True
        except Exception as e:
            print(e)
            return False


class LoadImage(Resource):
    def __init__(self):
        self.sql = SQLConn()

    def get(self):
        try:
            with open(UPLOAD_FOLDER + " image.gif", "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())

            encoded_string = str(encoded_string)
            return encoded_string
        except Exception as e:
            print(e)
            return False
