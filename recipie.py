import sqlite3
import pandas as pd
conn = sqlite3.connect(':memory:')
conn.execute("CREATE TABLE recipe (recipe_id INTEGER PRIMARY KEY,recipe_name TEXT NOT NULL,cuisine TEXT NOT NULL,prep_mins INTEGER NOT NULL)")
conn.execute("CREATE TABLE ingredient(ingredient_id INTEGER PRIMARY KEY,recipe_id INTEGER NOT NULL,item TEXT NOT NULL,quantity_g INTEGER NOT NULL)")
conn.executemany("INSERT INTO recipe VALUES (?,?,?,?)",[

    (1,'PASTA','ITALIAN',20),
    (2,'TACOS','MEXICAN',15),
    (3,'SUSHI','JAPANESE',45)
    (4,'PIZZA','ITALIAN',30)
    (5,'SALAD','GREEK',10)
])

conn.executemany("INSERT INTO ingredient VALUES (?,?,?,?)",[
    (1,2,'pasta',200),
    (2,1,'sauce',150),
    (3,2,'tortilla',80),
    (4,2,'beef',120),
    (5,3,'salmon',180),
    (6,4,'dough',250),
    (7,5,'lettuce',50),
    (8,5,'feta',40),
])

print("Recipe table:")
print(pd.read_sql("SELECT * FROM recipe",conn))
print()
print("INGREDIENT table")
print(pd.read_sql("SELECT * FROM ingredient",conn))
print()

col_alias = pd.read_sql(
    "SELECT recipe_name AS dish,cuisine AS style,prep_mins"
    "FROM recipe",
    conn
)
print("column aliases -- dish,style,time:")
print(col_alias)
print()
tbl_alias= pd.read_sql(
    "SELECT r.recipe_name AS dish,ing.item,ing.quantity_g AS grams"
    "FROM recipe AS r"
    "INNER JOIN ingredient AS ing"
    "ON r,recipe_id = ing.recipe_id",
    conn 
)

print("Table aliases == r for recipe ,ing for ingredient:")
print(tbl_alias)
print()

large_ingr = pd.read_sql(
    "SELECT recipe_name AS dish,cuisine AS style"
    "FROM recipe"
    "WHERE recipe_id IN("
    "SELECT recipe_id FROM ingredient WHERE quantity_g > 100"
    ")",
    conn

)
print("Subquery with IN -- recipes with an ingredient over 100g:")
print(large_ingr)
print()
quickest = pd.read_sql(
    "SELECT recipe_name AS dish,prep_mins AS time"
    "FROM recipe"
    "WHERE prep_mins = (SELECT Min(prep_mins) FROM recipe)",
    conn
)
print("subquery with = -- the quickest recipe to prepare :")
print(quickest)
conn.close()

