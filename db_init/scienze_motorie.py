import sqlite3


connection = sqlite3.connect('templates/materie/scienze_motorie/scienze_motorie.db')
with open('db/scienze_motorie.sql') as f:
    connection.executescript(f.read())
connection.commit()
connection.close