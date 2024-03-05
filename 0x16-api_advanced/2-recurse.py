#!/usr/bin/python3
"""Third script that uses Reddit API"""
import json
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """A code that can do stuff"""
    if subreddit is None or type(subreddit) is not str:
        return None
    user_agent = "0x16-api_advanced/1.0 by AMR856"
    params = {"limit": 50, "after": after, "count": count}
    headers = {"User-Agent": user_agent}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    my_json_object = requests.get(url, params=params,
                                  headers=headers, allow_redirects=False)
    if my_json_object.status_code == 404:
        return None
    else:
        my_object_after_parsing = json.loads(my_json_object.text)
        after = my_object_after_parsing['data']['after']
        count = count + int(my_object_after_parsing['data']['dist'])
        for reddit in my_object_after_parsing['data']['children']:
            hot_list.append(reddit['data']['title'])
        if after is not None:
            recurse(subreddit, hot_list, after, count)
        return hot_list
