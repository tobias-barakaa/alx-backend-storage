#!/usr/bin/env python3
"""
Main file
"""
import redis
import uuid
from typing import Union, Callable


class Cache:
    def __init__(self):
        """
        Initialize the Cache class with a Redis client instance and flush the database.
        """
        # Create an instance of the Redis client and flush the database
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis using a randomly generated key.

        :param data: The data to be stored, can be str, bytes, int, or float.
        :return: The randomly generated key used for storing the data.
        """
        # Generate a random key using uuid
        key = str(uuid.uuid4())
        
        # Store the input data in Redis using the random key
        if isinstance(data, (str, bytes, int, float)):
            self._redis.set(key, data)
        else:
            raise ValueError("Invalid data type. Supported types are str, bytes, int, or float.")

        # Return the generated key
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
