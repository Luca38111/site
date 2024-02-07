import sqlite3


connection = sqlite3.connect('templates/materie/Educazione_Civica/Educazione_Civica.db')
with open('db/Educazione_Civica.sql') as f:
    connection.executescript(f.read())
connection.commit()
connection.close