#!/usr/bin/python3
"""Dictionary of list of dictionaries export to JSON"""
import json
import requests

if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    
    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()
    
    all_data = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        user_tasks = [t for t in todos if t.get("userId") == user_id]
        
        task_list = []
        for task in user_tasks:
            task_dict = {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            task_list.append(task_dict)
            
        all_data[str(user_id)] = task_list
        
    with open("todo_all_employees.json", mode="w") as f:
        json.dump(all_data, f)
