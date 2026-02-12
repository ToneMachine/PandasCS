from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import sqlite3
import os

# Paths for database
CSV_FILE = "pandasCSSkins/files/listing.csv"
DB_FILE = "pandasCSSkins/db_files/listing.db"
TABLE_NAME = "listing"

URL = "https://cs2skins.gg/items"
item_id = 0

# creates listing.csv file to scrap info from url
with open("pandasCSSkins/files/listing.csv", "w", newline = "", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Name"])

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
                price_tag = item.find("span", class_="skin-price").text.lstrip("$")
            except AttributeError:
                price_tag = None

            writer.writerow([item_id, name_tag])# writes to listing file
            item_id += 1

# Check CSV exists
if not os.path.exists(CSV_FILE):
    raise FileNotFoundError(f"{CSV_FILE} not found")

# Load CSV
df = pd.read_csv(CSV_FILE)

# Connect to SQLite (creates DB if it doesn't exist)
conn = sqlite3.connect(DB_FILE)

# Write to database
df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)

# Close connection
conn.close()

print("✅ CSV successfully converted to SQLite database")
print(f"📁 Database file: {DB_FILE}")
print(f"📊 Table name: {TABLE_NAME}")