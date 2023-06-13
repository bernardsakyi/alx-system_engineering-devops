#!/usr/bin/python3
"""Count all matching keywords in hot posts from a subreddit with reddit API"""
import requests


def count_words(subreddit, word_list, after=None, session=None,
                count_dict=None):
    """Count all matching keywords in hot posts from a subreddit"""
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    if after is not None:
        url += '?after=' + after
    if count_dict is None:
        count_dict = {}
        for word in word_list:
            count_dict[word] = 0
    if (session is None):
        session = requests.Session()
        headers = {
            'User-Agent': 'My User Agent 1.0'
        }
        session.headers.update(headers)
    response = session.get(url, allow_redirects=False)
    if (response.ok is False or response.status_code == 302):
        return
    after = response.json().get('data').get('after')
    top_posts = response.json().get('data').get('children')
    for post in top_posts:
        title = post.get('data').get('title')
        for keyword in word_list:
            for word in title.casefold().split():
                if keyword.casefold() == word:
                    count_dict[keyword] += 1
    if (after is None):
        dupeless_dict = {}
        for key, value in count_dict.items():
            if value != 0:
                key = key.casefold()
                try:
                    dupeless_dict[key] = dupeless_dict.get(key) + value
                except TypeError as e:
                    dupeless_dict[key] = value
        sorted_dict = {val[0]: val[1]
                       for val in sorted(dupeless_dict.items(),
                                         key=lambda x: (-x[1], x[0]))}
        for key, value in sorted_dict.items():
            if (value > 0):
                print('{}: {}'.format(key, value))
        return
    count_words(subreddit, word_list, after, session, count_dict)
