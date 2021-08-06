### ChessOnlineAlfarnedo

## Overview
**ChessOnlineAlfarnedo** is the result of a Master Thesis Project, to develop a web application, as a tutor for the training of certain chess endings, which helps to improve the skills and enhance the capabilities of all types of chess players. 

To achieve this goal, it implements a set of technologies, such as frameworks, in this case Flask, as well as the adoption of the MySQL database and the latest version of the Stockfish-13 chess engine, which presents a high level of ELO and score and introduces the UCI protocol (Universal Chess Interface) that facilitates its use and access, and PGN (Portable Game Notation) and FEN (Forsyth-Edwards Notation) formats with which, respectively, the moves made during the game are collected and the state of the board is known at each moment of the game. 

The Stockfish complete source code is located at the following link: https://github.com/official-stockfish/Stockfish 

To carry out this project different books, open codes and tutorials of both GitHub and forums and videos were used, whose links are the following:
  * https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3-es 
  * https://books.google.es/books?hl=es&lr=&id=cVlPDwAAQBAJ&oi=fnd&pg=PT25&dq=FRAMEWORK+FLASK&ots=xODWal_qa_&sig=Sf99Qq5MN5M-3-nO3brzgxyVmJQ#v=onepage&q=FRAMEWORK%20FLASK&f=false
  * https://github.com/maksimKorzh/chess_programming
  * https://j2logo.com/tutorial-flask-leccion-3-formularios-wtforms/
  * https://www.youtube.com/watch?v=7Oj4LcCE7n8
  * https://www.youtube.com/watch?v=L20z4gCSfA8
  * https://www.youtube.com/watch?v=bdkIQsJQvNQ&t=412s

## APP DESCRIPTION
The web application for chess endgame training, object of this work, will integrate three profiles/roles: Unregistered User, Registered User and Application Administrator.

1) The user Without Registration will be able to see several links that will open new pages, in which he could:
  * Play a game of chess against the Stockfish engine. 
  * Playing chess endings, both basic and practical, against the Stockfish engine.
  * Access a Wikipedia link with information on what are chess endings and what types there are.
  * A registered link so that any user can register on the system (by filling in the required fields). 
  * A login link. This asks the user to enter their username and password. 
  * A Home link, to load the main menu.
  * An About us link, showing a description of who we are. 
  * A Stockfish link, a link to information on what Stockfish is.  

2) When a User registers, they will have the options (each with a different hyperlink that will take them to other pages) of: 
  * Play a game of chess against the Stockfish engine. 
  * Playing chess endings, both basic and practical, against the Stockfish engine; but in this case, some information will be saved in different tables in a MySQL database. 
     * The number of times the user achieves the goal of the chess ending. 
     * The number of times the user fails to achieve the goal of the chess ending.
     * The number of moves the user uses to achieve the goal of the chess ending. 
  * Access a Wikipedia link with information on what are chess endings and what types there are. 
  * Visualize in the statistics section, using bar graphs:
     * In percentage, with respect to the objective to be achieved in each type of chess ending, how many times has been achieved.
     * The average number of movements employed, relative to the number of optimal movements to achieve the chess ending goal. 
     * Information on what the goal is to achieve in each chess ending. 
  * Log out. 
  * A Home link, to load the main menú.
  * An About us link, showing a description of who we are. 
  * A Stockfish link, a link to information on what Stockfish is.
  
3) The Administrator will be the one who:
  * Install the program by following the steps indicated in the next section "FILES". 
  * View the code developed to implement the web application, called appChessOnline.py, as indicated in the next section "FILES"
  * Can use the database. 
  * Can modify the database, either by adding new tables or by removing the tables that are created automatically by running the script Instalacion.py, and creating your own (for this you must make changes to the script called appChessOnline.py).  
  * Visualize the database manually, if the required packages are installed, and be able to have control of:  
    * Users registered to the web application.
    * The statistics of each of the registered users: 
      * The number of times he meets the goal of the chess ending.
      * The number of times he doesn’t meet the goal of the chess ending.
      * The number of moves he uses in each chess ending to meet the goal of the chess ending. 

## FILES
The distribution of ChessOnlineAlfarnedo project consists of the following files:

  * Readme.md, the file you are currently reading.
  * LICENSE, a file that contains the GNU General Public License version 3.
  * AUTHORS, a text file with the list of authors for the Project
  * src, a subdirectory containing the full source code. 


## PRE-REQUISITES
The following packages must be installed on the computer where the web application is to be run.  
  * #### Python 3
    The computer where the project was developed has version Python 3.8.1. 
  * #### MySQL database
    You need to install MySQL on your computer in order to perform certain actions during the development of the web application.     
    To do this, you can follow this tutorial from youtube: https://www.youtube.com/watch?v=jkyLOV54BQM  
   * #### Mysql.connector
     To connect a Python script to MySQL, the mysql.connectorlibrary must be installed. To do this, run the following command "pip install mysql-connector-python" on the computer terminal. 
   * #### Flask
     In order to use the Python framework called Flask you need to have it installed on your computer. To do this, write the following command "pip install flask" to the computer terminal. 
   * #### Flask-SocketIO
     In the development of the web application it was decided to use the SocketIO transport protocol of the Flask-SocketIO library. To do this, write the following command on the computer terminal "pip install Flask-SocketIO". 
   * #### WTForms
     To validate and represent forms during the development of the web application, the WTForms library must be installed; therefore, the command "pip install WTForms" is written to the computer terminal. 
   * #### Passlib
     To encrypt the passwords that each user enters in their registry, the "sha256_crypt.encrypt" function of the Passlib library is used. Therefore, this library must be installed on the computer using the command "pip install passlib". 
   * #### Python-chess y Chess
     In order to implement and develop a chess in the web application, Python has two libraries for this purpose. Therefore, these libraries must be installed on the computer by typing the commands "pip install python-chess" and "pip install chess" in the terminal. 
   * #### DateTime
     To be able to take each of the dates on which either a user registers in the web application, or that a registered user plays a chess ending, the date function of the datetime library is used. For this reason, this library is installed on the computer using the command "pip install DateTime".

Once these packages are installed, first you must run the script installation.py in order to have the database and the necessary tables, for the web application. 

After that, the appChessOnline.py script is executed to run the web application for chess endings training.







