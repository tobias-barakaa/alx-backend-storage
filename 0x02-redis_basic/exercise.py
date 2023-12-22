#!/usr/bin/env python3
"""
Main file
"""
import redis
import uuid
from typing import Callable, Optional, Union

class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Get the value of the key and apply the conversion function if it exists.

        :param key: The key to get the value of.
        :param fn: The function to convert the value with.
        :return: The value of the key.
        """
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        Get the value of the key and convert it to a string.

        :param key: The key to get the value of.
        :return: The value of the key, converted to a string.
        """
        return self.get(key, fn=str)

    def get_int(self, key: str) -> int:
        """
        Get the value of the key and convert it to an integer.

        :param key: The key to get the value of.
        :return: The value of the key, converted to an integer.
        """
        return self.get(key, fn=int)
