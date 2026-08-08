import sqlite3
import pandas as pd
conn = sqlite3.connect(':memory:')
conn.execute("""CREATE TABLE author (
    author_id   INTEGER PRIMARY KEY,
    author_name TEXT NOT NULL UNIQUE
)""")

conn.execute("""CREATE TABLE book(
    book_id  INTEGER PRIMARY KEY,
    book_title  TEXT NOT NULL,
    author_id INTEGER
)""")

conn.executemany("INSERT INTO author VALUES(?,?)",[
    (1,'Roald dahl'),
    (2,'J.K Rowlig'),
    (3,'RICK RIORDAN'),
    (4,'JEFF KINNEY'),
    (5,'DAV PILKEY'),
    (6,'LEMONY SNICKET'),
    (7,'SATYJITH RAY')
])

conn.executemany("INSERT INTO book VALUES (?,?,?)",[
    (1,'CHARLIE AND CHOCOLATE FACTORY',1),
    (2,'JAMES AND THE GIANT PEACH',1),
    (3,'HARRY POTTER AND THE PHILOSOPHERS STONE',2),
    (4,'HARRY POTTER AND THE CHAMBER OF SECRETS',2)
    (5,'THE LIGHTENEING THIEF',3),
    (6,'THE SEA OF MONSTERS',3),
    (7,'DIARY OF A WIMPY KID',4),
    (8,'THE ATTIC ',7),

])


authors = pd.read_sql("SELECT * FROM author",conn)
books = pd.read_sql("SELECT * FROM book",conn)
print("Author table:")
print(authors)
print()
print("Book table :")
print(books)
print()

inner = pd.read_sql(
    "SELECT author.author_name,book.book_title"
    "FROM author INNER JOIN book ON author.author_id = book.author_id",
    conn
)
print("INNER JOIN - authors matched wih their book:")
print(inner)
print()

left = pd.read_sql(
    "SELECT author.author_name,book.book_title"
    "FROM author LEFT JOIN book ON author.author_id=book.author_id",
    conn
)

print("LEFT JOIN - all authors,NULL whereb no book found:")
print(left)
print()

cross = pd.read_sql(
    "SELECT author.author_name,book.book_title"
    "FROM author CROSS JOIN book WHERE author.author_id <=2",
    conn
)
