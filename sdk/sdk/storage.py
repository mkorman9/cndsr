from abc import ABCMeta, abstractmethod

import os
from typing import Optional

import redis

from sdk.url import URL


class Storage(metaclass=ABCMeta):
    @abstractmethod
    def get(self, key: str) -> Optional['URL']:
        """
        :param key: unique identifier of entry
        :return: resolved entry value or None if no association was found
        """
        pass

    @abstractmethod
    def set(self, key: str, url: 'URL') -> bool:
        """
        :param key: unique identifier of entry
        :param url: value to store
        :return: whether the set was successful
        """
        pass


class RedisStorage(Storage):
    def get(self, key: str) -> Optional['URL']:
        connection = self._get_redis_connection()
        entry = connection.get(key.lower())
        return URL(entry) if entry else None

    def set(self, key: str, url: 'URL') -> bool:
        connection = self._get_redis_connection()
        return connection.setnx(key.lower(), url.address) == 1

    @staticmethod
    def _get_redis_connection():
        host, port = os.getenv("REDIS_SERVICE_HOST"), os.getenv("REDIS_SERVICE_PORT")
        if not host or not port:
            raise Exception('REDIS_SERVICE_HOST or REDIS_SERVICE_PORT not set')

        return redis.StrictRedis(host=host, port=int(port), db=0)


def create_storage():
    return RedisStorage()
