#!/usr/bin/python3
"""Module to recursively query hot articles"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list containing the titles of all hot articles for a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'custom-user-agent'}
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        return None if not hot_list else hot_list
    data = response.json().get("data", {})
    after = data.get("after")
    children = data.get("children", [])
    for child in children:
        hot_list.append(child.get("data", {}).get("title"))
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
