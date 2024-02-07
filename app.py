from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)
# ita
db='data.db'
# set FLASK_APP=app.py
# set FLASK_ENV=development
# flask run --debug

@app.route('/<int:idx>/delete', methods=('POST',))
def delete(idx):
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row
    connection.execute('DELETE FROM Alternativa WHERE id=?', (idx,))
    connection.execute('DELETE FROM  Disegno_progettazzione_e_oranizzazione_industriale WHERE id=?', (idx,))
    connection.execute('DELETE FROM  Educazione_civica WHERE id=?', (idx,))
    connection.execute('DELETE FROM  Italiano WHERE id=?', (idx,))
    connection.execute('DELETE FROM  inglese WHERE id=?', (idx,))
    connection.execute('DELETE FROM  Matematica WHERE id=?', (idx,))
    connection.execute('DELETE FROM  Meccanica_macchine WHERE id=?', (idx,))
    connection.execute('DELETE FROM  Scienze_motorie WHERE id=?', (idx,))
    connection.execute('DELETE FROM  Storia WHERE id=?', (idx,))
    connection.execute('DELETE FROM  Tornio WHERE id=?', (idx,))
    connection.commit()
    connection.close
    return redirect('/materie')

@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')

@app.route('/materie', methods=('GET', 'POST'))
def materie():
    return render_template('/materie/materie.html')


@app.route('/alternativa', methods=('GET', 'POST'))
def alternativa():
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row
    Alternativa = connection.execute('SELECT * FROM Alternativa').fetchall()

    return render_template('/materie/Alternativa/Alternativa.html', Alternativa=Alternativa)

@app.route('/Disegno_progettazzione_e_oranizzazione_industriale', methods=('GET', 'POST'))
def Disegno_progettazzione_e_oranizzazione_industriale():
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row
    Disegno_progettazzione_e_oranizzazione_industriale = connection.execute('SELECT * FROM Disegno_progettazzione_e_oranizzazione_industriale').fetchall()


    return render_template('/materie/Disegno_progettazzione_e_oranizzazione_industriale/Disegno_progettazzione_e_oranizzazione_industriale.html', Disegno_progettazzione_e_oranizzazione_industriale=Disegno_progettazzione_e_oranizzazione_industriale)

@app.route('/Educazione_Civica', methods=('GET', 'POST'))
def Educazione_Civica():
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row
    Educazione_Civica = connection.execute('SELECT * FROM Educazione_Civica').fetchall()

    return render_template('/materie/Educazione_Civica/Educazione_Civica.html', Educazione_Civica=Educazione_Civica)

@app.route('/Italiano', methods=('GET', 'POST'))
def Italiano():

    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row
    Italiano = connection.execute('SELECT * FROM Italiano').fetchall()

    return render_template('/materie/Italiano/Italiano.html', Italiano=Italiano)

@app.route('/Inglese', methods=('GET', 'POST'))
def inglese():

    
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row
    Inglese = connection.execute('SELECT * FROM Inglese').fetchall()

    return render_template('/materie/inglese/inglese.html', Inglese=Inglese)

@app.route('/Matematica', methods=('GET', 'POST'))
def Matematica():

    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row
    Matematica = connection.execute('SELECT * FROM Matematica').fetchall()

    return render_template('/materie/Matematica/Matematica.html', Matematica=Matematica)

@app.route('/Meccanica_macchine', methods=('GET', 'POST'))
def Meccanica_macchine():
    
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row
    Meccanica_macchine = connection.execute('SELECT * FROM Meccanica_macchine').fetchall()

    return render_template('/materie/Meccanica_macchine/Meccanica_macchine.html', Meccanica_macchine=Meccanica_macchine)

@app.route('/scienze_motorie', methods=('GET', 'POST'))
def scienze_motorie():
    
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row
    Scienze_motorie = connection.execute('SELECT * FROM Scienze_motorie').fetchall()

    return render_template('/materie/scienze_motorie/scienze_motorie.html', Scienze_motorie=Scienze_motorie)

@app.route('/Storia', methods=('GET', 'POST'))
def Storia():
    
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row
    Storia = connection.execute('SELECT * FROM Storia').fetchall()

    return render_template('/materie/Storia/Storia.html', Storia=Storia)

@app.route('/Tornio', methods=('GET', 'POST'))
def Tornio():
    
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row
    Tornio = connection.execute('SELECT * FROM Tornio').fetchall()

    return render_template('/materie/Tornio/Tornio.html', Tornio=Tornio)
                                        #crea
@app.route('/crea_alternativa', methods=('GET', 'POST'))
def crea_alternativa():

    if request.method == 'POST':
        titolo = request.form['titolo']
        info = request.form['info']

        connection = sqlite3.connect(db)
        connection.row_factory = sqlite3.Row
        connection.execute(
            'INSERT INTO Alternativa (TITOLO, INFO) VALUES(?, ?)',
            (titolo, info)
        )
        connection.commit()
        connection.close()
        return redirect('/alternativa')
    return render_template('/materie/Alternativa/crea.html')

