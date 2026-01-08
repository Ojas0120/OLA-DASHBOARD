import sqlite3
import pandas as pd

conn = sqlite3.connect("ola.db")
df = pd.read_sql("SELECT * FROM ola_rides LIMIT 5", conn)

print("Columns in ola_rides table:")
print(df.columns.tolist())

conn.close()
