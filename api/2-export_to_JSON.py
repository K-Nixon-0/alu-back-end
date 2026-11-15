#!/usr/bin/python3
"""Export data to JSON format"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        emp_id = sys.argv[1]
        user_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
        todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(emp_id)
        
        user_res = requests.get(user_url).json()
        todos_res = requests.get(todos_url).json()
        
        username = user_res.get("username")
        
        task_list = []
        for task in todos_res:
            task_dict = {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            task_list.append(task_dict)
            
        out_dict = {str(emp_id): task_list}
        
        filename = "{}.json".format(emp_id)
        with open(filename, mode="w") as f:
            json.dump(out_dict, f)
