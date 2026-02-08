import sqlite3
import csv

file_name = "skin_table"

# 1. Create / open the database
conn = sqlite3.connect(f"pandasCSSkins/{file_name}.db")
cursor = conn.cursor()

# 2. Create table (match your CSV columns)
cursor.execute("""
CREATE TABLE IF NOT EXISTS listings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price TEXT
)
""")

# 3. Open CSV and insert rows
with open(f"pandasCSSkins/{file_name}.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    
    next(reader)  # skip header if you have one

    for row in reader:
        cursor.execute(
            "INSERT INTO listings (name, price) VALUES (?, ?)",
            (row[0], row[1])
        )

# 4. Save and close
conn.commit()
conn.close()

print("CSV imported into skins.db")
