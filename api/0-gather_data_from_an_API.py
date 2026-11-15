#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        emp_id = sys.argv[1]
        user_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
        todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(emp_id)
        
        user_res = requests.get(user_url).json()
        todos_res = requests.get(todos_url).json()
        
        name = user_res.get("name")
        total_tasks = len(todos_res)
        done_tasks = [t for t in todos_res if t.get("completed")]
        number_of_done = len(done_tasks)
        
        print("Employee {} is done with tasks({}/{}):".format(name, number_of_done, total_tasks))
        for task in done_tasks:
            print("\t {}".format(task.get("title")))
