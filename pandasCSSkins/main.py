from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import sqlite3
import os
import time

# opens csv file
with open("pandasCSSkins/files/listing.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) < 2:
            continue
        # creates weapon and weapon pattern name var
        name = row[1].lower().split('|')
        weapon = name[0].rstrip().replace(" ","-")
        pattern = (
            name[1].lstrip().replace("ö","").replace("ā","")
            .replace("'","").replace("!","").replace(".","").replace("&","")
            .replace(" 壱","").replace("弐","2").replace("龍王 ","")
            .replace(" ","-").replace("---","-").replace("--","-").replace("♥","") 
            if len(name) > 1 else None
            )
        
        url = f'https://steamcommunity.com/market/search?appid=730&q={weapon}+{pattern}'
        print("Scrapping:" + url)


        result = requests.get(url)

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(result.text, 'html.parser')

        # finds value on page
        try:
            list_total = soup.find("span", id="searchResults_total").text# number of items on the page
        except:
            time.sleep(30)
        name = soup.find_all("div", class_="market_listing_item_name_block")
        quanity = soup.find_all("span", class_="market_listing_num_listings_qty")
        price = soup.find_all("span", class_="normal_price")

        # writes price to csv file
        with open("pandasCSSkins/files/steam_price.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "quanity", "price"])




            # scraps data
            for listing in range(0, int(list_total) * 2, 2):
                Name = name[int(listing/2)].text.replace("\n","").replace("Counter-Strike 2","")
                Quanity = quanity[int(listing/2)].text
                Price = price[listing].text.lstrip().replace("Starting at:", "").split()
                PRICE = float(Price[0].strip("$"))


                print(Name)

    



