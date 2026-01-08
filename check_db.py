import sqlite3

print("🔍 Checking database...")

conn = sqlite3.connect("ola.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in database:", tables)

conn.close()
