#!/usr/bin/env python3
# 8-all.py

def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection: pymongo collection object.

    Returns:
        A list containing all documents in the collection.
    """
    # Use find() to retrieve all documents in the collection
    documents = list(mongo_collection.find({}))

    return documents

