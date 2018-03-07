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
        else:
            INSERT_SCHEDULE = "INSERT INTO `schedule` (`l_id` ,`bm_id`, "
            list_days = data["days"]
            timeDeltas = []
            for i in range(len(list_days)):
                day = list_days[i]
                dayColumn, timedelta = getSchedule(day)
                timeDeltas.append(timedelta)
                if dayColumn > 4:  # cant schedule during the weekend
                    return "can't schedule during weekends"
                INSERT_SCHEDULE += "`" + str(dayColumn) + "`"
                if i < len(list_days) - 1:
                    INSERT_SCHEDULE += ", "

            INSERT_SCHEDULE += ") VALUES ('" + data["l_id"] + "', '" + data["bm_id"] + "',"
            for i in range(len(list_days)):
                INSERT_SCHEDULE += "'" + timedelta + "'"
                if i < len(list_days) - 1:
                    INSERT_SCHEDULE += ", "
            INSERT_SCHEDULE += ")"
            try:
                self.sql.insert_query(INSERT_SCHEDULE)
            except Exception as e:
                print(e)
                return False
            return True
        return False


class RemoveSchedule(Resource):
    def __init__(self):
        self.sql = SQLConn()

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
                    dayColumn) + "` = null "
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
