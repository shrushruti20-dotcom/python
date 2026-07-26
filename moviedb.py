import sqlite3
import pandas as pd
conn = sqlite3.connect('movie.db')
cursor = conn.cursor()
cursor.executescript("""
DROP TABLE IF EXISTS movie;
DROP TABLE IF EXISTS actor;
DROP TABLE IF EXISTS movie_actor;



CREATE TABLE movie (
    movie_id INTEGER PRIMARY KEY,
    title TEXT,
    genre TEXT,
    year  TEXT,
    rating REAL,
    duration INTEGER
    );
CREATE TABLE actor(
    actor_id INTEGER PRIMARY KEY,
    actor_name TEXT,
    birth_year INTEGER,
    state TEXT
    );

CREATE TABLE movie_actor(
    movie_id INTEGER,
    actor_id INTEGER
    );

INSERT INTO movies VALUES
(1,'Theri','Action',2017,8.5,88),
(2,'The lion king',Animation,1994,8.5,87),
(3,'Spider man','action',2014,7.9,103),
(4,'dude','comedy',2026,8,98),
(5,'coco','animation',2017,8.6,160),
(6,'elf','comedy',2003,8.6,169),
(7,'Frozen','Animation',2013,7.4,102),
(8,'sarvam maya','drama',2025,9.2,107),
(9,'moana','animation,'2013,8.7,104),
(10,'Lik','drama',2025,8.6,97),
(11,'toy story','animation',1995,8.3,82),
(12,'leo','action',2023,9.4,108);


INSERT INTO actor VALUES
(1,'Tom hanks',1956,'USA'),
(2,'vijay',1978,'tamil nadu),
(3,'meryl streep',1949,'USA'),
(4,'nivin pauly','1987','kerala'),
(5,'Pradeep','2011','tamil nadu'),
(6,'Priyanka',1982,'India),
(7,'Jackie chan','1954,'china'),
(8,'Lupita nyongo',1982,'Kenya'),
(9,'Will smith',1968,'USA'),
(10,'Riya',2008,'kerala');


INSERT INTO movie_actor VALUES
  (1,2),(2,1),(5,1),(6,3),
  (6,8),(2,2),(8,2),(8,7),(9,5),(11,2);
""")

conn.commit()
print('Database ready!')
genres = pd.read_sql("""SELECT DISTICT(genre)
    FROM movie;""",conn)
print(genres)

countries = pd.read_sql("""SELECT DISTINCT(country)
    FrOM actor;""",conn)
print(countries)
top_movies = pd.read_sql("""SELECT title,genre,rating
    FROM movie
    ORDER BY rating DESC;""",conn)
print(top_movies)

oldest_first = pd.read_sql("""SELECT title,year
    FROM movie
    ORDER BY year;""",conn)
print(oldest_first)


youngest_actors = pd.read_sql("""SELECT actor_name,birth_year,state
    FROM actor
    ORDER BY birth_year DESC;""",conn)
print(youngest_actors)

action_count = pd.read_sql("""SELECT COUNT(movie_id
    FROM movie
    WHERE genre == 'action';""",conn)
print(action_count)

animation_mins = pd.read_sql("""SELECT SUM(duration)
    FROM movie
    WHERE genre == 'animation',""",conn)
print(animation_mins)

