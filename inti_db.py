import sqlite3


connection = sqlite3.connect('data.db')
with open('crea.sql') as f:
    connection.executescript(f.read())
connection.commit()
connection.close