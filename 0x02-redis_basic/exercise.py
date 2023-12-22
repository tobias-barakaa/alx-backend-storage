#!/usr/bin/env python3
"""
Main file
"""
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis using a random key.

        :param data: The data to be stored.
        :return: The key used to store the data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
