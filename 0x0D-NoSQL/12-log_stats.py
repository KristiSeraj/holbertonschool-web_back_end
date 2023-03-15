#!/usr/bin/env python3
"""Provides stats from nginx db"""
from pymongo import MongoClient


def count(elements):
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    return collection.count_documents(elements)


def main():
    print(f"{count({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {count({'method': 'GET'})}")
    print(f"\tmethod POST: {count({'method': 'POST'})}")
    print(f"\tmethod PUT: {count({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {count({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {count({'method': 'DELETE'})}")
    print(f"{count({'path': '/status'})} status check")


if __name__ == "__main__":
    main()
