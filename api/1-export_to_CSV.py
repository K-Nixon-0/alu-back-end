#!/usr/bin/python3
"""Export data to CSV format"""
import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        emp_id = sys.argv[1]
        user_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
        todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(emp_id)
        
        user_res = requests.get(user_url).json()
        todos_res = requests.get(todos_url).json()
        
        user_id = user_res.get("id")
        username = user_res.get("username")
        
        filename = "{}.csv".format(emp_id)
        with open(filename, mode="w", newline="") as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            for task in todos_res:
                writer.writerow([str(user_id), username, str(task.get("completed")), task.get("title")])
