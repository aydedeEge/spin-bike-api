import json
from datetime import datetime

from flask import request
from flask_restful import Resource
from SQLConnect import SQLConn


#"2018-03-12 15:00:00"
def getSchedule(day):
    datetime_object = datetime.strptime(day, '%Y-%m-%d %H:%M:%S')
    weekDay = datetime_object.weekday()
    time = datetime_object.time().__str__()
    return weekDay, time


class UpdateSchedule(Resource):
    def __init__(self):
        self.sql = SQLConn()

    #AJAX example call
    # form.append("data", "{\"l_id\": \"2\", \"bm_id\": \"7\",\"days\":[\"2018-03-15 16:00:00\",\"2018-03-14 16:00:00\"]}");

    # var settings = {
    #   "async": true,
    #   "crossDomain": true,
    #   "url": "http://localhost:5000/update_schedule",
    #   "method": "PUT",
    #   "headers": {
    #     "Content-Type": "application/x-www-form-urlencoded",
    #     "Cache-Control": "no-cache",
    #     "Postman-Token": "329dac58-6076-6ca2-c00e-cf7ad8c89a3d"
    #   },
    #   "processData": false,
    #   "contentType": false,
    #   "mimeType": "multipart/form-data",
    #   "data": form
    # }

    # $.ajax(settings).done(function (response) {
    #   console.log(response);
    # });
    def put(self):
        #first check that the requested entry exist
        SELECT_SCHEDULE = "SELECT * FROM `schedule` WHERE bm_id ='{bm_id}' AND l_id = '{l_id}'"
        data = request.form['data']
        data = json.loads(data)
        check_if_exist = self.sql.select_query(
            SELECT_SCHEDULE.format(bm_id=data["bm_id"], l_id=data["l_id"]))
        if check_if_exist:
            UPDATE_SCHEDULE = "UPDATE `schedule` SET "
            list_days = data["days"]
            for i in range(len(list_days)):
                day = list_days[i]
                dayColumn, timedelta = getSchedule(day)
                if dayColumn > 4:  # cant schedule during the weekend
                    return "can't schedule during weekends"
                UPDATE_SCHEDULE += " `" + str(
                    dayColumn) + "` = '" + timedelta + "'"
                if i < len(list_days) - 1:
                    UPDATE_SCHEDULE += ","

            UPDATE_SCHEDULE += "WHERE bm_id ='{bm_id}' AND l_id = '{l_id}'"
            try:
                print(
                    UPDATE_SCHEDULE.format(
                        bm_id=data["bm_id"], l_id=data["l_id"]))
                self.sql.insert_query(
                    UPDATE_SCHEDULE.format(
                        bm_id=data["bm_id"], l_id=data["l_id"]))
            except Exception as e:
                print(e)
                return False
            return True

        return False
