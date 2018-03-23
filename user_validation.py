import json
import datetime

from flask import request
from flask_restful import Resource
from SQLConnect import SQLConn

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


# These two functions will check the server to see if account details are used by
# any user that isnt the user given by bm_id. This allows us to maintain the same
# account information for the same user, should the user request to change some other
# detail
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