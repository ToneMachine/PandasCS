from bs4 import BeautifulSoup
import requests

URL = "https://cs2skins.gg/items"

with open("listing-CS2Skinsgg.txt", "w", encoding="utf-8") as f:

    # loops pages
    for page in range(1, 76):
        params = {
            "perPage": 96,
            "sort": "name_asc",
            "page": page
        }

        # gets requests
        response = requests.get(URL, params=params)
        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.find_all("div", class_="skin-details")

        if not items:
            print(f"No items found on page {page}")
            break

        # loops items
        for item in items:
            # checks if item has name or value
            try:
                name_tag = item.find("h3", class_="skin-name").text
            except AttributeError:
                name_tag = None

            try:
                price_tag = item.find("span", class_="skin-price").text
            except AttributeError:
                price_tag = None

            # if not name_tag or not price_tag:
            #     continue

            #item_name = name_tag.text.strip()
            #item_price = price_tag.text.strip()

            f.write(f"{name_tag} {price_tag}\n")# writes to file