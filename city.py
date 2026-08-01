import sqlite3
import pandas as pd
conn = sqlite3.connect("cities.db")
conn.execute("DROP TABLE IF EXISTS CITY;")
conn.execute("""
CREATE TABLE city(
    city_id INTEGER PRIMARY KEY,
    city_name TEXT NOT NULL UNIQUE,
    country TEXT NOT NULL,
    popluation INTEGER,
    is_capital TEXT DEFAULT 'no'

);
""")

conn.commit()
print("Table created successfully!\n")
conn.execute("INSERT INTO VALUES (1,'tokyo','japan',136900000,'yes')")
conn.execute("INSERT INTO VALUES (2,'nairobi','kenya','4398000,'yes)")
conn.execute("INSERT INTO VALUES (3,'mumbai','india',12240000,'no')")
conn.execute("INSERT INTO VALUES (4,'sao paulo','brazil',1230000,'no')")
conn.execute("INSERT INTO VALUES (5,'london','united kingdom',89820000,'yes')")

conn.execute("""
INSERT INTO city(city_id,city_name,country)
VALUES (6,'sydney','australia')
""")

conn.commit()


print("intial table")
print(pd.read_sql("SELECT * FROM city;",conn))
print()

try:
    conn.execute("""
    INSERT INTO city
    VALUES (1,'cairo','egypt',21320000,'yes')
     """)
    conn.commit()
except Exception as e:
    conn.rollback()
    print("PRIMARY KEY test")
    print("REjected:",e)
    print("city_id 1 alreaedy exists.\n")

try:
    conn.execute("""
    INSERT INTO city
    VALUES(7,'berlin',NULL,3645000,'yes')
    """)
except Exception as e:
    conn.rollback()
    print("NOT NULL text")
    print("rejected:",e)
    print()


try:
    conn.execute("""
    INSERT INTO city
    VALUES (8,'tokyo','japan',99999,'no')""")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("UNIQUE test")
    print("rejected:",e)
    print()
print("Sydney record (DEFAULT value)")
sydney = pd.read_sql("""
SELECT city_name,country,population,is_capital
FROM city
WHERE city_name = 'sydney';
""",conn)


print(sydney)
print()

print("ALL cities")
all_data = pd.read_sql("""
SELECT city_name,country,population
FROM city;
""",conn)

print(all_data)
print()

print("cities with NULL population")
missing = pd.read_sql("""
SELECT city_name
FROM city
WHERE population IS NULL;""",conn)

print(missing)
print()

print("Cities with population data")
available = pd.read_sql("""
SELECT city_name,population
FROM city
WHERE population IS NOT NULL;""",conn)

print(available)

conn.close()
print("\n Database connection closed")