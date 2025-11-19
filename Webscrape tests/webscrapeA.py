# This is for finding a Json file that has the winning numbers in it that the website gets the data from b/c it loads the data in via javascript and doesn't use the HTML
import requests

# after inspecting go to network, reload site, sort for XHR/Fetch, and click each of the names to get request url's
url = "https://www.calottery.com/api/DrawGameApi/DrawGamePastDrawResults/8/1/20"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
response = requests.get(url, headers=headers)

# Parses the Json file into python syntax
data = response.json()

print(data["DrawResults"][0])
