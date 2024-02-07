import sqlite3


connection = sqlite3.connect('templates/materie/Storia/Storia.db')
with open('db/storia.sql') as f:
    connection.executescript(f.read())
connection.commit()
connection.close