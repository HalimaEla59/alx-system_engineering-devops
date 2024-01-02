#!/usr/bin/python3
"""returns information about TODO list progress for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        api = "https://jsonplaceholder.typicode.com/"
        user = requests.get(api + "users/{}".format(sys.argv[1])).json()
        TD = requests.get(api + "todos", params={"userId": sys.argv[1]}).json()
        done = [t.get("title") for t in TD if t.get("completed") is True]

        print("Employee {} is done with tasks({}/{}):".format(
            user.get("name"), len(done), len(TD)))
        [print("\t {}".format(i)) for i in done]
