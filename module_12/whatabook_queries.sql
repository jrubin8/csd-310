-- whatabook_queries.sql
-- Jake Rubin
-- August, 2023
-- Queries, etc. for WhatABook

INSERT INTO wishlist(user_id, book_id)
    VALUES(1, 9);
-- Adding books to a wishlist, where the values are replaced with the program values chosen.^

DELETE FROM wishlist WHERE user_id = 1 AND book_id = 9;
-- Removing books from a wishlist, where the values are replaced with the program values chosen.^

SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author
FROM wishlist
    INNER JOIN user ON wishlist.user_id = user.user_id
    INNER JOIN book ON wishlist.book_id = book.book_id
WHERE user.user_id = 1;
-- Query to view wishlist items, from course repository^

SELECT book_id, book_name, author, details from book;
-- Query to view available books^

SELECT book_id, book_name, author, details
FROM book
WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = 1);
-- Query to view books not already in the wishlist, where the "user_id" is the program value chosen.
-- From course repository^

SELECT store_id, locale from store;
-- Query to retrieve the store's location^
