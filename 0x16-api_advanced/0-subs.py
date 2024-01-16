#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers for a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """If an invalid subreddit is given, the function should return 0"""
    link = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(link, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
