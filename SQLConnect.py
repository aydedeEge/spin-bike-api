import json
import pymysql.cursors
import os

from read_config import read_config

class SQLConn:

    def __init__(self):
        read_config()
        self.config = {
            "host": os.environ["HOST"],
            "user": os.environ["USER"],
            "password": os.environ["PASSWORD"],
            "port": os.environ["PORT"],
            "db": os.environ["DB"],
        }

    def connect(self):
        connection = pymysql.connect(
            host=self.config["host"],
            user=self.config["user"],
            password=self.config["password"],
            db=self.config["db"],
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )

        return connection

    def select_query(self, select_query):
        connection = self.connect()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `spin_bikes` LIMIT 5"
                cursor.execute(select_query)
                result = cursor.fetchall()
            connection.commit()

        finally:
            connection.close()

        return result

#This an example of a Select query using PyMySQL
    # def test_query(self):
    #     connection = self.connect()
    #     try:
    #         with connection.cursor() as cursor:
    #             sql = "SELECT * FROM `spin_bikes` LIMIT 5"
    #             cursor.execute(sql)
    #             result = cursor.fetchall()
    #         connection.commit()

    #     finally:
    #         connection.close()

    #     return result