@app.route('/crea_Disegno_progettazzione_e_oranizzazione_industriale', methods=('GET', 'POST'))
def crea_Disegno_progettazzione_e_oranizzazione_industriale():

    if request.method == 'POST':
        titolo = request.form['titolo']
        info = request.form['info']

        connection = sqlite3.connect(db)
        connection.row_factory = sqlite3.Row
        connection.execute(
            'INSERT INTO Disegno_progettazzione_e_oranizzazione_industriale (TITOLO, INFO) VALUES(?, ?)',
            (titolo, info)
        )
        connection.commit()
        connection.close()
        return redirect('/Disegno_progettazzione_e_oranizzazione_industriale')
    return render_template('/materie/Disegno_progettazzione_e_oranizzazione_industriale/crea.html')


@app.route('/crea_Educazione_Civica', methods=('GET', 'POST'))
def crea_Educazione_Civica():

    if request.method == 'POST':
        titolo = request.form['titolo']
        info = request.form['info']

        connection = sqlite3.connect(db)
        connection.row_factory = sqlite3.Row
        connection.execute(
            'INSERT INTO Educazione_Civica (TITOLO, INFO) VALUES(?, ?)',
            (titolo, info)
        )
        connection.commit()
        connection.close()
        return redirect('/Educazione_Civica')
    return render_template('/materie/Educazione_Civica/crea.html')

@app.route('/crea_Italiano', methods=('GET', 'POST'))
def crea_Italiano():

    if request.method == 'POST':
        titolo = request.form['titolo']
        info = request.form['info']

        connection = sqlite3.connect(db)
        connection.row_factory = sqlite3.Row
        connection.execute(
            'INSERT INTO Italiano (TITOLO, INFO) VALUES(?, ?)',
            (titolo, info)
        )
        connection.commit()
        connection.close()
        return redirect('/Italiano')

    return render_template('/materie/Italiano/crea.html')

@app.route('/crea_Inglese', methods=('GET', 'POST'))
def crea_inglese():

    if request.method == 'POST':
        titolo = request.form['titolo']
        info = request.form['info']

        connection = sqlite3.connect(db)
        connection.row_factory = sqlite3.Row
        connection.execute(
            'INSERT INTO Inglese (TITOLO, INFO) VALUES(?, ?)',
            (titolo, info)
        )
        connection.commit()
        connection.close()
        return redirect('Inglese')
    return render_template('/materie/inglese/crea.html')

@app.route('/crea_Matematica', methods=('GET', 'POST'))
def crea_Matematica():


    if request.method == 'POST':
        titolo = request.form['titolo']
        info = request.form['info']

        connection = sqlite3.connect(db)
        connection.row_factory = sqlite3.Row
        connection.execute(
            'INSERT INTO Matematica (TITOLO, INFO) VALUES(?, ?)',
            (titolo, info)
        )
        connection.commit()
        connection.close()
        return redirect('Matematica')
    return render_template('/materie/Matematica/crea.html')

@app.route('/crea_Meccanica_macchine', methods=('GET', 'POST'))
def crea_Meccanica_macchine():

    if request.method == 'POST':
        titolo = request.form['titolo']
        info = request.form['info']

        connection = sqlite3.connect(db)
        connection.row_factory = sqlite3.Row
        connection.execute(
            'INSERT INTO Meccanica_macchine (TITOLO, INFO) VALUES(?, ?)',
            (titolo, info)
        )
        connection.commit()
        connection.close()
        return redirect('Meccanica_macchine')
    return render_template('/materie/Meccanica_macchine/crea.html')

@app.route('/crea_scienze_motorie', methods=('GET', 'POST'))
def crea_scienze_motorie():
    
    if request.method == 'POST':
        titolo = request.form['titolo']
        info = request.form['info']

        connection = sqlite3.connect(db)
        connection.row_factory = sqlite3.Row
        connection.execute(
            'INSERT INTO Scienze_motorie (TITOLO, INFO) VALUES(?, ?)',
            (titolo, info)
        )
        connection.commit()
        connection.close()
        return redirect('scienze_motorie')
    return render_template('/materie/scienze_motorie/crea.html')

@app.route('/crea_Storia', methods=('GET', 'POST'))
def crea_Storia():
    
    if request.method == 'POST':
        titolo = request.form['titolo']
        info = request.form['info']

        connection = sqlite3.connect(db)
        connection.row_factory = sqlite3.Row
        connection.execute(
            'INSERT INTO Storia (TITOLO, INFO) VALUES(?, ?)',
            (titolo, info)
        )
        connection.commit()
        connection.close()
        return redirect('Storia')
    return render_template('/materie/Storia/crea.html')

@app.route('/crea_Tornio', methods=('GET', 'POST'))
def crea_Tornio():
        
    if request.method == 'POST':
        titolo = request.form['titolo']
        info = request.form['info']

        connection = sqlite3.connect(db)
        connection.row_factory = sqlite3.Row
        connection.execute(
            'INSERT INTO Tornio (TITOLO, INFO) VALUES(?, ?)',
            (titolo, info)
        )
        connection.commit()
        connection.close()
        return redirect('Tornio')
    return render_template('/materie/Tornio/crea.html')

