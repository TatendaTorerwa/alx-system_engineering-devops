#!/usr/bin/python3
"""function that queries the Reddit API and
returns the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Linux:0x16.api.advanced:v1.1 (by /u/Tatenda)'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 400:
        return 0
    final_data = response.json().get("data")
    return final_data.get("subscribers")
