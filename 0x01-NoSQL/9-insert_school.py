#!/usr/bin/env python3
"""
insert in school based on kwargs
"""

def insert_school(mongo_collection, **kwargs):
    """
    insert in school based on kwargs
    """
    return mongo_collection.insert_one(kwargs).inserted_id
