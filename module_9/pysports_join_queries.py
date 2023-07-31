#joining player and team tables
#by Jacob Rubin
#for CYBR410
#7/30/2023

import mysql.connector
from mysql.connector import errorcode
#required modules^
config = {
    "user": "root",
    "password": "Ninja1741$",
    "host": "localhost",
    "database": "pysports",
    "raise_on_warnings": True
}
#config object above, try/catch block below
try:
    
    db = mysql.connector.connect(**config) 
#connecting to pysports^
    cursor = db.cursor()
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
#inner join^
    players = cursor.fetchall()
#results from cursor^
    print("\n\nThe requested Player Records are as follows:")
    for player in players:
        print("\nPlayer ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player[0], player[1], player[2], player[3]))
#displaying results^
    input("\n\nPlease press the enter key or exit the program to conclude.")

except mysql.connector.Error as err:
    
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Unfortunately, the username and/or password provided are invalid. Feel free to try again.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Unfortunately, the specified database could not be located. It likely doesn't exist. Feel free to try again.")
    else:
        print(err)
#errors^
        
finally:

    db.close()
#closing the connection 
