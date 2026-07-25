import sqlite3
import pandas as pd
conn = sqlite3.connect('cricket.db')
cursor = conn.cursor()
cursor.executescript("""
DROP TABLE IF EXISTS Team;
DROP TABLE IF EXISTS Match;
DROP TABLE IF EXISTS player_match;
                     
CREATE TABLE Team(
    Team_id INTEGER PRIMARY KEY,
    Team_Name TEXT  
);

CREATE TABLE Match(
    match_id INTEGER PRIMARY KEY,
    season_id INTEGER,
    match_winner INTEGER,
    win_margin INTEGER
);

CREATE TABLE player_match(
    match_id INTEGER,
    player_id INTEGER
);
    
INSERT INTO Team VALUES
(1,'Royal Challengers Bengaluru'),(2,'Mumbai Indians'),(3,'Chennai super kings');
(4,'Delhi cappitals'),(5,'Punjab kings'),(6,'Rajasthan Royals'),
(7,'Kolkata knight riders' ),(8,'Gujarat titans') ;

INSERT INTO match VALUES
(1,18,37,8),(1,21,25,35),(7,8,31,48),(12,23,3,4),(56,67,78,89),
(6,7,8,44),(7,18,19,17),(11,1,2,3),(44,53,55,61),(77,100,18,79),(13,14,15,16),
(44,67,37,36);

INSERT INTO player_match VAlUES
(1,101),(1,102),(2,103),(3,101),(4,104),(5,102);
""")
conn.commit()
print("Database ready")
tables = pd.read_sql("""SELECT *
    FROM sqlite_master
    WHERE type='table';""",conn)
print(tables)
matches = pd.read_sql("""SELECT *
    FROM match;""",conn)
print(matches)
print('Rows and coloumns:',matches.shape)


teams = pd.read_sql("""SELECT *
    FROM teams;""",conn)
print(teams)

team_names = pd.read_sql("""SELECT team_id,team_name
    FROM team;""",conn)
print(team_names)

player_matches = pd.read_sql("""SELECT team_id,player_id
    FROM player_match;""",conn)
print(player_matches)

rcb_wins = pd.read_sql("""SELECT *
    FROM match
    WHERE match_winner == 1;""",conn)
print(rcb_wins)

mi_recent = pd.read_sql("""SELECT *
    FROM match
    WHERE match_winner == 5 AND season_id IN (8,9);""",conn)
print(mi_recent)
de_teams = pd.read_sql("""SELECT *
    FROM team
    WHERE team_name LIKE 'de%';""",conn)
print(de_teams)

