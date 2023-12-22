#!/usr/bin/env python3
"""
Retrieve the HTML of the provided URL.
"""
import requests
import redis
from functools import wraps
redis_client = redis.Redis()


def count_calls(func):
    """
    function
    """
    @wraps(func)
    def wrapper(url):
        # Increment the access count for the URL
        count_key = f"count:{url}"
        redis_client.incr(count_key)

        return func(url)
    return wrapper

def cache(expiration=10):
    def decorator(func):
        @wraps(func)
        def wrapper(url):
            # Try to get the cached result
            cache_key = f"cache:{url}"
            cached_result = redis_client.get(cache_key)

            if cached_result is not None:
                return cached_result.decode("utf-8")

            # Call the original function and cache the result
            result = func(url)
            redis_client.setex(cache_key, expiration, result)

            return result
        return decorator

@count_calls
@cache()
def get_page(url: str) -> str:
    """
    Fetch the HTML content of a URL and cache the result with a 10-second expiration time.

    :param url: The URL to fetch the HTML content from.
    :return: The HTML content.
    """
    response = requests.get(url)
    return response.text
