#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit"""
from requests import get
from sys import argv


def top_ten(subreddit):
    """If not a valid subreddit, print None"""
    header = {'User-Agent': 'Illustrious_Event_19'}
    try:
        counter = get('https://www.reddit.com/r/{}/hot.json?count=10'.format(
            subreddit), headers=header).json().get('data').get('children')
        print('\n'.join([dic.get('data').get('title')
                         for dic in counter][:10]))
    except:
        print('None')


if __name__ == "__main__":
    top_ten(argv[1])
