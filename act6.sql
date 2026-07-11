DROP TABLE IF EXISTS book;
CREATE TABLE IF NOT EXISTS book(
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    genre TEXT NOT NULL,
    author TEXT NOT NULL,
    published_year INTEGER NOT NULL,
    rating REAL NOT NULL
);
INSERT INTO book VALUES
(1,'HARRY POTTER','FANTASY','J.K.ROWLING',1997,4.9),
(2,'THE HOBBIT','FANTASY','J.R.R.TLOKIER',1937,4.8),
(3,'CHARLOOTEE S WEB','CHILDREN','E.B.WHITE',1937,4.6),
(4,'MATILDA','FANTASY','RONLD',1967,4.9),
(5,'THE MYSTERY ISLAND','ADVENTURE','STEVENSON',1883,4.5),
(6,'TRESSURE ISLAND','ADVENTURE','STEVENSON',1949,4.4),
(7,'PERCY JACKSON','FANTASY','RICK',2005,4.8),
(8,'THE JUNGLE BOOK','FANTASY','KIPLING',1897,4.8);
SELECT * FROM book;
SELECT * FROM book ORDER BY rating DESC;
SELECT * FROM book ORDER BY published_year ASC;
SELECT * FROM book ORDER BY genre ASC,rating DESC;
SELECT * FROM book ORDER BY rating DESC 
LIMIT 3;
SELECT * FROM book ORDER BY published_year ASC 
LIMIT 2;
SELECT genre,
COUNT(*) AS ToatalBooks
FROM book
GROUP BY genre;
SELECT genre,
AVG(rating) AS AverageRating
FROM book
GROUP BY genre;
SELECT genre,
SUM(rating) AS TotalRating
FROM book
GROUP BY genre;
SELECT genre,
COUNT(*) AS TotalBooks
FROM book
GROUP BY genre
HAVING COUNT(*) > 2;
SELECT genre,
AVG(rating) AS AverageRating
FROM book
GROUP BY genre
HAVING AVG(rating) > 4.5;



