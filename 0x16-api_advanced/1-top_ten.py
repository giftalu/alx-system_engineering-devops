#!/usr/bin/python3
"""Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit."""

import requests

def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit."""
    
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful
        if response.status_code == 200:
            json_data = response.json().get('data', {})
            children = json_data.get('children', [])

            if len(children) == 0:
                print("None")
                return
            
            # Print up to 10 titles
            for i, child in enumerate(children[:10]):
                title = child.get('data', {}).get('title', "None")
                print(title)
        
        else:
            # Non-200 response, print None
            print("None")
    
    except requests.RequestException as e:
        # Catch network-related errors
        print(f"Network error: {e}")
        print("None")
    
    except Exception as e:
        # Catch all other exceptions
        print(f"Error: {e}")
        print("None")
