import sqlite3
connection = sqlite3.connect("factory.db")
print("Database opened Successfully")
cursor = connection.cursor()
connection.execute("create table products (name TEXT NOT NULL, Quantity INTEGER NOT NULL)")
print("Table created Successfully")
connection.close()
