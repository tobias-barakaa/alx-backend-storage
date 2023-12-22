#!/usr/bin/env python3
"""
Main file
"""

import redis
import uuid
from functools import wraps
from typing import Union, Callable


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def _increment_call_count(self, key):
        return self._redis.incr(key)

    def count_calls(method: Callable) -> Callable:
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            key = method.__qualname__
            self._increment_call_count(key)
            return method(self, *args, **kwargs)
        return wrapper

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, None]:
        value = self._redis.get(key)
        if value is None:
            return None
        
        if fn:
            return fn(value)
        
        return value
