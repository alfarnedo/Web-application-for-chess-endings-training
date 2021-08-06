"""
LIBRARIES TO USE
"""
#For the database
import mysql.connector as sql

#The Flask object is imported
from flask import Flask

#The SocketIO transport protocol is imported
from flask_socketio import SocketIO

#The following functions of the flask package are installed:
#render_template, session, request, flash, redirect, url_for
from flask import render_template, flash, redirect, url_for, session, request

#wtforms library must be installed
#From this library the functions that are imported are:
#Form, StringField, PasswordField y validators
from wtforms import Form, StringField, PasswordField, validators

#passlib.hash library must be installed
#From this library the function that is imported is:
#sha256_crypt
from passlib.hash import sha256_crypt

#python-chess and chess libraries must be installed
#From these libraries, chess and chess.engine are imported
import chess
import chess.engine

#datetime library must be installed
#From this library the function that is imported is:
#date
from datetime import date

#Os is imported
import os

"""
CREATION OF THE WEB APPLICATION WITH ITS RESPECTIVE FUNCTIONS
"""
#Create a web app instance
app = Flask(__name__)
socketio = SocketIO(app)
app.secret_key = 'secret123'

#Connects to MySQL
connection = sql.connect(user = 'root',
                         host = 'localhost',
                         passwd = "enter your own password",
                         database = 'ChessOnlineAlfar')

#A) If the connection is available:
if connection.is_connected():
    print("Connection available")

#B) If the connection isn't available
else:
    print("Connection failed")


#RegisterForm class is created to later, be able to take the information
#that the user inserts in the registration form
class RegisterForm(Form):
    name = StringField('Name',[validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
             validators.DataRequired(),
             validators.EqualTo('confirm', message='Password do not match')
             ])
    confirm = PasswordField('Confirm Password')


#The main menu is displayed
@app.route('/')
def index():
    return render_template("index.html")

#Registration form is displayed
@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegisterForm(request.form)
    #The POST method is used to take the information
    #that the user inserts in the registration form
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        #An instance of the class "cursor ()" is created
        cur = connection.cursor()

        #The "SQL" statement called 'INSERT' is declared to insert the data
        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)",(name, email, username, password))
        connection.commit()
        #The cursor closes
        cur.close()

        #The tables in the database, finals and nummovi, are initialized

        #Name of all chess endings available in the application
        nombrefinalTorre = "Final_Torre_Y_Rey_Vs_Rey"
        nombrefinalAlfiles = "Final_Alfiles_Y_Rey_Vs_Rey"
        nombrefinalDama = "Final_Dama_Y_Rey_Vs_Rey"
        nombrefinalCaballo = "Final_Alfil_Caballo_Y_Rey_Vs_Rey"
        nombrefinalTorres = "Final_Torres_Y_Rey_Vs_Rey"
        nombrefinalCaballoYRey = "Final_Caballo_Y_Rey_Vs_Peon_Y_Rey"
        nombrefinalDamaYRey = "Final_Dama_Y_Rey_Vs_Peon_Y_Rey"

        #Rest of variables that are initialized
        user = username
        today = date.today()
        today_str = today.strftime('%d-%m-%Y')
        winS = "0"
        loseS = "0"
        movimientoS = "0"
        var1 = "08686904"
        var2 = "27686905"
        var3 = "08686911"
        var4 = "26686903"
        var5 = "19686911"
        var6 = "13686907"

        cursor = connection.cursor()

        #Data is saved in the finals table
        cursor.execute('INSERT INTO finals(username, final, win, lose, fecha) VALUES(%s, %s, %s, %s, %s)',(user, nombrefinalTorre, winS, loseS, today_str))
        connection.commit()

        #Data is saved in the nummovi table
        cursor.execute('INSERT INTO nummovi(username, final, movimientos, fecha) VALUES(%s, %s, %s, %s)',(user, nombrefinalTorre, movimientoS,today_str))
        connection.commit()

        #Data is saved in the finals table
        cursor.execute('INSERT INTO finals(username, final, win, lose, fecha) VALUES(%s, %s, %s, %s, %s)',(user, nombrefinalAlfiles, winS, loseS, today_str))
        connection.commit()

        #Data is saved in the nummovi table
        cursor.execute('INSERT INTO nummovi(username, final, movimientos, fecha) VALUES(%s, %s, %s, %s)',(user, nombrefinalAlfiles, movimientoS,today_str))
        connection.commit()

        #Data is saved in the finals table
        cursor.execute('INSERT INTO finals(username, final, win, lose, fecha) VALUES(%s, %s, %s, %s, %s)',(user, nombrefinalDama, winS, loseS, today_str))
        connection.commit()

        #Data is saved in the nummovi table
        cursor.execute('INSERT INTO nummovi(username, final, movimientos, fecha) VALUES(%s, %s, %s, %s)',(user, nombrefinalDama, movimientoS,today_str))
        connection.commit()

        #Data is saved in the finals table
        cursor.execute('INSERT INTO finals(username, final, win, lose, fecha) VALUES(%s, %s, %s, %s, %s)',(user, nombrefinalCaballo, winS, loseS, today_str))
        connection.commit()

        #Data is saved in the nummovi table
        cursor.execute('INSERT INTO nummovi(username, final, movimientos, fecha) VALUES(%s, %s, %s, %s)',(user, nombrefinalCaballo, movimientoS,today_str))
        connection.commit()

        #Data is saved in the finals table
        cursor.execute('INSERT INTO finals(username, final, win, lose, fecha) VALUES(%s, %s, %s, %s, %s)',(user, nombrefinalTorres, winS, loseS, today_str))
        connection.commit()

        #Data is saved in the nummovi table
        cursor.execute('INSERT INTO nummovi(username, final, movimientos, fecha) VALUES(%s, %s, %s, %s)',(user, nombrefinalTorres, movimientoS,today_str))
        connection.commit()

        #Data is saved in the finals table
        cursor.execute('INSERT INTO finals(username, final, win, lose, fecha) VALUES(%s, %s, %s, %s, %s)',(user, nombrefinalCaballoYRey, winS, loseS, today_str))
        connection.commit()

        #Data is saved in the nummovi table
        cursor.execute('INSERT INTO nummovi(username, final, movimientos, fecha) VALUES(%s, %s, %s, %s)',(user, nombrefinalCaballoYRey, movimientoS,today_str))
        connection.commit()

        #Data is saved in the finals table
        cursor.execute('INSERT INTO finals(username, final, win, lose, fecha) VALUES(%s, %s, %s, %s, %s)',(user, nombrefinalDamaYRey, winS, loseS, today_str))
        connection.commit()

        #Data is saved in the nummovi table
        cursor.execute('INSERT INTO nummovi(username, final, movimientos, fecha) VALUES(%s, %s, %s, %s)',(user, nombrefinalDamaYRey, movimientoS,today_str))
        connection.commit()

        #Closes the cursor
        cursor.close()

        flash('You are now registered and can log in', 'success')
        return redirect(url_for('index'))

    return render_template('registration.html', form=form)

#Log In form is displayed
@app.route('/login', methods=['GET', 'POST'])
def login():
    #The POST method is used to take the information
    #that the user inserts in the log in form
    if request.method == 'POST':
        username = request.form['username']
        password_candidate = request.form['password']

        cursor = connection.cursor()

        #Certain information is selected from the users table
        cursor.execute('SELECT * FROM users WHERE username =%s', [username])
        rows = cursor.fetchall()
        results = len(rows)

        if results > 0:
            row = rows[0]
            password = row[4]

            #If the passwords match:
            if sha256_crypt.verify(password_candidate, password):
                #The following information is saved in session variables
                session['logged_in'] = True
                session['username'] = username

                flash('You are logged in', 'success')
                app.logger.info('PASSWORD MATCHED')

                return redirect(url_for('indexRegisteredUser'))

                #Closes the cursor first and then the connection
                cursor.close()
                connection.close()

            #If the passwords do not match:
            else:
                app.logger.info('PASSWORD NO MATCHED')
                flash('Invalid login', 'danger')
                error = 'Invalid login'
                return render_template('login.html', error=error)

                #Closes the cursor first and then the connection
                cursor.close()
                connection.close()

        #If the username does not exist in the users table:
        else:

            app.logger.info('NO USER')
            flash('Username not found', 'danger')
            error = 'Username not found'

            return render_template('login.html', error=error)

    return render_template('login.html')

#The main menu of the registered user is displayed
@app.route('/indexRegisteredUser')
def indexRegisteredUser():
    return render_template("indexRegisteredUser.html")

#Log Out option is displayed
@app.route('/logout')
def logout():
    session.clear()
    flash('Your are now logged out','success')
    return redirect(url_for('login'))


#About us option is displayed
@app.route('/info')
def info():
    return render_template("info.html")

#About us option of the registered user is displayed
@app.route('/infoRegisteredUser')
def infoRegisteredUser():
    return render_template("infoRegisteredUser.html")

#Objective option is displayed
@app.route('/objective')
def objective():
    return render_template("objective.html")

