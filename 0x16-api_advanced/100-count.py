#!/usr/bin/python3
"""Third script that uses Reddit API"""
import json
import requests

word_dict = {}


def count_words(subreddit, word_list, after=''):
    global word_dict

    if not word_dict:
        for word in word_list:
            if word.lower() not in word_dict:
                word_dict[word.lower()] = 0

    if after is None:
        """Here we print"""
        # sorted(my_dict.items(), key=lambda item: (item[1], item[0]))
        sorted_list_by_values = sorted(word_dict.items(),
                                       key=lambda item: (item[1], item[0]),
                                       reverse=True)
        sorted_dict_by_values = dict(sorted_list_by_values)
        for key, value in sorted_dict_by_values.items():
            if value != 0:
                print(f"{key}: {value}")
            else:
                pass
        return None

    if subreddit is None or type(subreddit) is not str:
        return None

    user_agent = "0x16-api_advanced/1.0 by AMR856"
    params = {"limit": 100, "after": after}
    headers = {"User-Agent": user_agent}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    my_json_object = requests.get(url, params=params,
                                  headers=headers, allow_redirects=False)
    if my_json_object.status_code == 404:
        return None
    else:
        my_object_after_parsing = json.loads(my_json_object.text)
        after = my_object_after_parsing['data']['after']
        the_title = ''
        for reddit in my_object_after_parsing['data']['children']:
            the_title = reddit['data']['title']
            the_list = the_title.split(' ')
            for i in range(len(the_list)):
                the_list[i] = the_list[i].lower()
            for key in word_dict.keys():
                word_dict[key] = word_dict[key] + the_list.count(key)
    count_words(subreddit, word_list, after)
