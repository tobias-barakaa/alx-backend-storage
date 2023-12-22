#!/usr/bin/env python3
"""
Script that provides stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


def log_stats(mongo_collection):
    """
    Display some stats about Nginx logs stored in MongoDB
    """
    total_logs = mongo_collection.count_documents({})

    print("{} logs".format(total_logs))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    status_check_count = mongo_collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print("{} status check".format(status_check_count))
