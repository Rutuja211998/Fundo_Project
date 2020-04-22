"""
This file containing Mysql connect class which calls database query.
Author: Rutuja Tikhile.
Data:4/3/2020
"""
import mysql.connector
import os
from config.singleton import singleton
from dotenv import load_dotenv
load_dotenv()


@singleton
class MysqlConnect:
    """
    This class is used to form a database connection
    """
    def __init__(self, **kwargs):
        self.conn = self.connect(**kwargs)
        self.mycursor = self.conn.cursor()

    def connect(self, **kwargs):
        mydb = mysql.connector.connect(
            host=kwargs["host"],
            user=kwargs["user"],
            passwd=kwargs["passwd"],
            database=kwargs["database"],
        )
        return mydb

    def run_query(self, query, value=None):
        self.mycursor.execute(query, value)
        return self.mycursor.fetchall()

    def query_execute(self, query,value=None):
        self.mycursor.execute(query,value)
        self.conn.commit()

    def disconnect(self):
        self.conn.close()


con = MysqlConnect(host=os.getenv('mysql_host'),
                 user=os.getenv('mysql_user'),
                 passwd=os.getenv('mysql_passwd'),
                 database=os.getenv('mysql_database'))
