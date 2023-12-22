#!/usr/bin/env python3
"""
Retrieve the HTML of the provided URL.
"""
import requests
import redis
from functools import wraps
from typing import Callable


# Initialize Redis client
redis_client = redis.Redis()

def count_access(url: str) -> None:
    """
    Increment the access count for a given URL.

    :param url: The URL to track.
    """
    count_key = f"count:{url}"
    redis_client.incr(count_key)

def cache_result(url: str, result: str, expiration: int = 10) -> None:
    """
    Cache the result for a given URL with a specified expiration time.

    :param url: The URL to cache the result for.
    :param result: The result (HTML content) to cache.
    :param expiration: The expiration time for the cache in seconds.
    """
    cache_key = f"cache:{url}"
    redis_client.setex(cache_key, expiration, result)

def get_cached_result(url: str) -> str:
    """
    Retrieve the cached result for a given URL.

    :param url: The URL to retrieve the cached result for.
    :return: The cached result (HTML content).
    """
    cache_key = f"cache:{url}"
    return redis_client.get(cache_key)

def get_page(url: str) -> str:
    """
    Fetch the HTML content of a URL and cache the result with a 10-second expiration time.

    :param url: The URL to fetch the HTML content from.
    :return: The HTML content.
    """
    # Check if the result is already cached
    cached_result = get_cached_result(url)
    if cached_result is not None:
        return cached_result.decode("utf-8")

    # Fetch the HTML content using requests
    response = requests.get(url)
    html_content = response.text

    # Cache the result and count the access
    cache_result(url, html_content)
    count_access(url)

    return html_content

# Bonus: Implement a decorator for caching
def cache_decorator(expiration: int = 10) -> Callable:
    """
    Decorator to cache the result of a function with a specified expiration time.

    :param expiration: The expiration time for the cache in seconds.
    :return: Decorated function.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Use the first argument as the URL
            url = args[0]
            
            # Check if the result is already cached
            cached_result = get_cached_result(url)
            if cached_result is not None:
                return cached_result.decode("utf-8")

            # Call the original function
            result = func(*args, **kwargs)

            # Cache the result and count the access
            cache_result(url, result, expiration)
            count_access(url)

            return result
        return wrapper
    return decorator
