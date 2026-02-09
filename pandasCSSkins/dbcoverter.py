import pandas as pd
import sqlite3
import os

# Paths
CSV_FILE = "pandasCSSkins/files/listing.csv"
DB_FILE = "pandasCSSkins/db_files/listing.db"
TABLE_NAME = "listing"

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