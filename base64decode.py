# -*- coding: utf-8 -*-
"""
Created on thurs Jan 4 19:01:12 2024

@author: david
"""

# Import requests library
import requests

# Define the base URL for bard.google.com
base_url = "https://bard.google.com/"

# Define the query parameters for the top Cybersecurity stories
params = {
    "q": "Cybersecurity",
    "sort": "date",
    "order": "desc",
    "limit": 10
}

# Send a GET request to the base URL with the query parameters
response = requests.get(base_url, params=params)

# Check if the response status code is 200 (OK)
if response.status_code == 200:
    # Parse the response as JSON
    data = response.json()
    # Print the titles and URLs of the stories
    for story in data["results"]:
        print(story["title"])
        print(story["url"])
        print()
else:
    # Print an error message
    print("Something went wrong. Please try again later.")

