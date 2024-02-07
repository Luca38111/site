DROP TABLE IF EXISTS Alternativa;
CREATE TABLE Alternativa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titolo TEXT,
    info TEXT
);
INSERT INTO
    Alternativa (titolo, info)
VALUES
    ('Alternativa', '');

DROP TABLE IF EXISTS Disegno_progettazzione_e_oranizzazione_industriale;
CREATE TABLE Disegno_progettazzione_e_oranizzazione_industriale (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titolo TEXT,
    info TEXT
);
INSERT INTO
    Disegno_progettazzione_e_oranizzazione_industriale (titolo, info)
VALUES
    ('Disegno_progettazzione_e_oranizzazione_industriale', '');

DROP TABLE IF EXISTS Educazione_civica;
CREATE TABLE Educazione_civica (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titolo TEXT,
    info TEXT
);
INSERT INTO
    Educazione_civica (titolo, info)
VALUES
    ('Educazione_civica', '');

DROP TABLE IF EXISTS Italiano;
CREATE TABLE Italiano (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titolo TEXT,
    info TEXT
);
INSERT INTO
    Italiano (titolo, info)
VALUES
    ('Italiano', '');

DROP TABLE IF EXISTS inglese;
CREATE TABLE inglese (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titolo TEXT,
    info TEXT
);
INSERT INTO
    inglese (titolo, info)
VALUES
    ('inglese', '');

DROP TABLE IF EXISTS Matematica;
CREATE TABLE Matematica (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titolo TEXT,
    info TEXT
);
INSERT INTO
    Matematica (titolo, info)
VALUES
    ('Matematica', '');

DROP TABLE IF EXISTS Meccanica_macchine;
CREATE TABLE Meccanica_macchine (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titolo TEXT,
    info TEXT
);
INSERT INTO
    Meccanica_macchine (titolo, info)
VALUES
    ('Meccanica_macchine', '');

DROP TABLE IF EXISTS Scienze_motorie;
CREATE TABLE Scienze_motorie (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titolo TEXT,
    info TEXT
);
INSERT INTO
    Scienze_motorie (titolo, info)
VALUES
    ('Scienze_motorie', '');

DROP TABLE IF EXISTS Storia;
CREATE TABLE Storia (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titolo TEXT,
    info TEXT
);
INSERT INTO
    Storia (titolo, info)
VALUES
    ('Storia', '');

DROP TABLE IF EXISTS Tornio;
CREATE TABLE Tornio (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titolo TEXT,
    info TEXT
);
INSERT INTO
    Tornio (titolo, info)
VALUES
    ('Tornio', '');

