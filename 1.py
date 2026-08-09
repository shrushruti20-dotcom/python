import sqlite3
import pandas as pd

conn = sqlite3.connect('wildlife_park.db')
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS Animal;
DROP TABLE IF EXISTS Keeper;
DROP TABLE IF EXISTS Animal_Keeper;

CREATE TABLE Animal (
    Animal_Id     INTEGER PRIMARY KEY,
    Animal_Name   TEXT,
    Animal_Type   TEXT,
    Habitat       TEXT,
    Age           INTEGER,
    Food_Kg       REAL
);

CREATE TABLE Keeper (
    Keeper_Id     INTEGER PRIMARY KEY,
    Keeper_Name   TEXT,
    Country       TEXT
);

CREATE TABLE Animal_Keeper (
    Animal_Id  INTEGER,
    Keeper_Id  INTEGER
);

INSERT INTO Animal VALUES
  (1,'Leo','Mammal','Savannah',8,7.5),
  (2,'Maya','Mammal','Savannah',5,6.0),
  (3,'Ella','Bird','Rainforest',4,1.5),
  (4,'Rio','Bird','Rainforest',3,1.2),
  (5,'Tara','Reptile','Wetland',10,2.0),
  (6,'Max','Mammal','Forest',6,4.5),
  (7,'Nina','Mammal','Forest',2,3.0),
  (8,'Ollie','Bird','Wetland',7,1.8),
  (9,'Zara','Reptile','Desert',9,2.5);
  

INSERT INTO Keeper VALUES
  (1,'Aarav', 'India'),
  (2,'Diya', 'India'),
  (3,'Meera', 'Kenya'),
  (4,'Kabir', 'Australia'),
  (5,'Riya', 'India');

INSERT INTO Animal_Keeper VALUES
  (1,1),(2,1),(3,2),(4,2),(5,3),
  (6,4),(7,4),(8,3),(9,5);
""")

conn.commit()
print('Wildlife park database ready!')
animal_types = pd.read_sql("""SELECT DISTINCT(Animal_Type)
    FROM Animal;""", conn)
print(animal_types)
habitats = pd.read_sql("""SELECT DISTINCT(Habitat)
    FROM Animal;""", conn)
print(habitats)
oldest_animals = pd.read_sql("""SELECT Animal_Name, Animal_Type, Age
    FROM Animal
    ORDER BY Age DESC;""", conn)
print(oldest_animals)
food_order = pd.read_sql("""SELECT Animal_Name, Food_Kg
    FROM Animal
    ORDER BY Food_Kg;""", conn)
print(food_order)
mammal_count = pd.read_sql("""SELECT COUNT(Animal_Id)
    FROM Animal
    WHERE Animal_Type == 'Mammal';""", conn)
print(mammal_count)
bird_food = pd.read_sql("""SELECT SUM(Food_Kg)
    FROM Animal
    WHERE Animal_Type == 'Bird';""", conn)
print(bird_food)
average_age = pd.read_sql("""SELECT AVG(Age)
    FROM Animal;""", conn)
print(average_age)
animals_per_habitat = pd.read_sql("""SELECT Habitat, COUNT(Animal_Id)
    FROM Animal
    GROUP BY Habitat;""", conn)
print(animals_per_habitat)

conn.close()
