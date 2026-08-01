import sqlite3
import pandas as pd
conn = sqlite3.connect('library.db')
cursor = conn.cursor()
cursor.executescript("""
DROP TABLE IF EXISTS Book;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Book_Loan;

CREATE TABLE Book (
    Book_Id          INTEGER PRIMARY KEY,
    Book_Title       TEXT,
    Author           TEXT,
    Category         TEXT,
    Pages            INTEGER
);

CREATE TABLE Member (
    Member_Id   INTEGER PRIMARY KEY,
    Member_Name TEXT
);

CREATE TABLE Book_Loan (
    Loan_Id   INTEGER PRIMARY KEY,
    Book_Id   INTEGER,
    Member_Id INTEGER
);

INSERT INTO Book VALUES
  (1, 'The Secret Garden', 'Frances Hodgson Burnett', 'Fiction', 331),
  (2, 'Science', 'Riya Shah', 'Science', 120),
  (3, ' Adventure', 'Arun Mehta', 'Science', 245),
  (4, 'History of India', 'Neha Rao', 'History', 310),
  (5, 'The Jungle Book', 'Rudyard Kipling', 'Fiction', 277),
  (6, 'Maths Made Easy', 'Anita Das', 'Education', 180),
  (7, 'Stories for Children', 'Meera Singh', 'Fiction', 150),
  (8, 'Amazing Animals', 'Kabir Khan', 'Science', 210);

INSERT INTO Member VALUES
  (1, 'Aarav'), (2, 'Diya'), (3, 'Kabir'), (4, 'Meera');

INSERT INTO Book_Loan VALUES
  (1, 1, 1), (2, 3, 2), (3, 5, 3), (4, 2, 4);
""")
conn.commit()

print('Library database ready!')

tables = pd.read_sql("""SELECT *
    FROM sqlite_master
    WHERE type='table';""", conn)

print(tables)
books = pd.read_sql("""SELECT *
    FROM Book;""", conn)

print(books)
print('Rows and columns:', books.shape)
all_books = pd.read_sql("""SELECT *
    FROM Book;""", conn)

print(all_books)

book_details = pd.read_sql("""SELECT Book_Id, Book_Title, Author
    FROM Book;""", conn)

print(book_details)
loan_details = pd.read_sql("""SELECT Book_Id, Member_Id
    FROM Book_Loan;""", conn)

print(loan_details)

science_books = pd.read_sql("""SELECT *
    FROM Book
    WHERE Category == 'Science';""", conn)

print(science_books)

the_books = pd.read_sql("""SELECT *
    FROM Book
    WHERE Book_Title LIKE 'The%';""", conn)

print(the_books)
book_titles = pd.read_sql("""SELECT *
    FROM Book
    WHERE Book_Title LIKE '%Book';""", conn)

print(book_titles)
page_range = pd.read_sql("""SELECT MIN(Pages), MAX(Pages)
    FROM Book;""", conn)
print(page_range)
conn.close()
