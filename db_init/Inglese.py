import sqlite3


connection = sqlite3.connect('templates/materie/Inglese/Inglese.db')
with open('db/Inglese.sql') as f:
    connection.executescript(f.read())
connection.commit()
connection.close