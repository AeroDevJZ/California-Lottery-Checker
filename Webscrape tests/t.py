from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import re

# === CONFIGURE PATHS ===
# update if different
BRAVE_PATH = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
# update to where chromedriver.exe is
CHROMEDRIVER_PATH = "C:/path/to/chromedriver.exe"

# === SETUP BRAVE OPTIONS ===
chrome_options = Options()
chrome_options.binary_location = BRAVE_PATH
chrome_options.add_argument("--headless")  # optional: run without UI
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# === START DRIVER ===
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Open SuperLotto Plus results page
    driver.get("https://www.calottery.com/en/draw-games/superlotto-plus")

    # Find the div that contains "Winning numbers"
    div = driver.find_element(
        "xpath", '//div[contains(text(), "Winning numbers")]')
    text = div.text
    print("Raw text:", text)

    # Extract numbers using regex
    numbers = re.findall(r'\d+', text)
    # all except last are normal numbers
    print("Winning numbers:", numbers[:-1])
    print("Mega number:", numbers[-1])       # last number is Mega

finally:
    driver.quit()
