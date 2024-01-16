#!/usr/bin/python3
"""queries the Reddit API and returns a list containing the titles of all hot articles
for a given subreddit. If no results are found for the given subreddit,
the function should return None."""
from requests import get
from sys import argv


def recurse(subreddit, hotlist=[], after=None):
    """If not a valid subreddit, return None."""
    head = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by u/Illustrious_Event_19)"}
    try:
        if after:
            count = get('https://www.reddit.com/r/{}/hot.json?after={}'.format(
                subreddit, after), headers=head).json().get('data')
        else:
            count = get('https://www.reddit.com/r/{}/hot.json'.format(
                subreddit), headers=head).json().get('data')
        hotlist += [dic.get('data').get('title')
                    for dic in count.get('children')]
        if count.get('after'):
            return recurse(subreddit, hotlist, after=count.get('after'))
        return hotlist
    except:
        return None


if __name__ == "__main__":
    recurse(argv[1])
