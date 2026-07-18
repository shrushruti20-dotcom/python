CREATE TABLE IF NOT EXISTS restaurant (
    name TEXT,
    neighborhood TEXT,
    cuisine TEXT,
    review REAL,
    price TEXT,
    health TEXT
);
INSERT INTO restaurant (name,neighborhood,cuisine,review,price,health)
VALUES 
('peter','brooklyn','steak',4.4,'$$$','A'),
('jhon','midtown','korean',4.5,'$$$','A'),
('pocha','mostown','pizza',4.0,'$$','B'),
('lighthouse','queens','chinese',3.9,'$$','A'),
('ninca','downtown','american',4.6,'$$',''),
('marea','uptown','italian',4.9,'$$$$','B'),
('dirty candy','china town','chinese',3.0,'$$',''),
('pizza','midtown','pizza',3.8,'$$','A'),
('golden unicorn','uptown','italian',3.8,'$$','a');
SELECT DISTINCT neighborhood
FROM restaurant;
SELECT DISTINCT cuisine
FROM restaurant;

SELECT *
FROM restaurant
WHERE cuisine = 'chinese';

SELECT *
FROM restaurant
WHERE review >= 4.0;

SELECT *
FROM restaurant
WHERE cuisine = 'italian'
  AND price IN ('$$','$$$');

SELECT *
FROM restaurant
WHERE price = '$$$';

SELECT *
FROM restaurant
WHERE name LIKE '%candy%';

SELECT *
FROM restaurant
WHERE neighborhood IN ('midtown','downtown','chinatown');

SELECT *
FROM restaurant
WHERE health = '' OR health IS NULL;

SELECT *
FROM restaurant
ORDER BY review DESC
LIMIT 4;



SELECT *
FROM restaurant
WHERE cuisine = 'pizza';

SELECT *
FROM restaurant
ORDER BY review ASC
LIMIT 3;

SELECT *
FROM restaurant
WHERE name LIKE '%unicorn%';

SELECT *
FROM restaurant
WHERE name = 'peter';

SELECT *
FROM restaurant
WHERE health = 'B';

