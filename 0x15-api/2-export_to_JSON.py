#!/usr/bin/python3
"""extend your Python script to export data in the JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    Uid = sys.argv[1]
    api = "https://jsonplaceholder.typicode.com/"
    usr = requests.get(api + "users/{}".format(Uid)).json()
    username = usr.get("username")
    TD = requests.get(api + "todos", params={"userId": Uid}).json()

    with open("{}.json".format(Uid), "w") as jsonfile:
        json.dump({Uid: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in TD]}, jsonfile)
