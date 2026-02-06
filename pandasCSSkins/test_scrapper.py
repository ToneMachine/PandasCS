from bs4 import BeautifulSoup
import requests
import csv

URL = "https://cs2skins.gg/items/skin/rifles/ak-47/jet-set"

with open("pandasCSSkins/test.csv", "w", newline = "", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["category", "weapon", "pattern", "rarity", "stat trak", "souvenir", "team", "collection"])

    # get request
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    item = soup.find("div", class_="skin-properties mt-6")

    # data value
    property_list = item.find_all("div", class_="attribute-row")

    rarity = item.find("a", class_="attribute-link").text
    weapon_category = property_list[0].text.replace("Name","")
    style_description = property_list[1].text
    weapon_Name = property_list[2].text.replace("Name","")
    sticker_slots = property_list[3].text
    pattern_Name = property_list[4].text.replace("Name","")
    float_range = property_list[5].text
    is_stattrak = property_list[6].text.strip("StatTrak Available o es")
    is_souvenir = property_list[7].text.strip("Souvenir Available es")
    team = property_list[9].text.replace("NameCounter-Terrorist", "CT").replace("NameTerrorist", "T").replace("NameBoth Teams", "Both")
    collection = item.find("div", class_="collection-info").text

    # writes to csv file
    writer.writerow([weapon_category, weapon_Name, pattern_Name, rarity, is_stattrak, is_souvenir, team, collection])