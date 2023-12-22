#!/usr/bin/env python3
"""
Retrieve the HTML of the provided URL.
"""
import requests


def get_page(url: str) -> str:
    """
    Retrieve the HTML of the provided URL.

    :param url: The URL to retrieve the HTML from.
    :return: The HTML of the provided URL.
    """
    response = requests.get(url)
    return response.text
