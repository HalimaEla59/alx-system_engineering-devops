#!/usr/bin/python3
"""extend your Python script to export data in the JSON format"""
import json
import requests

if __name__ == "__main__":
    api = "https://jsonplaceholder.typicode.com/"
    usr = requests.get(api + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(api + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in usr}, jsonfile)
