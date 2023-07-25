
#pysports_queries.py
#By Jake Rubin
#For CYBR410
#Tests queries against "pysports" 


import mysql.connector
from mysql.connector import errorcode
#import statements needed for the program^

config = {
    "user": "root",
    "password": "Ninja1741$",
    "host": "localhost",
    "database": "pysports",
    "raise_on_warnings": True
}
#configuration object above, sets the pysports instance. Try catch block below.
try:

    db = mysql.connector.connect(**config)
    #Connecting to pysports^
    cursor = db.cursor() 
    cursor.execute("SELECT team_id, team_name, mascot FROM team") 
    teams = cursor.fetchall()
    print("\nAvailable Team Records are as follows:")
     #getting and printing results for team records^
    for team in teams: 
        print("\n\nTeam ID: {}\nTeam Name: {}\nMascot: {}\n".format(team[0], team[1], team[2]))

 
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player") 
    players = cursor.fetchall()
    print ("\nHere are all available Player Records:")

   #getting and printing results for player records^
    for player in players:
        print("\n\nPlayer ID: {}\nFirst Name: {}\nLast Name: {}\nTeam ID: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n\nPlease press the enter key to conclude the program.")

except mysql.connector.Error as err:
    

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The username and/or password provided were invalid. Please feel free to try again.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Unfortunately, the specified database does not exist. Please feel free to try again.")

    else:
        print(err)
#dealing with errors^^^
finally:
    
    db.close()
#closing the connection
