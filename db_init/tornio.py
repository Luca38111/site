import sqlite3


connection = sqlite3.connect('templates/materie/Tornio/Tornio.db')
with open('db/tornio.sql') as f:
    connection.executescript(f.read())
connection.commit()
connection.close