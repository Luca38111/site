import sqlite3


connection = sqlite3.connect('templates/materie/Matematica/Matematica.db')
with open('db/Matematica.sql') as f:
    connection.executescript(f.read())
connection.commit()
connection.close