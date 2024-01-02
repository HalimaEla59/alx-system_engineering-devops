#!/usr/bin/python3
"""extend your Python script to export data in the CSV format"""
import csv
import requests
import sys

if __name__ == "__main__":
    Uid = sys.argv[1]
    api = "https://jsonplaceholder.typicode.com/"
    usr = requests.get(api + "users/{}".format(Uid)).json()
    username = usr.get("username")
    TD = requests.get(api + "todos", params={"userId": Uid}).json()

    with open("{}.csv".format(Uid), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [Uid, username, t.get("completed"), t.get("title")]
         ) for t in TD]
