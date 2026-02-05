from bs4 import BeautifulSoup
import requests
import csv

URL = "https://cs2skins.gg/items/skin/heavy/m249/shipping-forecast"

with open("pandasCSSkins/test.csv", "w", newline = "", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["rarity", "stattrak", "souvenir", "team", "collection"])

    # get request
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    item = soup.find("div", class_="skin-properties mt-6")

    # data value
    property_list = item.find_all("div", class_="attribute-row")
    rarity = item.find("a", class_="attribute-link").text
    weapon_category = property_list[0].text
    style_description = property_list[1].text
    weapon_Name = property_list[2].text
    sticker_slots = property_list[3].text
    pattern_name = property_list[4].text
    float_range = property_list[5].text
    is_stattrak = property_list[6].text.strip("StatTrak Available o")
    is_souvenir = property_list[7].text.strip("Souvenir Available")
    team = property_list[9].text.strip("Name errorist")
    collection = item.find("div", class_="collection-info").text

    # writes to csv file
    writer.writerow([rarity, is_stattrak, is_souvenir, team, collection])