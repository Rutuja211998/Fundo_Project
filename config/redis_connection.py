"""
This file having redis class which contains redis functions for different methods.
Author: Rutuja Tikhile.
Date:3/3/2020
"""
import os
import redis
import logging
logging.basicConfig(level=logging.DEBUG)
from config.singleton import singleton
from dotenv import load_dotenv
load_dotenv()


@singleton
class RedisCon:
    """
    This class is used to form connection and execute query related to redis cache
    """
    def __init__(self, **kwargs):
        self.connection = self.connect(**kwargs)

    def connect(self, **kwargs):
        connection = redis.StrictRedis(host=kwargs['host'],
                                 port=kwargs['port'],
                                 db=kwargs['db'])

        if connection:
            logging.info('Redis Cache Connection established')
        return connection

    def set(self, key, value, exp_s=None, exp_ms=None):
        self.connection.set(key, value, exp_s, exp_ms)
        logging.info(f'{key} : {value}')

    def get(self, key):
        return self.connection.get(key)

    def exists(self, key):
        return self.connection.exists(key)

    def delete(self, key):
        logging.info(f'Key to Delete : {key}')
        self.connection.delete(key)

    def disconnect(self):
        self.connection.close()


con = RedisCon(host=os.getenv('redis_host'),
               port = os.getenv('redis_port'),
               db = os.getenv('redis_db'))
