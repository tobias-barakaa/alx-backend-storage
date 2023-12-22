#!/usr/bin/env python3
"""
Main file
"""
import redis
import uuid
from typing import Union


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
