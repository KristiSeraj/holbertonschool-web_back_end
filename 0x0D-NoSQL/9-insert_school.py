#!/usr/bin/env python3
"""insertion module"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on kwargs"""
    kwargs_el = {}
    for k, v in kwargs.items():
        kwargs_el[k] = v
    doc_id = mongo_collection.insert_one(kwargs_el).inserted_id
    return doc_id
