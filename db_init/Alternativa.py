import sqlite3


connection = sqlite3.connect('templates/materie/Alternativa/Alternativa.db')
with open('db/Alternativa.sql') as f:
    connection.executescript(f.read())
connection.commit()
connection.close