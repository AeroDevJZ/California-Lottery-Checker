import requests
from bs4 import BeautifulSoup

url = "https://www.calottery.com/en/draw-games/superlotto-plus#section-content-2-3"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 11.0; Win64; x64)"
}
response = requests.get(url, headers=headers)
html = response.text

# Parsing the scraped data
soup = BeautifulSoup(html, "html.parser")

number = soup.find_all("div", class_="sr-only")

print(number)

# doesn't work
