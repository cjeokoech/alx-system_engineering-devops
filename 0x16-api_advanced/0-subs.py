#!/usr/bin/python3
"""
import requests module
"""

from requests import get


def number_of_subscribers(subreddit):
    """ 
    function that queries the Reddit API 
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user_agent = {'User-agent': 'Google Chrome Version 125.0.6422.76'}

    if subreddit is None or not isinstance(subreddit, str):
        return 0
    response = get(url, headers=user_agent)
    all_data = response.json
    
    try:
        return all_data.get('data').get('subcribers')

    except:
        return 0
