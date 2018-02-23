import json
import datetime
from datetime import timedelta
from itertools import groupby
from flask_restful import Resource, request
from SQLConnect import SQLConn

DAYS = ["0", "1", "2", "3", "4"]  # monday to friday in python


def datetime_converter(date):
    if isinstance(date, datetime.datetime):
        return date.__str__()


def get_next_day(timedelta, DAY):
    day = datetime.date.today()
    while day.weekday() != int(DAY):
        day += datetime.timedelta(1)  # add a day once you reach correct one
    time = (datetime.datetime.min + timedelta).time()
    return datetime.datetime.combine(day, time)


#functions that convert a datetime type in a dictionnay into a string to be returnable in json
def convert_and_trim(list_dict):
    for i in range(len(list_dict)):
        dict_to_change = list_dict[i]
        schedule = []
        for key in DAYS:
            if dict_to_change[key] is not None:  # Add the time to schedule
                schedule.append(
                    datetime_converter(get_next_day(dict_to_change[key], key)))
            dict_to_change.pop(key)  # remove days form dict
        dict_to_change['schedule'] = schedule  # Add whole schedule as a list


class ScheduleAll(Resource):
    def __init__(self):
        self.sql = SQLConn()

    def get(self):
        SELECT_ALL_SCHEDULE = "SELECT * FROM `schedule`"
        schedule_entries = self.sql.select_query(SELECT_ALL_SCHEDULE)
        convert_and_trim(
            schedule_entries)  #cast date type to str for json and remove None
        
        #group schedule by manager id
        managers_schedule_dict = {}
        schedule_entries.sort(key=lambda x: x['bm_id'])
        for bm_id, g in groupby(schedule_entries, lambda x: x['bm_id']):
            managers_schedule_dict[bm_id] = list(g)

        return managers_schedule_dict

class Schedule(Resource):
    def __init__(self):
        self.sql = SQLConn()

    def get(self, bm_id):
        SELECT_SCHEDULE = "SELECT * FROM `schedule` WHERE `bm_id`={bm_id}".format(
            bm_id=bm_id)
        schedule_of_manager = self.sql.select_query(SELECT_SCHEDULE)
        convert_and_trim(schedule_of_manager
                         )  #cast date type to str for json and remove None
        return schedule_of_manager
