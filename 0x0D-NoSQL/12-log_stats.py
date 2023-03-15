#!/usr/bin/env python3
"""Provides stats from nginx db"""
from pymongo import MongoClient
list_all = __import__('8-all').list_all


client = MongoClient('mongodb://127.0.0.1:27017')
school = client.logs.nginx
print(f"{school.count_documents({})} logs")
print("Methods:")
print(f"\tmethod GET: {school.count_documents({'method': 'GET'})}")
print(f"\tmethod POST: {school.count_documents({'method': 'POST'})}")
print(f"\tmethod PUT: {school.count_documents({'method': 'PUT'})}")
print(f"\tmethod PATCH: {school.count_documents({'method': 'PATCH'})}")
print(f"\tmethod DELETE: {school.count_documents({'method': 'DELETE'})}")
print(f"{school.count_documents({'path': '/status'})} status check")