#Basic Chess Endings Statistics option is displayed
@app.route('/basicChessEndingStatistics')
def basicChessEndingStatistics():
    #Name of all Basic Chess endings available in the web application
    nombrefinalTorre = "Final_Torre_Y_Rey_Vs_Rey"
    nombrefinalAlfiles = "Final_Alfiles_Y_Rey_Vs_Rey"
    nombrefinalDama = "Final_Dama_Y_Rey_Vs_Rey"
    nombrefinalCaballo = "Final_Alfil_Caballo_Y_Rey_Vs_Rey"
    nombrefinalTorres = "Final_Torres_Y_Rey_Vs_Rey"
    nombrefinalCaballoYRey = "Final_Caballo_Y_Rey_Vs_Peon_Y_Rey"
    nombrefinalDamaYRey = "Final_Dama_Y_Rey_Vs_Peon_Y_Rey"
    #Name of the username
    user = session.get('username')

    #ROOK AND KING VS KING BASIC CHESS ENDING

    #1) Average number of movements
    cursor = connection.cursor()

    #The "SQL" statement called 'SELECT' is declared to select information
    cursor.execute('SELECT MOVIMIENTOS FROM nummovi WHERE USERNAME = "'+user+'" AND FINAL = "'+nombrefinalTorre+'"')
    movimientos = cursor.fetchall()
    tmn = len(movimientos)

    #The "SQL" statement called 'SELECT' is declared to select the sum of the movements of this chess ending
    cursor.execute('SELECT SUM(MOVIMIENTOS) FROM nummovi WHERE USERNAME = "'+user+'" AND FINAL = "'+nombrefinalTorre+'"')
    movi=cursor.fetchone()[0]
    moviI = int(movi)

    #If the user has not yet played any chess ending
    if (moviI == 0 and tmn == 1):
        moviIF = 0
    #If the user has played this chess ending
    else:
        #Average
        moviIF = int(moviI / (tmn - 1))

    session['nummoviTorre'] = moviIF
    session['nummovifinalTorre'] = nombrefinalTorre


    #2) Percentage of the number of times the user achieves the goal of this chess ending

    #The "SQL" statement called 'SELECT' is declared to select information
    cursor.execute('SELECT * FROM finals WHERE final = "'+nombrefinalTorre+'"')
    rows = cursor.fetchall()
    results = len(rows)

    if results > 0:
        #A) Number of times the objective of this chess ending is met

        #The "SQL" statement called 'SELECT' is declared to select the sum of the wins of this chess ending
        cursor.execute('SELECT SUM(WIN) FROM finals where USERNAME = "'+user+'" AND FINAL="'+nombrefinalTorre+'"')
        win=cursor.fetchone()[0]
        winI = int(win)

        #B) Number of times the objective of this chess ending is not met

        #The "SQL" statement called 'SELECT' is declared to select the sum of the loses of this chess ending
        cursor.execute('SELECT SUM(LOSE) FROM finals where USERNAME = "'+user+'" AND FINAL="'+nombrefinalTorre+'"')
        lose=cursor.fetchone()[0]
        loseI = int(lose)

        #C) Sum of the number of times this chess ending goal is achieved, plus the number of times this chess ending
        #goal is not achieved
        intentosI = winI + loseI
        numeI = winI * 100

        #If the user has not yet played any chess ending
        if (numeI == 0 and intentosI ==0):
            porcentaje = "0"
        #If the user has played this chess ending
        else:
            #Percentage
            porcentaje = numeI / intentosI

        porcentajeI = int(porcentaje)

        # They are stored in session variables:
        # 1) the name of this chess ending
        # 2) the number of times the goal of this chess ending is achieved
        # 3) the number of times the goal of this chess ending is not achieved
        # 4) the number of times this chess ending has been attempted
        # 5) The percentage of times the goal of this chess ending is achieved

        session['final'] = nombrefinalTorre
        session['win'] = winI
        session['lose'] = loseI
        session['intentos'] = intentosI
        session['porcentaje'] = porcentajeI


    #Once the procedure that has been developed for the Rook and King vs King chess ending has been
    #explained,it will be applied to the rest of the Basic Chess endings with some variation
    #with respect to the name of the chess ending which is referred to
    #in each case

    #BISHOPS AND KING VS KING BASIC CHESS ENDING

    #1) Average number of movements
    cursor = connection.cursor()
    cursor.execute('SELECT MOVIMIENTOS FROM nummovi WHERE USERNAME = "'+user+'" AND FINAL = "'+nombrefinalAlfiles+'"')

    movimientos = cursor.fetchall()
    tmn = len(movimientos)

    cursor.execute('SELECT SUM(MOVIMIENTOS) FROM nummovi WHERE USERNAME = "'+user+'" AND FINAL = "'+nombrefinalAlfiles+'"')
    movi=cursor.fetchone()[0]
    moviI = int(movi)

    if (moviI == 0 and tmn == 1):
        moviIF = 0
    else:
        moviIF = int(moviI / (tmn - 1))

    session['nummoviAlfiles'] = moviIF
    session['nummovifinalAlfiles'] = nombrefinalAlfiles

    #2) Percentage of the number of times the user achieves the goal of this chess ending
    cursor.execute('SELECT * FROM finals WHERE final = "'+nombrefinalAlfiles+'"')
    rows2 = cursor.fetchall()
    results2 = len(rows2)

    if results2 > 0:
        cursor.execute('SELECT SUM(WIN) FROM finals where USERNAME = "'+user+'" AND FINAL="'+nombrefinalAlfiles+'"')
        win=cursor.fetchone()[0]
        winI = int(win)

        cursor.execute('SELECT SUM(LOSE) FROM finals where USERNAME = "'+user+'" AND FINAL="'+nombrefinalAlfiles+'"')
        lose=cursor.fetchone()[0]
        loseI = int(lose)

        intentosI = winI + loseI
        numeI = winI * 100

        if (numeI == 0 and intentosI ==0):
            porcentaje = "0"
        else:
            porcentaje = numeI / intentosI

        porcentajeI = int(porcentaje)

        session['finalAlfiles'] = nombrefinalAlfiles
        session['winAlfiles'] = winI
        session['loseAlfiles'] = loseI
        session['intentosAlfiles'] = intentosI
        session['porcentajeAlfiles'] = porcentajeI

    #QUEEN AND KING VS KING BASIC CHESS ENDING

    #1) Average number of movements
    cursor = connection.cursor()
    cursor.execute('SELECT MOVIMIENTOS FROM nummovi WHERE USERNAME = "'+user+'" AND FINAL = "'+nombrefinalDama+'"')

    movimientos = cursor.fetchall()
    tmn = len(movimientos)

    cursor.execute('SELECT SUM(MOVIMIENTOS) FROM nummovi WHERE USERNAME = "'+user+'" AND FINAL = "'+nombrefinalDama+'"')
    movi=cursor.fetchone()[0]
    moviI = int(movi)

    if (moviI == 0 and tmn == 1):
        moviIF = 0
    else:
        moviIF = int(moviI / (tmn - 1))

    session['nummoviDama'] = moviIF
    session['nummovifinalDama'] = nombrefinalDama

    #2) Percentage of the number of times the user achieves the goal of this chess ending
    cursor.execute('SELECT * FROM finals WHERE final = "'+nombrefinalDama+'"')
    rows = cursor.fetchall()
    results = len(rows)

    if results > 0:
        cursor.execute('SELECT SUM(WIN) FROM finals where USERNAME = "'+user+'" AND FINAL="'+nombrefinalDama+'"')
        win=cursor.fetchone()[0]
        winI = int(win)

        cursor.execute('SELECT SUM(LOSE) FROM finals where USERNAME = "'+user+'" AND FINAL="'+nombrefinalDama+'"')
        lose=cursor.fetchone()[0]
        loseI = int(lose)

        intentosI = winI + loseI
        numeI = winI * 100

        if (numeI == 0 and intentosI ==0):
            porcentaje = "0"
        else:
            porcentaje = numeI / intentosI

        porcentajeI = int(porcentaje)

        session['finalDama'] = nombrefinalDama
        session['winDama'] = winI
        session['loseDama'] = loseI
        session['intentosDama'] = intentosI
        session['porcentajeDama'] = porcentajeI

    #BISHOP, KNIGHT AND KING VS KING BASIC CHESS ENDING

    #1) Average number of movements
    cursor = connection.cursor()
    cursor.execute('SELECT MOVIMIENTOS FROM nummovi WHERE USERNAME = "'+user+'" AND FINAL = "'+nombrefinalCaballo+'"')

    movimientos = cursor.fetchall()
    tmn = len(movimientos)

    cursor.execute('SELECT SUM(MOVIMIENTOS) FROM nummovi WHERE USERNAME = "'+user+'" AND FINAL = "'+nombrefinalCaballo+'"')
    movi=cursor.fetchone()[0]
    moviI = int(movi)

    if (moviI == 0 and tmn == 1):
        moviIF = 0
    else:
        moviIF = int(moviI / (tmn - 1))

    session['nummoviCaballo'] = moviIF
    session['nummovifinalCaballo'] = nombrefinalCaballo

    #2) Percentage of the number of times the user achieves the goal of this chess ending
    cursor.execute('SELECT * FROM finals WHERE final = "'+nombrefinalCaballo+'"')
    rows = cursor.fetchall()
    results = len(rows)

    if results > 0:
        cursor.execute('SELECT SUM(WIN) FROM finals where USERNAME = "'+user+'" AND FINAL="'+nombrefinalCaballo+'"')
        win=cursor.fetchone()[0]
        winI = int(win)

        cursor.execute('SELECT SUM(LOSE) FROM finals where USERNAME = "'+user+'" AND FINAL="'+nombrefinalCaballo+'"')
        lose=cursor.fetchone()[0]
        loseI = int(lose)

        intentosI = winI + loseI
        numeI = winI * 100

        if (numeI == 0 and intentosI ==0):
            porcentaje = "0"
        else:
            porcentaje = numeI / intentosI

        porcentajeI = int(porcentaje)

        session['finalCaballo'] = nombrefinalCaballo
        session['winCaballo'] = winI
        session['loseCaballo'] = loseI
        session['intentosCaballo'] = intentosI
        session['porcentajeCaballo'] = porcentajeI

    #ROOKS AND KING VS KING BASIC CHESS ENDING

    #1) Average number of movements
    cursor = connection.cursor()
    cursor.execute('SELECT MOVIMIENTOS FROM nummovi WHERE USERNAME = "'+user+'" AND FINAL = "'+nombrefinalTorres+'"')

    movimientos = cursor.fetchall()
    tmn = len(movimientos)

    cursor.execute('SELECT SUM(MOVIMIENTOS) FROM nummovi WHERE USERNAME = "'+user+'" AND FINAL = "'+nombrefinalTorres+'"')
    movi=cursor.fetchone()[0]
    moviI = int(movi)

    if (moviI == 0 and tmn == 1):
        moviIF = 0
    else:
        moviIF = int(moviI / (tmn - 1))

    session['nummoviTorres'] = moviIF
    session['nummovifinalTorres'] = nombrefinalTorres

    #2) Percentage of the number of times the user achieves the goal of this chess ending
    cursor.execute('SELECT * FROM finals WHERE final = "'+nombrefinalTorres+'"')
    rows = cursor.fetchall()
    results = len(rows)

    if results > 0:
        cursor.execute('SELECT SUM(WIN) FROM finals where USERNAME = "'+user+'" AND FINAL="'+nombrefinalTorres+'"')
        win=cursor.fetchone()[0]
        winI = int(win)

        cursor.execute('SELECT SUM(LOSE) FROM finals where USERNAME = "'+user+'" AND FINAL="'+nombrefinalTorres+'"')
        lose=cursor.fetchone()[0]
        loseI = int(lose)

        intentosI = winI + loseI
        numeI = winI * 100

        if (numeI == 0 and intentosI ==0):
            porcentaje = "0"
        else:
            porcentaje = numeI / intentosI

        porcentajeI = int(porcentaje)

        session['finalTorres'] = nombrefinalTorres
        session['winTorres'] = winI
        session['loseTorres'] = loseI
        session['intentosTorres'] = intentosI
        session['porcentajeTorres'] = porcentajeI

    return render_template('basicChessEndingStatistics.html')

