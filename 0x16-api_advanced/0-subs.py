#!/usr/bin/python3
"""First script that uses Reddit API"""
import json
import requests


def number_of_subscribers(subreddit):
    """A function to do stuff that can be done using other functions"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    user_agent = "0x16-api_advanced/1.0 by AMR856"
    headers = {"User-Agent": user_agent}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    my_json_object = requests.get(url, headers=headers, allow_redirects=False)
    if my_json_object.status_code == 200:
        my_dict = json.loads(my_json_object.text)
        return my_dict['data']['subscribers']
    else:
        return 0
