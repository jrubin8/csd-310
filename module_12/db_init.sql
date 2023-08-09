-- db_init.sql
-- Jacob Rubin
-- August, 2023
-- Script for WhatABook database initialization.

DROP USER IF EXISTS 'whatabook_user'@'localhost';
-- drops the user as required^

CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';
-- creating a user for WhatABook with the required password^
 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';
-- granting privileges to the created user^

ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;
-- drop constraints, from the course's repository^

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
-- drops the table if logically required^

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);
-- user table creation^
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);
-- store table creation^

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);
-- book table creation^
CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);
-- wishlist table creation, from course repository^

INSERT INTO user(first_name, last_name) 
    VALUES('Athos', 'Vicomte');

INSERT INTO user(first_name, last_name)
    VALUES('Porthos', 'Vicomte');

INSERT INTO user(first_name, last_name)
    VALUES('Aretha', 'Franklin');
-- inserting 3 required user records for Athos, Porthos, and Aretha^

INSERT INTO store(locale)
    VALUES('275 Aubrey Drive Quakertown, PA');
-- inserting a store record in Quakertown, PA^

INSERT INTO book(book_name, author, details)
    VALUES('Into the Wild', 'Erin Hunter', 'The first Warriors book');

INSERT INTO book(book_name, author, details)
    VALUES('Fire and Ice', 'Erin Hunter', 'The second Warriors book');

INSERT INTO book(book_name, author, details)
    VALUES('Forest of Secrets', 'Erin Hunter', 'The third Warriors book');

INSERT INTO book(book_name, author, details)
    VALUES('Rising Storm', 'Erin Hunter', 'The fourth Warriors book');

INSERT INTO book(book_name, author, details)
    VALUES('A Dangerous Path', 'Erin Hunter', 'The fifth Warriors book');

INSERT INTO book(book_name, author, details)
    VALUES('The Darkest Hour', 'Erin Hunter', 'The sixth Warriors book');

INSERT INTO book(book_name, author, details)
    VALUES('Enders Game', 'Orson Scott Card', 'Part of a series');

INSERT INTO book(book_name, author, details)
    VALUES('Speaker For the Dead', 'Orson Scott Card', 'Part of a series');

INSERT INTO book(book_name, author, details)
    VALUES('Xenocide', 'Orson Scott Card', 'Part of a series');
-- inserting book records for the required 9 books^

INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Athos'), 
        (SELECT book_id FROM book WHERE book_name = 'Enders Game')
    );
-- Athos wishlist^

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Porthos'),
        (SELECT book_id FROM book WHERE book_name = 'Xenocide')
    );
-- Porthos wishlist^

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Aretha'),
        (SELECT book_id FROM book WHERE book_name = 'Rising Storm')
    );
-- Aretha wishlist^