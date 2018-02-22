import json
import datetime

from flask_restful import Resource, request
from flask_httpauth import HTTPBasicAuth
from SQLConnect import SQLConn
from flask import jsonify

class ChecklistQuery(Resource):
    
    def __init__(self):
        self.sql = SQLConn()

    def getID(self):
        """
            Find the largest m_id and return max(m_id) incremented by 1
        """
        SELECT_QUERY = "SELECT max(m_id) FROM maintenance"
        result = self.sql.select_query(SELECT_QUERY)
        print(result)
        if(result[0]['max(m_id)'] != None):
            return result[0]['max(m_id)']+1
        else:
            return 1


    def get(self):
        """
            Insert the request 
        """
        args = request.args
        m_id = self.getID()
        maintenance_time = datetime.datetime.now()
        # bm_id = 1
        # l_id = 1
        # plants_watered = 1
        # clean = 1
        # comments = 1
        # done = 1
        # comp_state = 1
        # sb_id = 1
        bm_id = args['bm_id']
        l_id = args['l_id']
        plants_watered =  args['water']
        clean = args['clean']
        comments = args['comments']
        done = args['done']
        comp_state =  args['comp_state']
        sb_id = args['sb_id']

        # insert into mainteance table
        INSERT_QUERY = "INSERT INTO maintenance VALUES ({m_id},'{date}', {bm_id}, {l_id}, {plants}, {clean}, {comments}, {done})".format(
            m_id=m_id,
            date=maintenance_time,
            bm_id=bm_id,
            l_id=l_id,
            plants=plants_watered,
            clean=clean,
            comments=comments,
            done=done)
        result = self.sql.insert_query(INSERT_QUERY)

        # insert into bike_state table
        INSERT_QUERY = "INSERT INTO bike_state VALUES ({m_id}, {sb_id}, {comp_state})".format(
            m_id=m_id,
            sb_id=sb_id,
            comp_state=comp_state)
        result = self.sql.insert_query(INSERT_QUERY)
