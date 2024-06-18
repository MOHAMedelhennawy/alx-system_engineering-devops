#!/usr/bin/python3
"""Module for task 0"""

def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit.
    """
    import requests
    headers = {'User-Agent': "My-User-Agent"}

    res = requests.get('https://oauth.reddit.com/r/{}/hot.json?limit=10 '.format(subreddit),
                       headers=headers)

    if res.status_code != 200:
        print('None')
    else:
        for post in res.json()['data']['children']:
            print(post['data']['title'])
