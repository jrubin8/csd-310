#for inserting, updating, and deleting records from the database "pysports"
#by Jake Rubin
#CYBR410
#7/30/2023

import mysql.connector
from mysql.connector import errorcode
#import statement^

config = {
    "user": "root",
    "password": "Ninja1741$",
    "host": "localhost",
    "database": "pysports",
    "raise_on_warnings": True
}
#database config object^

def show_players(cursor, title):

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
#inner join^ 
    players = cursor.fetchall()
#getting results from cursor^
    print("\n\n{}".format(title)) 
    for player in players:
        print("\nPlayer ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player[0], player[1], player[2], player[3]))
#displays results^
        
try:
    
    db = mysql.connector.connect(**config)
#connecting to pysports^   
    cursor = db.cursor()
 
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                 "VALUES(%s, %s, %s)")
#player query insertion^ 
    player_data = ("Wheezy", "McStravick", 1)
#player data^
    cursor.execute(add_player, player_data)
#insert a new record^ 
    db.commit() 
    show_players(cursor, "Player records available after the insertion are as follows:")
#shows all records, post-insertion^
     
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Brenda', last_name = 'Toodleberry' WHERE first_name = 'Wheezy'")
#updates the new player^
    cursor.execute(update_player) 
    show_players(cursor, "Existing player records after the update are as follows:")
#shows all records post-update^ 
    delete_player = ("DELETE FROM player WHERE first_name = 'Brenda'")
#delete query^
    cursor.execute(delete_player)

    # show all records in the player table 
    show_players(cursor, "Existing players post-delete are as follows:")

    input("\n\nPlease press the enter key or exit the program to conclude.")

except mysql.connector.Error as err: 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("\nUnfortunately, the username and/or password provided are invalid. Please feel free to try again.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("\nUnfortunately, the specified database does not exist.")
    else:
        print(err)
#errors^
finally:

    db.close()
#closing the connection^
