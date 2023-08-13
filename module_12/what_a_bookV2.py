#WhatABookV2
#By Jake Rubin
#August, 2023
#Final project for CYBR410 with Professor Peter Haas
#As per requirements, this is intended to be:
#a console application that allows customers to browse their in-store book listing, add books to their Wishlist, and view store hours and location(s)
#connected to the whatabook database
#V2 Notes:
#Made some adjustments related to menu looping during errors after reviewing peer feedback.
#Added a user warning for something I was unable to fix to create a courteous warning about potential inconvenience.
import sys
import mysql.connector
from mysql.connector import errorcode
#Required imports^

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "localhost",
    "database": "whatabook",
    "raise_on_warnings": True
}
#Configuration object (WhatABook)^

def show_menu():    
    print("\nWhatABook Main Menu:\n")
    print("1. View Books\n2. View Store Locations\n3. My Account\n4. Exit Program\n\n")    
    try:
        choice = int(input('For example, enter 2 to view WhatABook locations: '))
        return choice
    except ValueError:        
        print("\n\nYour selection was invalid, but you can try again!\n")
        show_menu()
#main menu^
        
def show_account_menu():
    try:        
        print("\nWelcome to your WhatABook account. Please select an option from the list below.\n")
        print("1. My Wishlist\n\n2. Add Book to My Wishlist\n\n3. Main Menu")        
        account_option = int(input('For example, enter 3 to go back to the Main Menu: '))        
        return account_option
    except ValueError:        
        print("\nYour entry was invalid, but please feel free to try again.\n")
        show_account_menu()        
#my WhatABook account menu, through which users view and add books to their wishlist^
        
def validate_user():
    try:        
        user_id = int(input('\nEnter a valid customer id, for example 1 for user_id 1: '))
        if user_id < 0 or user_id > 3 or user_id == 0:            
            print("\nThat customer number wasn't valid. Try again with a valid customer id.\n")
            validate_user()
        return user_id
    except ValueError:        
        print("That wasn't a valid customer id. Try again with a valid customer id.\n")
        validate_user()        
#validates user_id^               

def show_locations(_cursor):    
    _cursor.execute("SELECT store_id, locale from store")
    locations = _cursor.fetchall()    
    print("\nDisplaying current WhatABook store locations below:\n")    
    for location in locations:        
        print("Locale: {}\n".format(location[1]))
        print("\nHours:\nMonday through Friday- 7am to 8pm\nSaturday - 10am to 8pm\nSunday - Closed!")
#shows all whatabook locations and hours^
        
def show_books(_cursor):    
    _cursor.execute("SELECT book_id, book_name, author, details from book") 
    books = _cursor.fetchall()    
    print("\nThe following lovely selection is available at WhatABook at this point in time:\n")    
    for book in books:
        print("Book Name: {}\nAuthor: {}\nDetails: {}\n".format(book[1], book[2], book[3]))        
#join and displayed results related to showing available books^
        
def show_wishlist(_cursor, _user_id):
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))    
    wishlist = _cursor.fetchall()   
    print("\nThe following items are currently in the wishlist:\n")
    for book in wishlist:
        print("Book Name: {}\nAuthor: {}\n".format(book[4], book[5]))
#finds and displays books in the user's current list^
        
def show_books_to_add(_cursor, _user_id):
    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
    _cursor.execute(query)
    books_to_add = _cursor.fetchall()
    print("\nThe following books aren't in your list at this time. What are you waiting for?\n\nPlease note: At this time, a system error will occur if you enter an invalid or non-numerical book_id.\nWe are working hard to fix this for you as soon as possible.\n")
    for book in books_to_add:
        print("Book Id: {}\nBook Name: {}\n".format(book[0], book[1]))
#query and displays books not in the user's current list^
        
def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))
#adding a book to the wishlist^
    
#try/catch block for errors below
    
try:
    db = mysql.connector.connect(**config) 
#connecting to WhatABook^
    cursor = db.cursor()
#query cursor^
    
    print("\n\nWelcome to WhatABook's first official application!\n")
#displays welcome message to those entering the program^
    
    user_selection = show_menu() 
#main menu^
    
    while user_selection != 4:
#defining the parameters for when the selection is not 4^
        
        if user_selection == 1:
            show_books(cursor)
#1 to show books^
        
        if user_selection == 2:
            show_locations(cursor)
#2 to show location(s)^
            

        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()
#3 validates the user and enters their account menu^
            
            while account_option != 3:
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)
                if account_option == 2:
                    show_books_to_add(cursor, my_user_id)
#when the option within the account menu is 1, the wishlist is shown; when the option is 2, books available to add are shown                     
#lines 114 through 138 came from the course repository^
                     
                    book_id = int(input("\nEnter the id of the book you would like to add at this time: "))
                    add_book_to_wishlist(cursor, my_user_id, book_id)
                    db.commit() # commit the changes to the database 
                    print("\nBook id: {} was just added to your wishlist. Look at you go!\n".format(book_id))
#entering the id of the desired books, adding them to the wishlist, committing changes to the database, and displaying results^
                     
                if account_option < 0 or account_option > 3 or account_option == 0:
                    print("\nYour option was invalid. Please try again or close the program.\n")                   
                account_option = show_account_menu()
#in case of an invalid entry^
                
        if user_selection < 0 or user_selection > 4 or user_selection == 0:
            print("\nThe option you selected was not valid. Please feel free to try again.\n")
        user_selection = show_menu()
#in case of invalid entry^
        
    print("\nThe WhatABook application will now conclude. Thanks for visiting WhatABook! We look forward to seeing you again soon.\n")

except mysql.connector.Error as err: 
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The username and/or password provided were not valid at this time. Please feel free to try again with different credentials.\n")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Unfortunately, the database you selected was invalid. Please choose a valid database.\n")
    else:
        print(err)
#error handling^
        
finally:
    db.close()
#closes the connection to the database^
