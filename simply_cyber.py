import requests

# Get the URL of the Simply Cyber YouTube channel
url = "https://www.youtube.com/c/SimplyCyber"

# Get the response from the URL
response = requests.get(url)

# Check if the response is successful
if response.status_code == 200:

    # Get the JSON data from the response
    data = response.json()

    # Get the list of videos
    videos = data["items"]

    # Print the titles of the last ten videos
    for i in range(10):
        print(videos[i]["snippet"]["title"])

else:
    print("Error getting response from YouTube")