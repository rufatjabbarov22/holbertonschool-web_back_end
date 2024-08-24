#!/usr/bin/env python3
"""Script to display stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient

def main():
    """Main function to fetch and display stats from MongoDB"""
    # Connect to MongoDB
    client = MongoClient()
    db = client['logs']
    collection = db['nginx']
    
    # Total number of documents
    total_logs = collection.count_documents({})
    
    # Counts for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method}) for method in methods}
    
    # Count for GET method with path /status
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
    
    # Output results
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    main()
