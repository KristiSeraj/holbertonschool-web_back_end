#!/usr/bin/env python3
"""search module"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specific topic:"""
    result = mongo_collection.find({'topics': {'$in': [topic]}})
    return result
