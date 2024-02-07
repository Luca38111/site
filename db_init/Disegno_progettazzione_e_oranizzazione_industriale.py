import sqlite3


connection = sqlite3.connect('templates/materie/Disegno_progettazzione_e_oranizzazione_industriale/Disegno_progettazzione_e_oranizzazione_industriale.db')
with open('db/Disegno_progettazzione_e_oranizzazione_industriale.sql') as f:
    connection.executescript(f.read())
connection.commit()
connection.close