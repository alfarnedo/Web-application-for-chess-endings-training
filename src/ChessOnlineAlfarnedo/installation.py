#This script must be run first, in order to have
#the database and the necessary tables, for the web application

#NOTE:
#The user must, before running this script:
    # 1) Install "MySQL" on your computer
    # 2) Install "mysql.connector", to be able to connect this script to "MySQL",
         #by typing the command "pip install mysql-connector-python" in the terminal

#FOR THE DATABASE

#Imports 'mysql.connector' as sql
import mysql.connector as sql

#Connect to MySQL using the 'connect ()' method
#For this method, 3 parameters are needed: 'host', 'user', 'password'
connection = sql.connect(user = 'root',
                         host = 'localhost',
                         passwd = "enter your own password")

#Using the method 'is_connected ()' we inform ourselves if the connection to MySQL Server is available or not

#A) If the connection is available:
if connection.is_connected():
    #It shows on the screen that the connection to MySQL is available
    print("Connection available")

    #An instance of the "cursor ()" class is created, to be able to execute "SQL" statements in "Python"
    cur1 = connection.cursor()
    #The "SQL" statement is declared to create the database called ChessOnlineAlfar
    sql="create database ChessOnlineAlfar"
    #The method "exectue ()" is used to compile the previous "statement" of "SQL"
    cur1.execute(sql)

    #After creating the database, through the "statement" "use + database name", you must select
    #the database you want to work with; in this case ChessOnlineAlfar
    sql="use ChessOnlineAlfar"
    #The "exectue ()" method is used to compile the previous "statement"
    cur1.execute(sql)

    #We proceed to declare the "SQL" statements to create the necessary tables
    #to store certain information in the web application:

    #1) Registered users in the web application are stored in the "users" table
    sql="""create table users (
         id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
         name VARCHAR(100),
         email VARCHAR(100),
         username VARCHAR(100),
         password VARCHAR(100),
         register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
         )"""

    #The "exectue ()" method is used to compile the previous "statement"
    cur1.execute(sql)
    #The "commit()" method is used to send a COMMIT statement to the MySQL server,
    #thus confirming the current transaction
    connection.commit()

    #2) Each registered user’s game statistics are stored in the "finals" table:
    #The number of times the user achieves the goal of each chess ending and
    #the number of times the goal is not achieved
    sql="""create table finals (
         ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
         USERNAME VARCHAR(100) NOT NULL,
         FINAL VARCHAR(100) NOT NULL,
         WIN  VARCHAR(1000) NOT NULL,
         LOSE VARCHAR(1000) NOT NULL,
         FECHA VARCHAR(1000) NOT NULL,
         PRIMARY KEY (ID)
         )"""

    #The "exectue ()" method is used to compile the previous "statement"
    cur1.execute(sql)
    #The "commit()" method is used to send a COMMIT statement to the MySQL server,
    #thus confirming the current transaction
    connection.commit()

    #3) In the table "nummovi" the number of moves that the registered user uses
    #to achieve the goal of each chess ending is stored
    sql="""create table nummovi (
         ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
         USERNAME VARCHAR(100) NOT NULL,
         FINAL VARCHAR(100) NOT NULL,
         MOVIMIENTOS VARCHAR(10000) NOT NULL,
         FECHA VARCHAR(1000) NOT NULL,
         PRIMARY KEY (ID)
         )"""

    #The "exectue ()" method is used to compile the previous "statement".
    cur1.execute(sql)
    #The "commit()" method is used to send a COMMIT statement to the MySQL server,
    #thus confirming the current transaction.
    connection.commit()

    #Finally, after completing all queries to "MySQL", proceed to close the cursor
    #and then close the connection
    cur1.close()
    connection.close()

#B) If the connection isn't available
else:
    #It shows on the screen that the connection to MySQL isn't available
    print("Connection failed")
