import sqlite3


connection = sqlite3.connect('templates/materie/Meccanica_macchine/Meccanica_macchine.db')
with open('db/Meccanica_macchine.sql') as f:
    connection.executescript(f.read())
connection.commit()
connection.close