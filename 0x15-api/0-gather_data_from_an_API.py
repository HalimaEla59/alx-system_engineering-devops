#!/usr/bin/python3
"""returns information about TODO list progress for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        APIurl = "https://jsonplaceholder.typicode.com/"
        user = requests.get(APIurl + "users/{}".format(sys.argv[1])).json()
        ToDo = requests.get(APIurl + "ToDo", params={"userId": sys.argv[1]}).json()
        completedToDo = [t.get("title") for t in ToDo if t.get("completedToDo") is True]

        print("Employee {} is done with tasks({}/{}):".format(
            user.get("name"), len(completedToDo), len(ToDo)))
        [print("\t {}".format(i)) for i in completedToDo]
