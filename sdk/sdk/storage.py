from abc import ABCMeta, abstractmethod

import os

import redis


class Storage(metaclass=ABCMeta):
    @abstractmethod
    def get(self, key):
        """
        :param key: unique identifier of entry
        :type key: basestring
        :return: resolved entry value or None if no association was found
        """
        pass

    @abstractmethod
    def set(self, key, value):
        """
        :param key: unique identifier of entry
        :type key: basestring
        :param value: value of entry
        :type value: basestring
        """
        pass


class RedisStorage(Storage):
    def get(self, key):
        connection = self._get_redis_connection()
        return connection.get(key)

    def set(self, key, value):
        connection = self._get_redis_connection()
        connection.set(key, value)

    @staticmethod
    def _get_redis_connection():
        host, port = os.getenv("REDIS_SERVICE_HOST"), os.getenv("REDIS_SERVICE_PORT")
        if not host or not port:
            raise Exception('REDIS_SERVICE_HOST or REDIS_SERVICE_PORT not set')

        return redis.StrictRedis(host=host, port=int(port), db=0)


def create_storage():
    return RedisStorage()
