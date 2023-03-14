#!/usr/bin/env python3
"""List all documents inside a collection"""


def list_all(mongo_collection):
    """Function to list all documents inside a collection"""
    collection_list = []

    for data in mongo_collection.find():
        if data:
            collection_list.append(data)
    return collection_list
