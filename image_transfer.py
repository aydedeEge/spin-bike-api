import json
import os
from os import walk
from flask_restful import Resource, request
from SQLConnect import SQLConn
from flask import jsonify
from flask import send_file

UPLOAD_FOLDER = 'images/'


class UploadImage(Resource):
    def __init__(self):
        self.sql = SQLConn()

    def post(self):
        file = request.files['image']
        f = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(f)
        print(file.filename)
        return True

class LoadImage(Resource):
    def __init__(self):
        self.sql = SQLConn()

    def get(self):
        f = []
        for (dirpath, dirnames, filenames) in walk(UPLOAD_FOLDER):        
            for image in filenames:
                path = os.path.join(UPLOAD_FOLDER, image)
                f.append(path)
                break
        #only returns one random image for now
        return send_file(f[0], mimetype='image/png')
