#!/usr/bin/python3
"""Second script that uses Reddit API"""
import json
import requests


def top_ten(subreddit):
    """A function to do stuff that can be done using other functions"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    user_agent = "0x16-api_advanced/1.0 by AMR856"
    headers = {"User-Agent": user_agent}
    params = {"limit": 10}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    my_object = requests.get(url, params=params, headers=headers, allow_redirects=False)
    if my_object.status_code == 404:
        print("None")
        return
    else:
        my_dict = my_object.json()
        for reddit in my_dict['data']['children']:
            print(reddit['data']['title'])


"https://www.reddit.com/r/programming/hot.json/?limit=10"
