#!/usr/bin/python3
"""Module for task 0"""

def number_of_subscribers(subreddit):
    import requests
    headers = {'User-Agent': "My-User-Agent"}

    res = requests.get(f'https://oauth.reddit.com/r/{subreddit}/about.json',
                       headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    else:
        return res.json()['data']['subscribers']