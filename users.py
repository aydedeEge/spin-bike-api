import json
import datetime

from flask import request
from flask_restful import Resource
from SQLConnect import SQLConn

class ReturnUserNamesAndIDs(Resource):

    def __init__(self):
        self.sql = SQLConn()

    def get(self):
        GET_NAMES="SELECT bm_name, bm_id FROM `bike_manager`"
        result=self.sql.select_query(GET_NAMES)
        users = []
        for user in result:
            jsonUser = {
                "bm_name" : user['bm_name'],
                "bm_id" : user['bm_id']
                }
            jsonUser = json.dumps(jsonUser)
            users.append(jsonUser)
        return users
    
class ReturnUser(Resource):

    def __init__(self):
        self.sql = SQLConn()

    def get(self, bm_id):
        GET_USER="SELECT * FROM `bike_manager` WHERE bm_id='" +bm_id +"'"
        result=self.sql.select_query(GET_USER)
        user=json.dumps(result[0])
        return user
    
class NameExists(Resource):
    def __init__(self):
        self.sql = SQLConn()
        

    def get(self, bm_name):
        GET_NAMES="SELECT bm_name FROM `bike_manager` WHERE bm_name ='" +bm_name +"'"
        result = self.sql.select_query(GET_NAMES)
        if(len(result) >= 1):
            return True
        return False

class EmailExists(Resource):
	def __init__(self):
		self.sql = SQLConn()

	def get(self, email):
		GET_EMAILS="SELECT email FROM `bike_manager` WHERE email ='" +email +"'"
		result = self.sql.select_query(GET_EMAILS)
		if(len(result) >= 1):
			return True
		return False


class NameExistsOtherUser(Resource):
    def __init__(self):
        self.sql = SQLConn()
    
    def get(self, bm_name, bm_id):
        GET_NAMES="SELECT bm_name FROM `bike_manager` WHERE bm_name ='" +bm_name +"' AND bm_id !='" +bm_id +"'"
        result = self.sql.select_query(GET_NAMES)
        if(len(result) >= 1):
            return True
        return False

class EmailExistsOtherUser(Resource):
	def __init__(self):
		self.sql = SQLConn()

	def get(self, email, bm_id):
		GET_EMAILS="SELECT email FROM `bike_manager` WHERE email ='" +email +"' AND bm_id !='" +bm_id +"'"
		result = self.sql.select_query(GET_EMAILS)
		if(len(result) >= 1):
			return True
		return False

class CreateUser(Resource):
    def __init__(self):
        self.sql = SQLConn()

    #Form data must be in the form:
    # {"key": "value", "key": "value", ...} 
    def put(self):
        INSERT_USER = "INSERT INTO `bike_manager` (`email`, `pwd`, `bm_name`, `role`) VALUES ('{email}' ,'{pwd}', '{bm_name}', '{role}')"
        data = request.form['data']
        data = json.loads(data)
        #Do check to make sure not already in db
        try:
            self.sql.insert_query(INSERT_USER.format(
                email=data["email"],
                pwd=data["pwd"],
                bm_name=data["bm_name"],
                role=data["role"]
            ))
        except Exception as e:
            return False
        return True

class EditUser(Resource):
    def __init__(self):
        self.sql = SQLConn()

    def put(self):
        data = request.form['data']
        data = json.loads(data)
        UPDATE_USER = "UPDATE `bike_manager` SET email='" +data["email"] +"', pwd='" +data["pwd"] +"', bm_name='" +data["bm_name"] +"', role='" +data["role"] +"' WHERE bm_id ='" +bm_id +"'"
        
        try:
            request = self.sql.update_query(UPDATE_USER);
        except Exception as e:
            return False
        return True