#Practical Chess Endings Statistics option is displayed
@app.route('/practicalChessEndingStatistics')
def practicalChessEndingStatistics():
    #Name of all Practical Chess Endings available in the application
    nombrefinalCaballoYRey = "Final_Caballo_Y_Rey_Vs_Peon_Y_Rey"
    nombrefinalDamaYRey = "Final_Dama_Y_Rey_Vs_Peon_Y_Rey"
    #Name of the username
    user = session.get('username')

    #KNIGHT AND KING VS PAWN AND KING PRACTICAL CHESS ENDING

    #1) Average number of movements
    cursor = connection.cursor()

    #The "SQL" statement called 'SELECT' is declared to select information
    cursor.execute('SELECT MOVIMIENTOS FROM nummovi WHERE USERNAME = "'+user+'" AND FINAL = "'+nombrefinalCaballoYRey+'"')
    movimientos = cursor.fetchall()
    tmn = len(movimientos)

    #The "SQL" statement called 'SELECT' is declared to select the sum of the movements of this chess ending
    cursor.execute('SELECT SUM(MOVIMIENTOS) FROM nummovi WHERE USERNAME = "'+user+'" AND FINAL = "'+nombrefinalCaballoYRey+'"')
    movi=cursor.fetchone()[0]
    moviI = int(movi)

    #If the user has not yet played any chess ending
    if (moviI == 0 and tmn == 1):
        moviIF = 0
    #If the user has played this chess ending
    else:
        #Average
        moviIF = int(moviI / (tmn - 1))

    session['nummoviCaballoYRey'] = moviIF
    session['nummovifinalCaballoYRey'] = nombrefinalCaballoYRey

    #2) Percentage of the number of times the user achieves the goal of this chess ending

    #The "SQL" statement called 'SELECT' is declared to select information
    cursor.execute('SELECT * FROM finals WHERE final = "'+nombrefinalCaballoYRey+'"')
    rows = cursor.fetchall()
    results = len(rows)

    if results > 0:
        #A) Number of times the objective of this chess ending is met

        #The "SQL" statement called 'SELECT' is declared to select the sum of the wins of this chess ending
        cursor.execute('SELECT SUM(WIN) FROM finals where USERNAME = "'+user+'" AND FINAL="'+nombrefinalCaballoYRey+'"')
        win=cursor.fetchone()[0]
        winI = int(win)

        #B) Number of times the objective of this chess ending is not met

        #The "SQL" statement called 'SELECT' is declared to select the sum of the loses of this chess ending
        cursor.execute('SELECT SUM(LOSE) FROM finals where USERNAME = "'+user+'" AND FINAL="'+nombrefinalCaballoYRey+'"')
        lose=cursor.fetchone()[0]
        loseI = int(lose)

        #C) Sum of the number of times this chess ending goal is achieved, plus the number of times
        #this chess ending goal is not achieved
        intentosI = winI + loseI
        numeI = winI * 100

        #If the user has not yet played any chess ending
        if (numeI == 0 and intentosI ==0):
            porcentaje = "0"
        #If the user has played this chess ending
        else:
            porcentaje = numeI / intentosI

        porcentajeI = int(porcentaje)

        # They are stored in session variables:
        # 1) the name of this chess ending
        # 2) the number of times the goal of this chess ending is achieved
        # 3) the number of times the goal of this chess ending is not achieved
        # 4) the number of times this chess ending has been attempted
        # 5) The percentage of times the goal of this chess ending is achieved
        session['finalCaballoYRey'] = nombrefinalCaballoYRey
        session['winCaballoYRey'] = winI
        session['loseCaballoYRey'] = loseI
        session['intentosCaballoYRey'] = intentosI
        session['porcentajeCaballoYRey'] = porcentajeI

    #Once the procedure that has been developed for the Knight and King vs Pawn and King chess ending
    #has been explained,it will be applied to the rest of the Practical Chess endings with some variation
    #with respect to the name of the chess ending which is referred to in each case

    #QUEEN AND KING VS PAWN AND KING PRACTICAL CHESS ENDING

    #1) Average number of movements
    cursor = connection.cursor()
    cursor.execute('SELECT MOVIMIENTOS FROM nummovi WHERE USERNAME = "'+user+'" AND FINAL = "'+nombrefinalDamaYRey+'"')

    movimientos = cursor.fetchall()
    tmn = len(movimientos)

    cursor.execute('SELECT SUM(MOVIMIENTOS) FROM nummovi WHERE USERNAME = "'+user+'" AND FINAL = "'+nombrefinalDamaYRey+'"')
    movi=cursor.fetchone()[0]
    moviI = int(movi)

    if (moviI == 0 and tmn == 1):
        moviIF = 0
    else:
        moviIF = int(moviI / (tmn - 1))

    session['nummoviDamaYRey'] = moviIF
    session['nummovifinalDamaYRey'] = nombrefinalDamaYRey

    #2) Percentage of the number of times the user achieves the goal of this chess ending
    cursor.execute('SELECT * FROM finals WHERE final = "'+nombrefinalDamaYRey+'"')
    rows = cursor.fetchall()
    results = len(rows)

    if results > 0:
        cursor.execute('SELECT SUM(WIN) FROM finals where USERNAME = "'+user+'" AND FINAL="'+nombrefinalDamaYRey+'"')
        win=cursor.fetchone()[0]
        winI = int(win)

        cursor.execute('SELECT SUM(LOSE) FROM finals where USERNAME = "'+user+'" AND FINAL="'+nombrefinalDamaYRey+'"')
        lose=cursor.fetchone()[0]
        loseI = int(lose)

        intentosI = winI + loseI
        numeI = winI * 100

        if (numeI == 0 and intentosI ==0):
            porcentaje = "0"
        else:
            porcentaje = numeI / intentosI

        porcentajeI = int(porcentaje)

        session['finalDamaYRey'] = nombrefinalDamaYRey
        session['winDamaYRey'] = winI
        session['loseDamaYRey'] = loseI
        session['intentosDamaYRey'] = intentosI
        session['porcentajeDamaYRey'] = porcentajeI

    return render_template('practicalChessEndingStatistics.html')

#The option to play Chess is displayed
@app.route('/chessGame')
def chessGame():
    return render_template('chessGame.html')

#To make moves during the game of chess and thus be able to establish
#a game between the user and the chess engine
@app.route('/make_moveChessGame', methods=['POST'])
def make_moveChessGame():

    #An instance of the chess engine is created
    engine = chess.engine.SimpleEngine.popen_uci('./engine/stockfish_13_win_x64.exe')

    #FEN is extracted
    fen = request.form.get('fen')
    #PGN is extracted
    pgn = request.form.get('pgn')
    #The gameover variable is extracted
    gameover = request.form.get('gameover')
    #The value of depth that has been set is extracted
    fixed_depth = request.form.get('fixed_depth')
    #The move time value that has been set is extracted
    move_time = request.form.get('move_time')

    #A chessboard instance is initialized
    board = chess.Board(fen)

    #If a move time is set
    if move_time != '0':
        #If it is an instant move time
        if move_time == 'instant':
            #Search for the best move instantly
            info = engine.analyse(board, chess.engine.Limit(time=0.1))
        #If it is not an instant move time
        else:
            #Search for the best move with a fixed move time
            info = engine.analyse(board, chess.engine.Limit(time=int(move_time)))

    #If a fixed depth is set
    if fixed_depth != '0':
        #Search for the best move with this fixed depth
        info = engine.analyse(board, chess.engine.Limit(depth=int(fixed_depth)))

    #The best move is extracted from info['pv']
    best_move = info['pv'][0]

    #Python chessboard internal state is updated
    board.push(best_move)

    #FEN is extracted from the current state of the board
    fen = board.fen()

    #The value of score is extracted from info to know the state of the game in each move
    resultado = str(info['score'])

    #If the user (the white pieces) has won the game
    if (resultado == "PovScore(Mate(+1), WHITE)"):
        print("WIN")

    #If the user (the white pieces) has lost the game
    if(gameover == "true"):
        print("GAME OVER")

    #The chess engine process is terminated
    engine.quit()

    #The following values ​​are returned to the "make_moveChessGame()" function, the http POST request,
    #of "chessGame.html"
    return {
        'fen': fen,
        'best_move': str(best_move),
        'score': str(info['score']),
        'depth': info['depth'],
        'pv': ' '.join([str(move) for move in info['pv']]),
        'nodes': info['nodes'],
        'time': info['time']
    }


#The option to play basic chess endings is displayed
@app.route('/basicChessEndings')
def basicChessEndings():
    return render_template('basicChessEndings.html')

#To make moves during the basic chess ending game and thus be able to establish
#a game between the user and the chess engine
@app.route('/make_moveBasicChessEndings', methods=['POST'])
def make_moveBasicChessEndings():

    #An instance of the chess engine is created
    engine = chess.engine.SimpleEngine.popen_uci('./engine/stockfish_13_win_x64.exe')

    #FEN is extracted
    fen = request.form.get('fen')
    #PGN is extracted
    pgn = request.form.get('pgn')
    #The gameover variable is extracted
    gameover = request.form.get('gameover')
    #The value of depth that has been set is extracted
    fixed_depth = request.form.get('fixed_depth')
    #The movement time value that has been set is extracted
    move_time = request.form.get('move_time')
    #List is created to save the PGN
    list = []

    #A chessboard instance is initialized
    board = chess.Board(fen)

    #If a move time is set
    if move_time != '0':
        #If it is an instant move time
        if move_time == 'instant':
            #Search for the best move instantly
            info = engine.analyse(board, chess.engine.Limit(time=0.1))
        #If it is not an instant move time
        else:
            #Search for the best move with a fixed move time
            info = engine.analyse(board, chess.engine.Limit(time=int(move_time)))

    #If a fixed depth is set
    if fixed_depth != '0':
        #Search for the best move with this fixed depth
        info = engine.analyse(board, chess.engine.Limit(depth=int(fixed_depth)))

    #The best move is extracted from info['pv']
    best_move = info['pv'][0]

    #Python chessboard internal state is updated
    board.push(best_move)

    #FEN is extracted from the current state of the board
    fen = board.fen()

    #The value of score is extracted from info to know the state of the game in each move
    resultado = str(info['score'])

    #The PGN of the game at that moment is saved in the list
    list = pgn

    #If the user (the white pieces) has achieved the goal of the basic chess ending
    if (resultado == "PovScore(Mate(+1), WHITE)"):
        print("WIN")

        #The number of moves that the user has made is saved
        mov = []

        if (list[-10] == "."):
            mov = list[-12] + list[-11]
        else:
            mov = list[-11] + list[-10]

        movI = int(mov)
        movIF = movI + 1
        print("MOVif ", movIF)
        var7 = "836565"

    #If the user (the white pieces) has not achieved the goal of the basic chess ending
    if(gameover == "true"):
        print("GAME OVER")

    #The chess engine process is terminated
    engine.quit()

    #The following values ​​are returned to the "make_moveBasicChessEndings()" function, the http POST
    #request, of "basicChessEndings.html"
    return {
        'fen': fen,
        'best_move': str(best_move),
        'score': str(info['score']),
        'depth': info['depth'],
        'pv': ' '.join([str(move) for move in info['pv']]),
        'nodes': info['nodes'],
        'time': info['time']
    }

#The option to play Practical chess endings is displayed
@app.route('/practicalChessEnding')
def practicalChessEnding():
    return render_template('practicalChessEnding.html')

#To make moves during the practical chess ending game and thus be able to establish
#a game between the user and the chess engine
@app.route('/make_movePracticalChessEndings', methods=['POST'])
def make_movePracticalChessEndings():

    #An instance of the chess engine is created
    engine = chess.engine.SimpleEngine.popen_uci('./engine/stockfish_13_win_x64.exe')

    #FEN is extracted
    fen = request.form.get('fen')
    #PGN is extracted
    pgn = request.form.get('pgn')
    #The gameover variable is extracted
    gameover = request.form.get('gameover')
    #The tablas variable is extracted
    tablas = request.form.get('tablas')
    #The value of depth that has been set is extracted
    fixed_depth = request.form.get('fixed_depth')
    #The movement time value that has been set is extracted
    move_time = request.form.get('move_time')
    #List is created to save the PGN
    list = []

    #A chessboard instance is initialized
    board = chess.Board(fen)

    #If a move time is set
    if move_time != '0':
        #If it is an instant move time
        if move_time == 'instant':
            #Search for the best move instantly
            info = engine.analyse(board, chess.engine.Limit(time=0.1))
        #If it is not an instant move time
        else:
            #Search for the best move with a fixed move time
            info = engine.analyse(board, chess.engine.Limit(time=int(move_time)))

    #If a fixed depth is set
    if fixed_depth != '0':
        #Search for the best move with this fixed depth
        info = engine.analyse(board, chess.engine.Limit(depth=int(fixed_depth)))

    #The best movement is extracted from info['pv']
    best_move = info['pv'][0]

    #Python chessboard internal state is updated
    board.push(best_move)

    #FEN is extracted from the current state of the board
    fen = board.fen()

    #The value of score is extracted from info to know the state of the game in each move
    resultado = str(info['score'])

    #The PGN of the game at that moment is saved in the list
    list = pgn

    #If the user (the white pieces) has achieved the goal of the practical chess ending
    if (resultado == "PovScore(Mate(+1), WHITE)"):
        print("WIN")
        #The number of moves that the user has made is saved
        mov = []

        if (list[-9] == "."):
            mov = list[-11] + list[-10]
        else:
            mov = list[-10] + list[-9]

        movI = int(mov)
        movIF = movI + 1
        print("MOVif ", movIF)

    #If the user (the white pieces) has achieved stalemate in the Knight and King Vs Pawn and King
    #chess ending
    if ((pgn.find("8/8/8/8/8/4N2p/5K1k/8") >=0 and tablas == "true") or (pgn.find("8/8/8/8/8/p7/3N4/k1K5") >=0 and tablas == "true") or (pgn.find("8/8/5K2/8/8/8/4N2p/7k") >=0 and tablas == "true") or (pgn.find("8/8/5K2/8/8/8/7p/4N2k") >=0 and tablas == "true") or (pgn.find("8/8/5K2/8/8/8/6Np/7k") >=0 and tablas == "true") or (pgn.find("8/8/5K2/8/8/8/2N4p/7k") >=0 and tablas == "true")):
        print("TABLAS WIN1")
        #The number of moves that the user has made is saved
        mov = []

        if (list[-7] == "."):
            mov = list[-9] + list[-8]
        elif (list[-9] == "."):
            mov = list[-11] + list[-10]
        elif (list[-8] == "."):
            mov = list[-10] + list[-9]
        elif (list[-10] == "."):
            mov = list[-12] + list[-11]
        elif (list[-11] == "."):
            mov = list[-13] + list[-12]
        else:
            mov = list[-8] + list[-7]

        movI = int(mov)
        print("MOVi: ", movI)

    #If the user (the white pieces) has achieved stalemate in the Queen and King Vs Pawn and King
    #chess ending
    elif ((pgn.find("8/3pk3/8/8/8/1K6/8/2Q5") >=0 and resultado == "PovScore(Cp(0), BLACK)") or (pgn.find("5k2/4p3/8/8/8/8/8/2KQ4") >=0 and resultado == "PovScore(Cp(0), BLACK)") or (pgn.find("8/3pk3/8/8/8/8/5K2/2Q5") >=0 and resultado == "PovScore(Cp(0), BLACK)") or (pgn.find("8/1pk5/8/8/8/6K1/8/3Q4") >=0 and resultado == "PovScore(Cp(0), BLACK)") or (pgn.find("8/2pk4/8/8/8/8/6KQ/8") >=0 and resultado == "PovScore(Cp(0), BLACK)")):
        print("TABLAS WIN2")
        #The number of moves that the user has made is saved
        mov = []

        if (list[-6] == "."):
            mov = list[-8] + list[-7]
        elif (list[-7] == "."):
            mov = list[-9] + list[-8]
        else:
            mov = list[-7] + list[-6]

        movI = int(mov)
        print("MOVi: ", movI)

    #If the user (the white pieces) has not achieved the goal of the practical chess ending
    if(resultado=="PovScore(Mate(+1), BLACK)"):
        print("CHECKMATE GAME OVER")

    #The chess engine process is terminated
    engine.quit()

    #The following values ​​are returned to the "make_movePracticalChessEndings()" function,
    #the http POST request, of "practicalChessEnding.html"
    return {
        'fen': fen,
        'best_move': str(best_move),
        'score': str(info['score']),
        'depth': info['depth'],
        'pv': ' '.join([str(move) for move in info['pv']]),
        'nodes': info['nodes'],
        'time': info['time']
    }

