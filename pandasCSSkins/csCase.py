# use python 3.10
from bs4 import BeautifulSoup
import requests

url = "https://steamcommunity.com/market/search?appid=730#p1_name_asc"

result = requests.get(url)

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(result.text, 'html.parser')

# Find all the items
items = soup.find_all('a', class_ = "market_listing_row_link")

# Print item name and price on the same line
for item in items:
    item_name = item.find('span', class_="market_listing_item_name").text
    item_price = item.find('span', class_="normal_price").text
    strip_item_price = item_price.strip()
    print(f"{item_name}:\n{strip_item_price}")