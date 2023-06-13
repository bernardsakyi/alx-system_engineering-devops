#!/usr/bin/python3
"""Get number of subscribers from a subreddit using reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Get number of subscribers from a subreddit"""
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    session = requests.Session()
    headers = {
        'User-Agent': 'My User Agent 1.0'
    }
    session.headers.update(headers)
    response = session.get(url, allow_redirects=False)
    if (response.ok is False):
        return (0)
    return (response.json().get('data').get('subscribers'))