#The option to play basic chess endings for registered users is displayed
@app.route('/basicChessEndingsRegisteredUser')
def basicChessEndingsRegisteredUser():
    return render_template('basicChessEndingsRegisteredUser.html')

#To make moves during the basic chess ending game and thus be able to establish
#a game between the user and the chess engine
@app.route('/make_moveBasicChessEndingsRegisteredUser', methods=['POST'])
def make_moveBasicChessEndingsRegisteredUser():

    #An instance of the chess engine is created
    engine = chess.engine.SimpleEngine.popen_uci('./engine/stockfish_13_win_x64.exe')

    #FEN is extracted
    fen = request.form.get('fen')
    #PGN is extracted
    pgn = request.form.get('pgn')
    #The gameover variable is extracted
    gameover = request.form.get('gameover')
    #The value of depth that has been set is extracted
    fixed_depth = request.form.get('fixed_depth')
    #The movement time value that has been set is extracted
    move_time = request.form.get('move_time')
    #List is created to save the PGN
    list = []

    #A chessboard instance is initialized
    board = chess.Board(fen)

    #If a move time is set
    if move_time != '0':
        #If it is an instant move time
        if move_time == 'instant':
            #Search for the best move instantly
            info = engine.analyse(board, chess.engine.Limit(time=0.1))
        #If it is not an instant move time
        else:
            #Search for the best move with a fixed move time
            info = engine.analyse(board, chess.engine.Limit(time=int(move_time)))

    #If a fixed depth is set
    if fixed_depth != '0':
        #Search for the best move with this fixed depth
        info = engine.analyse(board, chess.engine.Limit(depth=int(fixed_depth)))

    #The best move is extracted from info['pv']
    best_move = info['pv'][0]

    #Python chessboard internal state is updated
    board.push(best_move)

    #FEN is extracted from the current state of the board
    fen = board.fen()

    #The value of score is extracted from info to know the state of the game in each move
    resultado = str(info['score'])

    #The PGN of the game at that moment is saved in the list
    list = pgn

    #1) WIN KING AND ROOK VS KING CHESS ENDING

    #If the user (the white pieces) has won this basic chess ending
    if ((pgn.find("8/8/8/8/2k5/6R1/3K4/8") >=0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("8/8/8/8/4k3/8/8/R4K2") >=0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("8/8/8/4k3/8/8/8/R3K3") >=0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("8/8/8/3k4/R7/8/8/4K3") >=0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("8/8/8/3k4/R7/8/3K4/8") >= 0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("8/8/8/8/4k3/R7/8/5K2") >=0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("8/8/8/8/1k6/6R1/1K6/8") >=0 and resultado == "PovScore(Mate(+1), WHITE)")) :
        #The name of the chess ending is saved
        nombrefinal = "Final_Torre_Y_Rey_Vs_Rey"
        #The username is saved
        user = session.get('username')
        #The date is saved
        today = date.today()
        #The date is saved in string type
        today_str = today.strftime('%d-%m-%Y')
        print("YOU WON" + nombrefinal + user)

        #The number of moves that the user has made is saved
        mov = []

        if (list[-10] == "."):
            mov = list[-12] + list[-11]
        else:
            mov = list[-11] + list[-10]

        movI = int(mov)
        movIF = movI + 1
        print("MOVif ", movIF)


        cursor = connection.cursor()
        #The "SQL" statement called 'SELECT' is declared to select information
        cursor.execute('SELECT * FROM finals WHERE USERNAME = "'+user+'" AND FINAL="'+nombrefinal+'" AND FECHA = "'+today_str+'"')
        rows = cursor.fetchall()
        results = len(rows)


        #If the user has already played that basic chess ending
        if results > 0:
            print('There is the username, the date and the name of the chess ending')

            #1) The number of times the user achieves the goal of the basic chess ending is taken

            #The "SQL" statement called 'SELECT' is declared to select information
            cursor.execute('SELECT WIN FROM finals where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            win=cursor.fetchone()[0]
            winI = int(win)
            winF = winI + 1

            #The value of win is saved in a session variable
            session['win "'+user+'""'+nombrefinal+'"'] = winF
            winn = session.get('win "'+user+'""'+nombrefinal+'"')
            winS = str(winn)

            #2) The new value of the number of times the user achieves the goal of the basic chess ending
            #is updated
            cursor.execute('UPDATE finals set WIN ="'+winS+'" where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            connection.commit()

            #3) The number of moves that the user has used to achieve the goal of the basic chess ending
            #is inserted into the database

            # The value of moves is saved in a session variable
            session['movimientos "'+user+'""'+nombrefinal+'"'] = movIF
            movimiento = session.get('movimientos "'+user+'""'+nombrefinal+'"')
            movimientoS = str(movimiento)

            #The "SQL" statement called 'INSERT' is declared to insert information
            cursor.execute('INSERT INTO nummovi(username, final, movimientos, fecha) VALUES(%s, %s, %s, %s)',(user, nombrefinal, movimientoS,today_str))
            connection.commit()

            #The cursor closes
            cursor.close()

        #If this is the first time the user has played that basic chess ending
        else:
            print('There is no such combination')
            #The value of win is saved in a session variable
            session['win "'+user+'""'+nombrefinal+'"'] = 1
            win = session.get('win "'+user+'""'+nombrefinal+'"')
            winS = str(win)

            #The value of lose is saved in a session variable
            session['lose "'+user+'""'+nombrefinal+'"'] = 0
            lose = session.get('lose "'+user+'""'+nombrefinal+'"')
            loseS = str(lose)

            #1) The new values ​​of: the number of times that the user achieves the goal of the basic
            #chess ending and the number of times that the user does not achieve that goal, are inserted
            cursor = connection.cursor()

            #The "SQL" statement called 'INSERT' is declared to insert information
            cursor.execute('INSERT INTO finals(username, final, win, lose, fecha) VALUES(%s, %s, %s, %s, %s)',(user, nombrefinal, winS, loseS, today_str))
            connection.commit()

            #2) The number of moves that the user has used to achieve the goal of the basic chess ending
            #is inserted into the database

            #The value of moves is saved in a session variable
            session['movimientos "'+user+'""'+nombrefinal+'"'] = movIF
            movimiento = session.get('movimientos "'+user+'""'+nombrefinal+'"')
            movimientoS = str(movimiento)

            #The "SQL" statement called 'INSERT' is declared to insert information
            cursor.execute('INSERT INTO nummovi(username, final, movimientos, fecha) VALUES(%s, %s, %s, %s)',(user, nombrefinal, movimientoS, today_str))
            connection.commit()

            #The cursor closes
            cursor.close()

    #Once the procedure that has been developed for when the user has achieved the objective of the
    #rook and king vs king chess ending, has been explained, it will be applied
    #to the rest of the basic chess endings with some variation in terms of the end name
    #that is concerned in each case


    #2) WIN BISHOPS AND ROOK VS KING CHESS ENDING
    elif ((pgn.find("8/8/8/3k4/8/8/8/2B1KB2") >=0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("8/8/4k3/8/3BB3/8/8/K7") >=0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("8/8/3k4/8/2K5/3BB3/8/8") >=0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("8/8/3k4/8/2KB4/3B4/8/8") >=0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("3k4/5B2/2KB4/8/8/8/8/8") >= 0 and resultado == "PovScore(Mate(+1), WHITE)")) :
        nombrefinal = "Final_Alfiles_Y_Rey_Vs_Rey"
        user = session.get('username')
        today = date.today()
        today_str = today.strftime('%d-%m-%Y')
        print("YOU WON" + nombrefinal + user)

        mov = []

        if (list[-10] == "."):
            mov = list[-12] + list[-11]
        else:
            mov = list[-11] + list[-10]

        movI = int(mov)
        movIF = movI + 1
        print("MOVif ", movIF)


        cursor2 = connection.cursor()
        cursor2.execute('SELECT * FROM finals WHERE USERNAME = "'+user+'" AND FINAL="'+nombrefinal+'" AND FECHA = "'+today_str+'"')
        rows = cursor2.fetchall()
        results = len(rows)

        if results > 0:
            print('There is the username, the date and the name of the chess ending')

            cursor2.execute('SELECT WIN FROM finals where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            win=cursor2.fetchone()[0]
            winI = int(win)
            winF = winI + 1
            session['win "'+user+'""'+nombrefinal+'"'] = winF
            winn = session.get('win "'+user+'""'+nombrefinal+'"')
            winS = str(winn)


            cursor2.execute('UPDATE finals set WIN ="'+winS+'" where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            connection.commit()

            session['movimientos "'+user+'""'+nombrefinal+'"'] = movIF
            movimiento = session.get('movimientos "'+user+'""'+nombrefinal+'"')
            movimientoS = str(movimiento)


            cursor2.execute('INSERT INTO nummovi(username, final, movimientos, fecha) VALUES(%s, %s, %s, %s)',(user, nombrefinal, movimientoS,today_str))
            connection.commit()

            cursor2.close()

        else:
            print('There is no such combination')

            session['win "'+user+'""'+nombrefinal+'"'] = 1
            win = session.get('win "'+user+'""'+nombrefinal+'"')
            winS = str(win)

            session['lose "'+user+'""'+nombrefinal+'"'] = 0
            lose = session.get('lose "'+user+'""'+nombrefinal+'"')
            loseS = str(lose)


            cursor2 = connection.cursor()
            cursor2.execute('INSERT INTO finals(username, final, win, lose, fecha) VALUES(%s, %s, %s, %s, %s)',(user, nombrefinal, winS, loseS, today_str))
            connection.commit()


            session['movimientos "'+user+'""'+nombrefinal+'"'] = movIF
            movimiento = session.get('movimientos "'+user+'""'+nombrefinal+'"')
            movimientoS = str(movimiento)

            cursor2.execute('INSERT INTO nummovi(username, final, movimientos, fecha) VALUES(%s, %s, %s, %s)',(user, nombrefinal, movimientoS, today_str))
            connection.commit()

            cursor2.close()

    #3) WIN QUEEN AND KING VS KING CHESS ENDING
    if ((pgn.find("8/8/8/8/4k3/8/8/Q3K3") >=0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("8/8/8/8/4k3/2Q5/8/4K3") >=0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("8/8/8/3k4/8/2Q5/8/4K3") >=0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("8/1k6/8/2Q5/8/8/8/4K3") >=0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("1k6/4Q3/8/8/8/8/8/4K3") >= 0 and resultado == "PovScore(Mate(+1), WHITE)")):
        nombrefinal = "Final_Dama_Y_Rey_Vs_Rey"
        user = session.get('username')
        today = date.today()
        today_str = today.strftime('%d-%m-%Y')
        print("YOU WON" + nombrefinal + user)

        mov = []

        if (list[-10] == "."):
            mov = list[-12] + list[-11]
        else:
            mov = list[-11] + list[-10]

        movI = int(mov)
        movIF = movI + 1
        print("MOVif ", movIF)


        cursor = connection.cursor()
        cursor.execute('SELECT * FROM finals WHERE USERNAME = "'+user+'" AND FINAL="'+nombrefinal+'" AND FECHA = "'+today_str+'"')
        rows = cursor.fetchall()
        results = len(rows)

        if results > 0:
            print('There is the username, the date and the name of the chess ending')
            cursor.execute('SELECT WIN FROM finals where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            win=cursor.fetchone()[0]
            winI = int(win)
            winF = winI + 1
            session['win "'+user+'""'+nombrefinal+'"'] = winF
            winn = session.get('win "'+user+'""'+nombrefinal+'"')
            winS = str(winn)

            cursor.execute('UPDATE finals set WIN ="'+winS+'" where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            connection.commit()

            session['movimientos "'+user+'""'+nombrefinal+'"'] = movIF
            movimiento = session.get('movimientos "'+user+'""'+nombrefinal+'"')
            movimientoS = str(movimiento)

            cursor.execute('INSERT INTO nummovi(username, final, movimientos, fecha) VALUES(%s, %s, %s, %s)',(user, nombrefinal, movimientoS,today_str))
            connection.commit()

            cursor.close()

        else:
            print('There is no such combination')
            session['win "'+user+'""'+nombrefinal+'"'] = 1
            win = session.get('win "'+user+'""'+nombrefinal+'"')
            winS = str(win)

            session['lose "'+user+'""'+nombrefinal+'"'] = 0
            lose = session.get('lose "'+user+'""'+nombrefinal+'"')
            loseS = str(lose)

            cursor = connection.cursor()
            cursor.execute('INSERT INTO finals(username, final, win, lose, fecha) VALUES(%s, %s, %s, %s, %s)',(user, nombrefinal, winS, loseS, today_str))
            connection.commit()

            session['movimientos "'+user+'""'+nombrefinal+'"'] = movIF
            movimiento = session.get('movimientos "'+user+'""'+nombrefinal+'"')
            movimientoS = str(movimiento)

            cursor.execute('INSERT INTO nummovi(username, final, movimientos, fecha) VALUES(%s, %s, %s, %s)',(user, nombrefinal, movimientoS, today_str))
            connection.commit()

            cursor.close()

    #4) WIN BISHOP, KNIGHT AND KING VS KING CHESS ENDING
    if ((pgn.find("k7/8/2K5/3N4/5B2/8/8/8") >=0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("1B6/8/kNK5/8/8/8/8/8") >=0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("1B6/8/8/2KN4/k7/8/8/8") >=0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("8/8/8/2K5/1N3B2/2k5/8/8") >= 0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("8/8/1B6/8/8/k1K5/1N6/8") >=0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("8/8/1B6/8/8/k7/1NK5/8") >=0 and resultado == "PovScore(Mate(+1), WHITE)")):
        nombrefinal = "Final_Alfil_Caballo_Y_Rey_Vs_Rey"
        user = session.get('username')
        today = date.today()
        today_str = today.strftime('%d-%m-%Y')
        print("YOU WON" + nombrefinal + user)

        mov = []

        if (list[-10] == "."):
            mov = list[-12] + list[-11]
        else:
            mov = list[-11] + list[-10]

        movI = int(mov)
        movIF = movI + 1
        print("MOVif ", movIF)

        cursor = connection.cursor()
        cursor.execute('SELECT * FROM finals WHERE USERNAME = "'+user+'" AND FINAL="'+nombrefinal+'" AND FECHA = "'+today_str+'"')
        rows = cursor.fetchall()
        results = len(rows)

        if results > 0:
            print('There is the username, the date and the name of the chess ending')
            cursor.execute('SELECT WIN FROM finals where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            win=cursor.fetchone()[0]
            winI = int(win)
            winF = winI + 1
            session['win "'+user+'""'+nombrefinal+'"'] = winF
            winn = session.get('win "'+user+'""'+nombrefinal+'"')
            winS = str(winn)


            cursor.execute('UPDATE finals set WIN ="'+winS+'" where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            connection.commit()

            session['movimientos "'+user+'""'+nombrefinal+'"'] = movIF
            movimiento = session.get('movimientos "'+user+'""'+nombrefinal+'"')
            movimientoS = str(movimiento)

            cursor.execute('INSERT INTO nummovi(username, final, movimientos, fecha) VALUES(%s, %s, %s, %s)',(user, nombrefinal, movimientoS,today_str))
            connection.commit()

            cursor.close()

        else:
            print('There is no such combination')
            session['win "'+user+'""'+nombrefinal+'"'] = 1
            win = session.get('win "'+user+'""'+nombrefinal+'"')
            winS = str(win)

            session['lose "'+user+'""'+nombrefinal+'"'] = 0
            lose = session.get('lose "'+user+'""'+nombrefinal+'"')
            loseS = str(lose)

            cursor = connection.cursor()
            cursor.execute('INSERT INTO finals(username, final, win, lose, fecha) VALUES(%s, %s, %s, %s, %s)',(user, nombrefinal, winS, loseS, today_str))
            connection.commit()

            session['movimientos "'+user+'""'+nombrefinal+'"'] = movIF
            movimiento = session.get('movimientos "'+user+'""'+nombrefinal+'"')
            movimientoS = str(movimiento)

            cursor.execute('INSERT INTO nummovi(username, final, movimientos, fecha) VALUES(%s, %s, %s, %s)',(user, nombrefinal, movimientoS, today_str))
            connection.commit()

            cursor.close()

    #5) WIN ROOKS AND KING VS KING CHESS ENDING
    if ((pgn.find("8/8/8/8/4k3/8/8/R3K2R") >=0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("8/8/8/6k1/1R6/R7/8/4K3") >=0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("2k5/R7/1R6/8/8/8/8/4K3") >= 0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("8/8/8/6k1/R6R/8/8/4k3") >=0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("8/8/8/5k2/R6R/8/8/4k3") >=0 and resultado == "PovScore(Mate(+1), WHITE)")) :
        nombrefinal = "Final_Torres_Y_Rey_Vs_Rey"
        user = session.get('username')
        today = date.today()
        today_str = today.strftime('%d-%m-%Y')
        print("YOU WON" + nombrefinal + user)

        mov = []

        if (list[-10] == "."):
            mov = list[-12] + list[-11]
        else:
            mov = list[-11] + list[-10]

        movI = int(mov)
        movIF = movI + 1
        print("MOVif ", movIF)

        cursor = connection.cursor()
        cursor.execute('SELECT * FROM finals WHERE USERNAME = "'+user+'" AND FINAL="'+nombrefinal+'" AND FECHA = "'+today_str+'"')
        rows = cursor.fetchall()
        results = len(rows)

        if results > 0:
            print('There is the username, the date and the name of the chess ending')
            cursor.execute('SELECT WIN FROM finals where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            win=cursor.fetchone()[0]
            winI = int(win)
            winF = winI + 1
            session['win "'+user+'""'+nombrefinal+'"'] = winF
            winn = session.get('win "'+user+'""'+nombrefinal+'"')
            winS = str(winn)

            cursor.execute('UPDATE finals set WIN ="'+winS+'" where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            connection.commit()

            session['movimientos "'+user+'""'+nombrefinal+'"'] = movIF
            movimiento = session.get('movimientos "'+user+'""'+nombrefinal+'"')
            movimientoS = str(movimiento)


            cursor.execute('INSERT INTO nummovi(username, final, movimientos, fecha) VALUES(%s, %s, %s, %s)',(user, nombrefinal, movimientoS,today_str))
            connection.commit()

            cursor.close()

        else:
            print('There is no such combination')
            session['win "'+user+'""'+nombrefinal+'"'] = 1
            win = session.get('win "'+user+'""'+nombrefinal+'"')
            winS = str(win)

            session['lose "'+user+'""'+nombrefinal+'"'] = 0
            lose = session.get('lose "'+user+'""'+nombrefinal+'"')
            loseS = str(lose)

            cursor = connection.cursor()
            cursor.execute('INSERT INTO finals(username, final, win, lose, fecha) VALUES(%s, %s, %s, %s, %s)',(user, nombrefinal, winS, loseS, today_str))
            connection.commit()

            session['movimientos "'+user+'""'+nombrefinal+'"'] = movIF
            movimiento = session.get('movimientos "'+user+'""'+nombrefinal+'"')
            movimientoS = str(movimiento)

            cursor.execute('INSERT INTO nummovi(username, final, movimientos, fecha) VALUES(%s, %s, %s, %s)',(user, nombrefinal, movimientoS, today_str))
            connection.commit()

            cursor.close()


    #1) LOSE ROOK AND KING VS KING CHESS ENDING

    #If the user (the white pieces) has lost this basic chess ending
    elif ((pgn.find("8/8/8/8/2k5/6R1/3K4/8") >=0 and gameover == "true") or (pgn.find("8/8/8/8/4k3/8/8/R4K2") >=0 and gameover == "true") or (pgn.find("8/8/8/4k3/8/8/8/R3K3") >=0 and gameover == "true") or (pgn.find("8/8/8/3k4/R7/8/8/4K3") >=0 and gameover == "true") or (pgn.find("8/8/8/3k4/R7/8/3K4/8") >= 0 and gameover == "true") or (pgn.find("8/8/8/8/4k3/R7/8/5K2") >=0 and gameover == "true") or (pgn.find("8/8/8/8/1k6/6R1/1K6/8") >=0 and gameover == "true")) :
        #The name of the chess ending is saved
        nombrefinal = "Final_Torre_Y_Rey_Vs_Rey"
        #The username is saved
        user = session.get('username')
        #The date is saved
        today = date.today()
        #The date is saved in string type
        today_str = today.strftime('%d-%m-%Y')
        print("YOU LOSE" + nombrefinal + user)

        cursor = connection.cursor()
        #The "SQL" statement called 'SELECT' is declared to select information
        cursor.execute('SELECT * FROM finals WHERE USERNAME = "'+user+'" AND FINAL="'+nombrefinal+'" AND FECHA = "'+today_str+'"')
        rows = cursor.fetchall()
        results = len(rows)

        #If the user has already played that basic chess ending
        if results > 0:
            print('There is the username, the date and the name of the chess ending')

            #1) The number of times the user doesn't achieves the goal of the basic chess ending is taken

            #The "SQL" statement called 'SELECT' is declared to select information
            cursor.execute('SELECT LOSE FROM finals where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            lose=cursor.fetchone()[0]
            loseI = int(lose)
            loseF = loseI + 1

            #The value of lose is saved in a session variable
            session['lose "'+user+'""'+nombrefinal+'"'] = loseF
            losee = session.get('lose "'+user+'""'+nombrefinal+'"')
            loseS = str(losee)

            #2) The new value of the number of times the user doesn't achieve the goal of the
            #basic chess ending is updated
            cursor.execute('UPDATE finals set LOSE ="'+loseS+'" where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            connection.commit()

            #The cursor closes
            cursor.close()

        #If this is the first time the user has played that basic chess ending
        else:
            print('There is no such combination')
            #The value of win is saved in a session variable
            session['win "'+user+'""'+nombrefinal+'"'] = 0
            win = session.get('win "'+user+'""'+nombrefinal+'"')
            winS = str(win)

            #The value of lose is saved in a session variable
            session['lose "'+user+'""'+nombrefinal+'"'] = 1
            lose = session.get('lose "'+user+'""'+nombrefinal+'"')
            loseS = str(lose)

            #1) The new values ​​of: the number of times that the user achieves the goal of the basic
            #chess ending and the number of times that the user does not achieve that goal, are inserted
            cursor = connection.cursor()

            #The "SQL" statement called 'INSERT' is declared to insert information
            cursor.execute('INSERT INTO finals(username, final, win, lose, fecha) VALUES(%s, %s, %s, %s, %s)',(user, nombrefinal, winS, loseS, today_str))
            connection.commit()

            #The cursor closes
            cursor.close()

        #Once the procedure that has been developed for when the user hasn't achieved the objective of the
        #rook and king vs king chess ending, has been explained, it will be applied
        #to the rest of the basic chess endings with some variation in terms of the end name that is concerned in each case


    #2) LOSE BISHOPS AND KING VS KING CHESS ENDING
    elif ((pgn.find("8/8/8/3k4/8/8/8/2B1KB2") >=0 and gameover == "true") or (pgn.find("8/8/4k3/8/3BB3/8/8/K7") >=0 and gameover == "true") or (pgn.find("8/8/3k4/8/2K5/3BB3/8/8") >=0 and gameover == "true") or (pgn.find("8/8/3k4/8/2KB4/3B4/8/8") >=0 and gameover == "true") or (pgn.find("3k4/5B2/2KB4/8/8/8/8/8") >= 0 and gameover == "true")) :
        nombrefinal = "Final_Alfiles_Y_Rey_Vs_Rey"
        user = session.get('username')
        today = date.today()
        today_str = today.strftime('%d-%m-%Y')
        print("YOU LOSE " + nombrefinal + user)

        cursor2 = connection.cursor()
        cursor2.execute('SELECT * FROM finals WHERE USERNAME = "'+user+'" AND FINAL="'+nombrefinal+'" AND FECHA = "'+today_str+'"')
        rows = cursor2.fetchall()
        results = len(rows)

        if results > 0:
            print('There is the username, the date and the name of the chess ending')
            cursor2.execute('SELECT LOSE FROM finals where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            lose=cursor2.fetchone()[0]
            loseI = int(lose)
            loseF = loseI + 1
            session['lose "'+user+'""'+nombrefinal+'"'] = loseF
            losee = session.get('lose "'+user+'""'+nombrefinal+'"')
            loseS = str(losee)

            cursor2.execute('UPDATE finals set LOSE ="'+loseS+'" where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            connection.commit()

            cursor2.close()

        else:
            print('There is no such combination')
            session['win "'+user+'""'+nombrefinal+'"'] = 0
            win = session.get('win "'+user+'""'+nombrefinal+'"')
            winS = str(win)

            session['lose "'+user+'""'+nombrefinal+'"'] = 1
            lose = session.get('lose "'+user+'""'+nombrefinal+'"')
            loseS = str(lose)

            cursor2 = connection.cursor()
            cursor2.execute('INSERT INTO finals(username, final, win, lose, fecha) VALUES(%s, %s, %s, %s, %s)',(user, nombrefinal, winS, loseS, today_str))
            connection.commit()

            cursor2.close()

    #3) LOSE QUEEN AND KING VS KING CHESS ENDING
    elif ((pgn.find("8/8/8/8/4k3/8/8/Q3K3") >=0 and gameover == "true") or (pgn.find("8/8/8/8/4k3/2Q5/8/4K3") >=0 and gameover == "true") or (pgn.find("8/8/8/3k4/8/2Q5/8/4K3") >=0 and gameover == "true") or (pgn.find("8/1k6/8/2Q5/8/8/8/4K3") >=0 and gameover == "true") or (pgn.find("1k6/4Q3/8/8/8/8/8/4K3") >= 0 and gameover == "true")):
        nombrefinal = "Final_Dama_Y_Rey_Vs_Rey"
        user = session.get('username')
        today = date.today()
        today_str = today.strftime('%d-%m-%Y')
        print("YOU LOSE" + nombrefinal + user)

        cursor = connection.cursor()
        cursor.execute('SELECT * FROM finals WHERE USERNAME = "'+user+'" AND FINAL="'+nombrefinal+'" AND FECHA = "'+today_str+'"')
        rows = cursor.fetchall()
        results = len(rows)

        if results > 0:
            print('There is the username, the date and the name of the chess ending')

            cursor.execute('SELECT LOSE FROM finals where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            lose=cursor.fetchone()[0]
            loseI = int(lose)
            loseF = loseI + 1
            session['lose "'+user+'""'+nombrefinal+'"'] = loseF
            losee = session.get('lose "'+user+'""'+nombrefinal+'"')
            loseS = str(losee)

            cursor.execute('UPDATE finals set LOSE ="'+loseS+'" where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            connection.commit()

            cursor.close()

        else:
            print('There is no such combination')
            session['win "'+user+'""'+nombrefinal+'"'] = 0
            win = session.get('win "'+user+'""'+nombrefinal+'"')
            winS = str(win)

            session['lose "'+user+'""'+nombrefinal+'"'] = 1
            lose = session.get('lose "'+user+'""'+nombrefinal+'"')
            loseS = str(lose)

            cursor = connection.cursor()
            cursor.execute('INSERT INTO finals(username, final, win, lose, fecha) VALUES(%s, %s, %s, %s, %s)',(user, nombrefinal, winS, loseS, today_str))
            connection.commit()

            cursor.close()

    #4) LOSE BISHOP, KNIGHT AND KING VS KING CHESS ENDING
    elif ((pgn.find("k7/8/2K5/3N4/5B2/8/8/8") >=0 and gameover == "true") or (pgn.find("1B6/8/kNK5/8/8/8/8/8") >=0 and gameover == "true") or (pgn.find("1B6/8/8/2KN4/k7/8/8/8") >=0 and gameover == "true") or (pgn.find("8/8/8/2K5/1N3B2/2k5/8/8") >= 0 and gameover == "true") or (pgn.find("8/8/1B6/8/8/k1K5/1N6/8") >=0 and gameover == "true") or (pgn.find("8/8/1B6/8/8/k7/1NK5/8") >=0 and gameover == "true")) :
        nombrefinal = "Final_Alfil_Caballo_Y_Rey_Vs_Rey"
        user = session.get('username')
        today = date.today()
        today_str = today.strftime('%d-%m-%Y')
        print("YOU LOSE" + nombrefinal + user)

        cursor = connection.cursor()
        cursor.execute('SELECT * FROM finals WHERE USERNAME = "'+user+'" AND FINAL="'+nombrefinal+'" AND FECHA = "'+today_str+'"')
        rows = cursor.fetchall()
        results = len(rows)

        if results > 0:
            print('There is the username, the date and the name of the chess ending')

            cursor.execute('SELECT LOSE FROM finals where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            lose=cursor.fetchone()[0]
            loseI = int(lose)
            loseF = loseI + 1
            session['lose "'+user+'""'+nombrefinal+'"'] = loseF
            losee = session.get('lose "'+user+'""'+nombrefinal+'"')
            loseS = str(losee)

            cursor.execute('UPDATE finals set LOSE ="'+loseS+'" where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            connection.commit()

            cursor.close()

        else:
            print('There is no such combination')
            session['win "'+user+'""'+nombrefinal+'"'] = 0
            win = session.get('win "'+user+'""'+nombrefinal+'"')
            winS = str(win)

            session['lose "'+user+'""'+nombrefinal+'"'] = 1
            lose = session.get('lose "'+user+'""'+nombrefinal+'"')
            loseS = str(lose)

            cursor = connection.cursor()
            cursor.execute('INSERT INTO finals(username, final, win, lose, fecha) VALUES(%s, %s, %s, %s, %s)',(user, nombrefinal, winS, loseS, today_str))
            connection.commit()

            cursor.close()

    #5) LOSE ROOKS AND KING VS KING
    elif ((pgn.find("8/8/8/8/4k3/8/8/R3K2R") >=0 and gameover == "true") or (pgn.find("8/8/8/6k1/1R6/R7/8/4K3") >=0 and gameover == "true") or (pgn.find("2k5/R7/1R6/8/8/8/8/4K3") >= 0 and gameover == "true") or (pgn.find("8/8/8/6k1/R6R/8/8/4k3") >=0 and gameover == "true") or (pgn.find("8/8/8/5k2/R6R/8/8/4k3") >=0 and gameover == "true")) :
        nombrefinal = "Final_Torres_Y_Rey_Vs_Rey"
        user = session.get('username')
        today = date.today()
        today_str = today.strftime('%d-%m-%Y')
        print("YOU LOSE" + nombrefinal + user)

        cursor = connection.cursor()
        cursor.execute('SELECT * FROM finals WHERE USERNAME = "'+user+'" AND FINAL="'+nombrefinal+'" AND FECHA = "'+today_str+'"')
        rows = cursor.fetchall()
        results = len(rows)

        if results > 0:
            print('There is the username, the date and the name of the chess ending')

            cursor.execute('SELECT LOSE FROM finals where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            lose=cursor.fetchone()[0]
            loseI = int(lose)
            loseF = loseI + 1
            session['lose "'+user+'""'+nombrefinal+'"'] = loseF
            losee = session.get('lose "'+user+'""'+nombrefinal+'"')
            loseS = str(losee)

            cursor.execute('UPDATE finals set LOSE ="'+loseS+'" where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            connection.commit()

            cursor.close()

        else:
            print('There is no such combination')
            session['win "'+user+'""'+nombrefinal+'"'] = 0
            win = session.get('win "'+user+'""'+nombrefinal+'"')
            winS = str(win)

            session['lose "'+user+'""'+nombrefinal+'"'] = 1
            lose = session.get('lose "'+user+'""'+nombrefinal+'"')
            loseS = str(lose)

            cursor = connection.cursor()
            cursor.execute('INSERT INTO finals(username, final, win, lose, fecha) VALUES(%s, %s, %s, %s, %s)',(user, nombrefinal, winS, loseS, today_str))
            connection.commit()

            cursor.close()

    #The chess engine process is terminated
    engine.quit()

    #The following values ​​are returned to the "make_moveBasicChessEndingsRegisteredUser()" function,
    #the http POST request, of "basicChessEndingRegisteredUser.html"
    return {
        'fen': fen,
        'best_move': str(best_move),
        'score': str(info['score']),
        'depth': info['depth'],
        'pv': ' '.join([str(move) for move in info['pv']]),
        'nodes': info['nodes'],
        'time': info['time']
    }

#The option to play Practical chess endings for registered users is displayed
@app.route('/practicalChessEndingRegisteredUser')
def practicalChessEndingRegisteredUser():
    return render_template('practicalChessEndingRegisteredUser.html')

#To make moves during the practical chess ending game and thus be able to establish
#a game between the user and the chess engine
@app.route('/make_movePracticalChessEndingsRegisteredUser', methods=['POST'])
def make_movePracticalChessEndingsRegisteredUser():

    #An instance of the chess engine is created
    engine = chess.engine.SimpleEngine.popen_uci('./engine/stockfish_13_win_x64.exe')

    #FEN is extracted
    fen = request.form.get('fen')
    #PGN is extracted
    pgn = request.form.get('pgn')
    #The gameover variable is extracted
    gameover = request.form.get('gameover')
    #The tablas variable is extracted
    tablas = request.form.get('tablas')
    #The value of depth that has been set is extracted
    fixed_depth = request.form.get('fixed_depth')
    #The movement time value that has been set is extracted
    move_time = request.form.get('move_time')
    #List is created to save the PGN
    list = []

    #A chessboard instance is initialized
    board = chess.Board(fen)

    #If a move time is set
    if move_time != '0':
        #If it is an instant move time
        if move_time == 'instant':
            #Search for the best move instantly
            info = engine.analyse(board, chess.engine.Limit(time=0.1))
        #If it is not an instant move time
        else:
            #Search for the best move with a fixed move time
            info = engine.analyse(board, chess.engine.Limit(time=int(move_time)))

    #If a fixed depth is set
    if fixed_depth != '0':
        #Search for the best move with this fixed depth
        info = engine.analyse(board, chess.engine.Limit(depth=int(fixed_depth)))

    #The best movement is extracted from info['pv']
    best_move = info['pv'][0]

    #Python chessboard internal state is updated
    board.push(best_move)

    #FEN is extracted from the current state of the board
    fen = board.fen()

    #The value of score is extracted from info to know the state of the game in each move
    resultado = str(info['score'])

    #The PGN of the game at that moment is saved in the list
    list = pgn

    #1) WIN KNIGHT AND KING VS PAWN AND KING CHESS ENDING

    #If the user (the white pieces) has won this practical chess ending
    if ((pgn.find("8/8/8/8/8/4N2p/5K1k/8") >=0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("8/8/8/8/8/p7/3N4/k1K5") >=0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("8/8/5K2/8/8/8/4N2p/7k") >=0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("8/8/5K2/8/8/8/7p/4N2k") >=0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("8/8/5K2/8/8/8/6Np/7k") >= 0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("8/8/5K2/8/8/8/2N4p/7k") >=0 and resultado == "PovScore(Mate(+1), WHITE)")) :

        #The name of the chess ending is saved
        nombrefinal = "Final_Caballo_Y_Rey_Vs_Peon_Y_Rey"
        #The username is saved
        user = session.get('username')
        #The date is saved
        today = date.today()
        #The date is saved in string type
        today_str = today.strftime('%d-%m-%Y')
        print("YOU WON" + nombrefinal + user)

        #The number of moves that the user has made is saved
        mov = []
        if (list[-9] == "."):
            mov = list[-11] + list[-10]
        else:
            mov = list[-10] + list[-9]

        movI = int(mov)
        movIF = movI + 1
        print("MOVif ", movIF)

        cursor = connection.cursor()
        #The "SQL" statement called 'SELECT' is declared to select information
        cursor.execute('SELECT * FROM finals WHERE USERNAME = "'+user+'" AND FINAL="'+nombrefinal+'" AND FECHA = "'+today_str+'"')
        rows = cursor.fetchall()
        results = len(rows)

        #If the user has already played that practical chess ending
        if results > 0:
            print('There is the username, the date and the name of the chess ending')

            #1) The number of times the user achieves the goal of the practical chess ending is taken

            #The "SQL" statement called 'SELECT' is declared to select information
            cursor.execute('SELECT WIN FROM finals where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            win=cursor.fetchone()[0]
            winI = int(win)
            winF = winI + 1

            #The value of win is saved in a session variable
            session['win "'+user+'""'+nombrefinal+'"'] = winF
            winn = session.get('win "'+user+'""'+nombrefinal+'"')
            winS = str(winn)

            #2) The new value of the number of times the user achieves the goal of the practical
            #chess ending is updated
            cursor.execute('UPDATE finals set WIN ="'+winS+'" where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            connection.commit()

            #3) The number of moves that the user has used to achieve the goal of the practical chess ending
            #is inserted into the database

            #The value of moves is saved in a session variable
            session['movimientos "'+user+'""'+nombrefinal+'"'] = movIF
            movimiento = session.get('movimientos "'+user+'""'+nombrefinal+'"')
            movimientoS = str(movimiento)

            #The "SQL" statement called 'INSERT' is declared to insert information
            cursor.execute('INSERT INTO nummovi(username, final, movimientos, fecha) VALUES(%s, %s, %s, %s)',(user, nombrefinal, movimientoS,today_str))
            connection.commit()

            #The cursor closes
            cursor.close()

        #If this is the first time the user has played that practical chess ending
        else:
            print('There is no such combination')
            #The value of win is saved in a session variable
            session['win "'+user+'""'+nombrefinal+'"'] = 1
            win = session.get('win "'+user+'""'+nombrefinal+'"')
            winS = str(win)

            #The value of lose is saved in a session variable
            session['lose "'+user+'""'+nombrefinal+'"'] = 0
            lose = session.get('lose "'+user+'""'+nombrefinal+'"')
            loseS = str(lose)

            #1) The new values ​​of: the number of times that the user achieves the goal of the practical
            #chess ending and the number of times that the user does not achieve that goal, are inserted
            cursor = connection.cursor()

            #The "SQL" statement called 'INSERT' is declared to insert information
            cursor.execute('INSERT INTO finals(username, final, win, lose, fecha) VALUES(%s, %s, %s, %s, %s)',(user, nombrefinal, winS, loseS, today_str))
            connection.commit()

            #2) The number of moves that the user has used to achieve the goal of the practical
            #chess ending is inserted into the database

            #The value of moves is saved in a session variable
            session['movimientos "'+user+'""'+nombrefinal+'"'] = movIF
            movimiento = session.get('movimientos "'+user+'""'+nombrefinal+'"')
            movimientoS = str(movimiento)

            #The "SQL" statement called 'INSERT' is declared to insert information
            cursor.execute('INSERT INTO nummovi(username, final, movimientos, fecha) VALUES(%s, %s, %s, %s)',(user, nombrefinal, movimientoS,today_str))
            connection.commit()

            #The cursor closes
            cursor.close()

    #Once the procedure that has been developed for when the user has achieved the objective of the
    #knight and king vs pawn and king chess ending, has been explained, it will be applied
    #to the rest of the practical chess endings with some variation
    #in terms of the end name that is concerned in each case.


    #1) GET DRAW IN THE KNIGHT AND KING VS PAWN AND KING CHESS ENDING

    #If the user (the white pieces) has achieved stalemate in the practical chess ending
    elif ((pgn.find("8/8/8/8/8/4N2p/5K1k/8") >=0 and tablas == "true") or (pgn.find("8/8/8/8/8/p7/3N4/k1K5") >=0 and tablas == "true") or (pgn.find("8/8/5K2/8/8/8/4N2p/7k") >=0 and tablas == "true") or (pgn.find("8/8/5K2/8/8/8/7p/4N2k") >=0 and tablas == "true") or (pgn.find("8/8/5K2/8/8/8/6Np/7k") >= 0 and tablas == "true") or (pgn.find("8/8/5K2/8/8/8/2N4p/7k") >=0 and tablas == "true")):

        #The name of the chess ending is saved
        nombrefinal = "Final_Caballo_Y_Rey_Vs_Peon_Y_Rey"
        #The username is saved
        user = session.get('username')
        #The date is saved
        today = date.today()
        #The date is saved in string type
        today_str = today.strftime('%d-%m-%Y')
        print("YOU WON" + nombrefinal + user)

        #The number of moves that the user has made is saved
        mov = []

        if (list[-7] == "."):
            mov = list[-9] + list[-8]
        elif (list[-9] == "."):
            mov = list[-11] + list[-10]
        elif (list[-8] == "."):
            mov = list[-10] + list[-9]
        elif (list[-10] == "."):
            mov = list[-12] + list[-11]
        elif (list[-11] == "."):
            mov = list[-13] + list[-12]
        else:
            mov = list[-8] + list[-7]

        movI = int(mov)
        print("MOVi: ", movI)

        cursor = connection.cursor()
        #The "SQL" statement called 'SELECT' is declared to select information
        cursor.execute('SELECT * FROM finals WHERE USERNAME = "'+user+'" AND FINAL="'+nombrefinal+'" AND FECHA = "'+today_str+'"')
        rows = cursor.fetchall()
        results = len(rows)

        #If the user has already played that practical chess ending
        if results > 0:
            print('There is the username, the date and the name of the chess ending')

            #1) The number of times the user achieves the goal of the practical chess ending is taken

            #The "SQL" statement called 'SELECT' is declared to select information
            cursor.execute('SELECT WIN FROM finals where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            win=cursor.fetchone()[0]
            winI = int(win)
            winF = winI + 1

            #The value of win is saved in a session variable
            session['win "'+user+'""'+nombrefinal+'"'] = winF
            winn = session.get('win "'+user+'""'+nombrefinal+'"')
            winS = str(winn)

            #2) The new value of the number of times the user achieves the goal of the practical
            #chess ending is updated
            cursor.execute('UPDATE finals set WIN ="'+winS+'" where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            connection.commit()

            #3) The number of moves that the user has used to achieve the goal of the practical
            #chess ending is inserted into the database

            #The value of movements is saved in a session variable
            session['movimientos "'+user+'""'+nombrefinal+'"'] = movI
            movimiento = session.get('movimientos "'+user+'""'+nombrefinal+'"')
            movimientoS = str(movimiento)

            #The "SQL" statement called 'INSERT' is declared to insert information
            cursor.execute('INSERT INTO nummovi(username, final, movimientos, fecha) VALUES(%s, %s, %s, %s)',(user, nombrefinal, movimientoS,today_str))
            connection.commit()

            #The cursor closes
            cursor.close()

        #If this is the first time the user has played that practical chess ending
        else:
            print('There is no such combination')
            #The value of win is saved in a session variable
            session['win "'+user+'""'+nombrefinal+'"'] = 1
            win = session.get('win "'+user+'""'+nombrefinal+'"')
            winS = str(win)

            #The value of lose is saved in a session variable
            session['lose "'+user+'""'+nombrefinal+'"'] = 0
            lose = session.get('lose "'+user+'""'+nombrefinal+'"')
            loseS = str(lose)

            #1) The new values ​​of: the number of times that the user achieves the goal of the practical
            #chess ending and the number of times that the user does not achieve that goal, are inserted
            cursor = connection.cursor()

            #The "SQL" statement called 'INSERT' is declared to insert information
            cursor.execute('INSERT INTO finals(username, final, win, lose, fecha) VALUES(%s, %s, %s, %s, %s)',(user, nombrefinal, winS, loseS, today_str))
            connection.commit()

            #2) The number of moves that the user has used to achieve the goal of the practical
            #chess ending is inserted into the database

            #The value of moves is saved in a session variable
            session['movimientos "'+user+'""'+nombrefinal+'"'] = movI
            movimiento = session.get('movimientos "'+user+'""'+nombrefinal+'"')
            movimientoS = str(movimiento)

            #The "SQL" statement called 'INSERT' is declared to insert information
            cursor.execute('INSERT INTO nummovi(username, final, movimientos, fecha) VALUES(%s, %s, %s, %s)',(user, nombrefinal, movimientoS,today_str))
            connection.commit()

            #The cursor closes
            cursor.close()

    #Once the procedure that has been developed for when the user has achieved stalemate in the
    #knight and king vs pawn and king chess ending, has been explained, it will be applied
    #to the rest of the practical cess endings with some variation
    #in terms of the end name that is concerned in each case.

    #1) LOSE KNIGHT AND KING VS PAWN AND KING CHESS ENDING

    #If the user (the white pieces) has lost this practical chess ending
    elif ((pgn.find("8/8/8/8/8/4N2p/5K1k/8") >=0 and resultado=="PovScore(Mate(+1), BLACK)") or (pgn.find("8/8/8/8/8/p7/3N4/k1K5") >=0 and resultado=="PovScore(Mate(+1), BLACK)") or (pgn.find("8/8/5K2/8/8/8/4N2p/7k") >=0 and resultado=="PovScore(Mate(+1), BLACK)") or (pgn.find("8/8/5K2/8/8/8/7p/4N2k") >=0 and resultado=="PovScore(Mate(+1), BLACK)") or (pgn.find("8/8/5K2/8/8/8/6Np/7k") >= 0 and resultado=="PovScore(Mate(+1), BLACK)") or (pgn.find("8/8/5K2/8/8/8/2N4p/7k") >=0 and resultado=="PovScore(Mate(+1), BLACK)")) :

        #The name of the chess ending is saved
        nombrefinal = "Final_Caballo_Y_Rey_Vs_Peon_Y_Rey"
        #The username is saved
        user = session.get('username')
        #The date is saved
        today = date.today()
        #The date is saved in string type
        today_str = today.strftime('%d-%m-%Y')
        print("YOU LOSE" + nombrefinal + user)

        cursor = connection.cursor()
        #The "SQL" statement called 'SELECT' is declared to select information
        cursor.execute('SELECT * FROM finals WHERE USERNAME = "'+user+'" AND FINAL="'+nombrefinal+'" AND FECHA = "'+today_str+'"')
        rows = cursor.fetchall()
        results = len(rows)

        #If the user has already played that practical chess ending
        if results > 0:
            print('There is the username, the date and the name of the chess ending')

            #1) The number of times the user doesn't achieve the goal of the practical chess ending
            #is taken

            #The "SQL" statement called 'SELECT' is declared to select information
            cursor.execute('SELECT LOSE FROM finals where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            lose=cursor.fetchone()[0]
            loseI = int(lose)
            loseF = loseI + 1

            #The value of lose is saved in a session variable
            session['lose "'+user+'""'+nombrefinal+'"'] = loseF
            losee = session.get('lose "'+user+'""'+nombrefinal+'"')
            loseS = str(losee)

            #2) The new value of the number of times the user achieves the goal of the practical
            #chess ending is updated
            cursor.execute('UPDATE finals set LOSE ="'+loseS+'" where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            connection.commit()

            #The cursor closes
            cursor.close()

        #If this is the first time the user has played that practical chess ending
        else:
            print('There is no such combination')
            #The value of win is saved in a session variable
            session['win "'+user+'""'+nombrefinal+'"'] = 0
            win = session.get('win "'+user+'""'+nombrefinal+'"')
            winS = str(win)

            #The value of lose is saved in a session variable
            session['lose "'+user+'""'+nombrefinal+'"'] = 1
            lose = session.get('lose "'+user+'""'+nombrefinal+'"')
            loseS = str(lose)

            #1) The new values ​​of: the number of times that the user achieves the goal of the practical
            #chess ending and the number of times that the user does not achieve that goal, are inserted
            cursor = connection.cursor()

            #The "SQL" statement called 'INSERT' is declared to insert information
            cursor.execute('INSERT INTO finals(username, final, win, lose, fecha) VALUES(%s, %s, %s, %s, %s)',(user, nombrefinal, winS, loseS, today_str))
            connection.commit()

            #The cursor closes
            cursor.close()

    #Once the procedure that has been developed for when the user hasn't achieved the objective of the
    #knight and king vs pawn and king chess ending, has been explained, it will be applied
    #to the rest of the practical chess endings with some variation
    #in terms of the end name that is concerned in each case.


    #2) WIN QUEEN AND KING VS PAWN AND KING CHESS ENDING
    elif ((pgn.find("8/3pk3/8/8/8/1K6/8/2Q5") >=0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("5k2/4p3/8/8/8/8/8/2KQ4") >=0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("8/3pk3/8/8/8/8/5K2/2Q5") >=0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("8/1pk5/8/8/8/6K1/8/3Q4") >=0 and resultado == "PovScore(Mate(+1), WHITE)") or (pgn.find("8/2pk4/8/8/8/8/6KQ/8") >=0 and resultado == "PovScore(Mate(+1), WHITE)")):
        nombrefinal = "Final_Dama_Y_Rey_Vs_Peon_Y_Rey"
        user = session.get('username')
        today = date.today()
        today_str = today.strftime('%d-%m-%Y')
        print("YOU WON" + nombrefinal + user)

        mov = []

        if (list[-9] == "."):
            mov = list[-11] + list[-10]
        else:
            mov = list[-10] + list[-9]

        movI = int(mov)
        movIF = movI + 1
        print("MOVif ", movIF)


        cursor = connection.cursor()
        cursor.execute('SELECT * FROM finals WHERE USERNAME = "'+user+'" AND FINAL="'+nombrefinal+'" AND FECHA = "'+today_str+'"')
        rows = cursor.fetchall()
        results = len(rows)

        if results > 0:
            print('There is the username, the date and the name of the chess ending')
            cursor.execute('SELECT WIN FROM finals where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            win=cursor.fetchone()[0]
            winI = int(win)
            winF = winI + 1
            session['win "'+user+'""'+nombrefinal+'"'] = winF
            winn = session.get('win "'+user+'""'+nombrefinal+'"')
            winS = str(winn)

            cursor.execute('UPDATE finals set WIN ="'+winS+'" where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            connection.commit()

            session['movimientos "'+user+'""'+nombrefinal+'"'] = movIF
            movimiento = session.get('movimientos "'+user+'""'+nombrefinal+'"')
            movimientoS = str(movimiento)

            cursor.execute('INSERT INTO nummovi(username, final, movimientos, fecha) VALUES(%s, %s, %s, %s)',(user, nombrefinal, movimientoS,today_str))
            connection.commit()

            cursor.close()

        else:
            print('There is no such combination')
            session['win "'+user+'""'+nombrefinal+'"'] = 1
            win = session.get('win "'+user+'""'+nombrefinal+'"')
            winS = str(win)

            session['lose "'+user+'""'+nombrefinal+'"'] = 0
            lose = session.get('lose "'+user+'""'+nombrefinal+'"')
            loseS = str(lose)

            cursor = connection.cursor()
            cursor.execute('INSERT INTO finals(username, final, win, lose, fecha) VALUES(%s, %s, %s, %s, %s)',(user, nombrefinal, winS, loseS, today_str))
            connection.commit()

            session['movimientos "'+user+'""'+nombrefinal+'"'] = movIF
            movimiento = session.get('movimientos "'+user+'""'+nombrefinal+'"')
            movimientoS = str(movimiento)

            cursor.execute('INSERT INTO nummovi(username, final, movimientos, fecha) VALUES(%s, %s, %s, %s)',(user, nombrefinal, movimientoS,today_str))
            connection.commit()

            cursor.close()

    #2) GET DRAW IN THE QUEEN AND KING VS PAWN AND KING CHESS ENDING
    elif ((pgn.find("8/3pk3/8/8/8/1K6/8/2Q5") >=0 and resultado == "PovScore(Cp(0), BLACK)") or (pgn.find("5k2/4p3/8/8/8/8/8/2KQ4") >=0 and resultado == "PovScore(Cp(0), BLACK)") or (pgn.find("8/3pk3/8/8/8/8/5K2/2Q5") >=0 and resultado == "PovScore(Cp(0), BLACK)") or (pgn.find("8/1pk5/8/8/8/6K1/8/3Q4") >=0 and resultado == "PovScore(Cp(0), BLACK)") or (pgn.find("8/2pk4/8/8/8/8/6KQ/8") >=0 and resultado == "PovScore(Cp(0), BLACK)")):
        nombrefinal = "Final_Dama_Y_Rey_Vs_Peon_Y_Rey"
        user = session.get('username')
        today = date.today()
        today_str = today.strftime('%d-%m-%Y')
        print("YOU WON" + nombrefinal + user)

        mov = []

        if (list[-6] == "."):
            mov = list[-8] + list[-7]
        elif (list[-7] == "."):
            mov = list[-9] + list[-8]
        else:
            mov = list[-7] + list[-6]

        movI = int(mov)
        print("MOVi: ", movI)

        cursor = connection.cursor()
        cursor.execute('SELECT * FROM finals WHERE USERNAME = "'+user+'" AND FINAL="'+nombrefinal+'" AND FECHA = "'+today_str+'"')
        rows = cursor.fetchall()
        results = len(rows)

        if results > 0:
            print('There is the username, the date and the name of the chess ending')
            cursor.execute('SELECT WIN FROM finals where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            win=cursor.fetchone()[0]
            winI = int(win)
            winF = winI + 1
            session['win "'+user+'""'+nombrefinal+'"'] = winF
            winn = session.get('win "'+user+'""'+nombrefinal+'"')
            winS = str(winn)

            cursor.execute('UPDATE finals set WIN ="'+winS+'" where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            connection.commit()

            session['movimientos "'+user+'""'+nombrefinal+'"'] = movI
            movimiento = session.get('movimientos "'+user+'""'+nombrefinal+'"')
            movimientoS = str(movimiento)

            cursor.execute('INSERT INTO nummovi(username, final, movimientos, fecha) VALUES(%s, %s, %s, %s)',(user, nombrefinal, movimientoS,today_str))
            connection.commit()

            cursor.close()

        else:
            print('There is no such combination')
            session['win "'+user+'""'+nombrefinal+'"'] = 1
            win = session.get('win "'+user+'""'+nombrefinal+'"')
            winS = str(win)

            session['lose "'+user+'""'+nombrefinal+'"'] = 0
            lose = session.get('lose "'+user+'""'+nombrefinal+'"')
            loseS = str(lose)

            cursor = connection.cursor()
            cursor.execute('INSERT INTO finals(username, final, win, lose, fecha) VALUES(%s, %s, %s, %s, %s)',(user, nombrefinal, winS, loseS, today_str))
            connection.commit()

            session['movimientos "'+user+'""'+nombrefinal+'"'] = movI
            movimiento = session.get('movimientos "'+user+'""'+nombrefinal+'"')
            movimientoS = str(movimiento)

            cursor.execute('INSERT INTO nummovi(username, final, movimientos, fecha) VALUES(%s, %s, %s, %s)',(user, nombrefinal, movimientoS,today_str))
            connection.commit()

            cursor.close()

    #2) LOSE QUEEN AND KING VS PAWN AND KING CHESS ENDING
    elif ((pgn.find("8/3pk3/8/8/8/1K6/8/2Q5") >=0 and resultado=="PovScore(Mate(+1), BLACK)") or (pgn.find("5k2/4p3/8/8/8/8/8/2KQ4") >=0 and resultado=="PovScore(Mate(+1), BLACK)") or (pgn.find("8/3pk3/8/8/8/8/5K2/2Q5") >=0 and resultado=="PovScore(Mate(+1), BLACK)") or (pgn.find("8/1pk5/8/8/8/6K1/8/3Q4") >=0 and resultado=="PovScore(Mate(+1), BLACK)") or (pgn.find("8/2pk4/8/8/8/8/6KQ/8") >=0 and resultado =="PovScore(Mate(+1), BLACK)")):
        nombrefinal = "Final_Dama_Y_Rey_Vs_Peon_Y_Rey"
        user = session.get('username')
        today = date.today()
        today_str = today.strftime('%d-%m-%Y')
        print("YOU LOSE" + nombrefinal + user)

        cursor = connection.cursor()
        cursor.execute('SELECT * FROM finals WHERE USERNAME = "'+user+'" AND FINAL="'+nombrefinal+'" AND FECHA = "'+today_str+'"')
        rows = cursor.fetchall()
        results = len(rows)

        if results > 0:
            print('There is the username, the date and the name of the chess ending')

            cursor.execute('SELECT LOSE FROM finals where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            lose=cursor.fetchone()[0]
            loseI = int(lose)
            loseF = loseI + 1
            session['lose "'+user+'""'+nombrefinal+'"'] = loseF
            losee = session.get('lose "'+user+'""'+nombrefinal+'"')
            loseS = str(losee)

            cursor.execute('UPDATE finals set LOSE ="'+loseS+'" where USERNAME = "'+user+'" AND FINAL = "'+nombrefinal+'" AND FECHA = "'+today_str+'"')
            connection.commit()

            cursor.close()

        else:
            print('There is no such combination')
            session['win "'+user+'""'+nombrefinal+'"'] = 0
            win = session.get('win "'+user+'""'+nombrefinal+'"')
            winS = str(win)

            session['lose "'+user+'""'+nombrefinal+'"'] = 1
            lose = session.get('lose "'+user+'""'+nombrefinal+'"')
            loseS = str(lose)

            cursor = connection.cursor()
            cursor.execute('INSERT INTO finals(username, final, win, lose, fecha) VALUES(%s, %s, %s, %s, %s)',(user, nombrefinal, winS, loseS, today_str))
            connection.commit()

            cursor.close()

    #The chess engine process is terminated
    engine.quit()

    #The following values ​​are returned to the "make_movePracticalChessEndingsRegisteredUser()" function,
    #the http POST request, of "practicalChessEndingRegisteredUser.html"
    return {
        'fen': fen,
        'best_move': str(best_move),
        'score': str(info['score']),
        'depth': info['depth'],
        'pv': ' '.join([str(move) for move in info['pv']]),
        'nodes': info['nodes'],
        'time': info['time']
    }


#A main driver is created
if __name__ == '__main__':
    #The HTTP server starts
    port = int(os.environ.get('PORT', 5000))
    #A socket is created
    socketio.run(app, host='127.0.0.1', port=port)
