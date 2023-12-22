#!/usr/bin/env python3
"""
function that returns list of schools having a specific topic
"""

def schools_by_topic(mongo_collection, topic):
    """
    function that returns list of schools having a specific topic
    """
    return mongo_collection.find({"topics": topic})
