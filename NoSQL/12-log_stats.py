#!/usr/bin/env python3
"""Module for logging stats"""
from pymongo import MongoClient

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

def log_method_stats(mongo_collection, method):
    """Log statistics for a specific HTTP method"""
    value = mongo_collection.count_documents({"method": method})
    print(f"\tmethod {method}: {value}")

def log_stats(mongo_collection):
    """Function to get nginx stats from mongodb"""
    # Count and print total number of logs
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")

    # Log statistics for each HTTP method
    print("Methods:")
    for method in METHODS:
        log_method_stats(mongo_collection, method)

    # Log status check count
    status_check = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check} status check")

if __name__ == "__main__":
    # Connect to MongoDB and select the nginx collection
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Log the stats
    log_stats(nginx_collection)
