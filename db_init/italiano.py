import sqlite3


connection = sqlite3.connect('templates/materie/Italiano/Italiano.db')
with open('/db/italiano.sql') as f:
    connection.executescript(f.read())
connection.commit()
connection.close