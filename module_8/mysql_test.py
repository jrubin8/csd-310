#module 8 assignment 8.2 mysql_test: Jake Rubin

#import statement
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "Ninja1741$",
    "host": "localhost",
    "database": "pysports",
    "raise_on_warnings": True
}

#configurating database^
try: 

    db = mysql.connector.connect(**config) #connecting to 'pysports'
     
    print("\n\n\nThe user {} has successfully connected to MySQL on the following host: {} with the following database: {}".format(config["user"], config["host"], config["database"]))

    input("\nPlease press the 'enter' key or close the program to conclude the test.")
#The status as output for the user
except mysql.connector.Error as err:
#error code^

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("\n\nAn Insufficient username and/or password was specified. Please feel free to try again.")
#conditional message printed if username/password were incorrect.
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("\n\n Unfortunately, the specified database was not found. It may have been spelled incorrectly or might not exist. Please feel free to try again.")
#conditional message printed if database was bad.
    else:
        print(err)

finally:

    db.close()
#closing
