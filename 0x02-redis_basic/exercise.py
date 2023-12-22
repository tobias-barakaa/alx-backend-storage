#!/usr/bin/env python3
"""
Main file
"""
from functools import wraps
import redis
import uuid
from typing import Union, Callable


class Cache:
    def __init__(self):
        """
        Initialize the Cache class with a Redis client instance and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @staticmethod
    def count_calls(method):
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            key = f"calls:{method.__qualname__}"  # Using the method's qualified name as the key
            self._redis.incr(key)  # Increment the count for this method
            return method(self, *args, **kwargs)  # Execute the original method
        return wrapper

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis using a randomly generated key.

        :param data: The data to be stored, can be str, bytes, int, or float.
        :return: The randomly generated key used for storing the data.
        """
        key = str(uuid.uuid4())
        
        if isinstance(data, (str, bytes, int, float)):
            self._redis.set(key, data)
        else:
            raise ValueError("Invalid data type. Supported types are str, bytes, int, or float.")

        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, None]:
        """
        Retrieve data from Redis using the provided key and optionally apply a conversion function.

        :param key: The key used to retrieve data from Redis.
        :param fn: Optional conversion function to apply on the retrieved data.
        :return: The retrieved data, optionally converted using the provided function.
        """
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """
        Retrieve a string from Redis using the provided key.

        :param key: The key used to retrieve data from Redis.
        :return: The retrieved string or None if the key does not exist.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """
        Retrieve an integer from Redis using the provided key.

        :param key: The key used to retrieve data from Redis.
        :return: The retrieved integer or None if the key does not exist.
        """
        return self.get(key, fn=int)
