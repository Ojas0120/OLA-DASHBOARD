import pandas as pd
import sqlite3

# Load cleaned dataset
df = pd.read_csv("data/ola_cleaned.csv")

# Create SQLite database
conn = sqlite3.connect("ola.db")

# Create table
df.to_sql("ola_rides", conn, if_exists="replace", index=False)

conn.close()

print("✅ ola_rides table created successfully")
