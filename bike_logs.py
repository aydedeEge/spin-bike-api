import json 
import datetime
import decimal
import re
from itertools import groupby
from flask_restful import Resource
from SQLConnect import SQLConn
from bike_usage import datetime_converter, convert_dict_datetime_str

class BikeLogs(Resource):

    def __init__(self):
        self.sql = SQLConn()

    def get(self, start_date='0-0-0', end_date="3000-0-0"):
        #query bikes info
        start_date = self.validate_date(start_date, 'start')
        end_date = self.validate_date(end_date, 'end')
        
        LOG_DATA = """
            SELECT 
                l.l_id as Location_ID, 
                l.address as Address, 
                s.sb_id as Bike_ID, 
                s.model as Bike_Model,
                SUM(bu.duration) as Total_Usage,
                COUNT(bu.duration) as Usage_Instances
            FROM 
                `location` l 
            JOIN 
                `spin_bikes` s 
            ON 
                l.l_id=s.l_id 
            JOIN 
                `bike_usage` bu 
            ON 
                bu.sb_id=s.sb_id 
            JOIN
                `maintenance` m
            ON
                l.l_id=m.l_id
            WHERE 
                bu.start_time>='{start_date}'
            AND 
                bu.start_time<'{end_date}'
            GROUP BY 
                l.l_id, 
                l.address, 
                s.sb_id, 
                s.model;
        """.format(start_date=start_date, end_date=end_date)
        result = self.sql.select_query(LOG_DATA)
        result = json.dumps(result, default=self.decimal_default)
        result = json.loads(result)
        return result

    def decimal_default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        raise TypeError

    def validate_date(self, date, start_or_end):
        r = re.compile('.*-.*-.*')
        if r.match(date) is None:
            if(start_or_end == "start"):
                return '0-0-0'
            else:
                return '3000-0-0'
        else:
            return date