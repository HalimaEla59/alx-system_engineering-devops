#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers for a given subreddit."""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """If an invalid subreddit is given, the function should return 0"""
    header = {'User-Agent': 'Illustrious_Event_19'}
    SubNum = get('https://www.reddit.com/r/{}/about.json'.format(
        subreddit), headers=header).json()
    try:
        return SubNum.get('data').get('subscribers')
    except:
        return 0

if __name__ == "__main__":
    number_of_subscribers(argv[1])
