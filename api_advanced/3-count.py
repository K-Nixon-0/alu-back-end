#!/usr/bin/python3
"""Module to count keywords in hot articles"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Recursive function to count keywords in hot posts titles"""
    if counts is None:
        counts = {}
        word_list = [w.lower() for w in word_list]

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'custom-user-agent'}
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        if not counts and after is None:
            return
        if after is None:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                if count > 0:
                    print("{}: {}".format(word, count))
        return

    data = response.json().get("data", {})
    after = data.get("after")
    children = data.get("children", [])

    for child in children:
        title = child.get("data", {}).get("title").lower()
        words = title.split()
        for w in words:
            clean_w = ''.join(c for c in w if c.isalnum() or c == '_')
            for word in word_list:
                if clean_w == word:
                    counts[word] = counts.get(word, 0) + 1

    if after is not None:
        return count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count > 0:
                print("{}: {}".format(word, count))
