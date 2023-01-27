#!/usr/bin/env python3
"""Caching system"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Inherits from BaseCaching class"""
    def put(self, key, item):
        """Assign to the dictionary cache_data the item for value key"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve the value of key found in cache_data dictionary"""
        if key and self.cache_data.get(key):
            return self.cache_data.get(key)
        return None
