CREATE TABLE IF NOT EXISTS zoo_animal(
    animal_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    ageyears INTEGER NOT NULL,
    weight_kg REAL NOT NULL
);
INSERT INTO zoo_animal VALUES
(1,'lion','big cat',8,190),
(2,'tiger','big cat',5,220),
(3,'elephant','pachyderm',12,5400),
(4,'giraffe','ungulate',7,800),
(5,'penguin','bird',3,30),
(6,'panda','bear',6,120),
(7,'cheetah','big cat',4,65),
(8,'rhino','pachyerm',9,1340);
SELECT * FROM zoo_animal;
SELECT species
FROM zoo_animal;
SELECT DISTINCT species
FROM zoo_animal;
SELECT COUNT(DISTINCT species) AS UniqueSpecies
FROM zoo_animal;
SELECT COUNT(animal_id) AS TotalAnimals
FROM zoo_animal;
SELECT COUNT(animal_id) AS OlderThanFive
FROM zoo_animal
WHERE age_years > 5;
SELECT SUM(weight_kg) AS TotalWeight
FROM zoo_animal;
SELECT AVG(age_years) AS AverageAge
FROM zoo_animal;
SELECT
    COUNT(animal_id) AS TotalAnimals,
    COUNT(DISTINCT species)AS UniqueSpecies,
    SUM(weight_kg) AS TotalWeight,
    AVG(age_years) AS  AverageAge
FROM zoo_animal;
SELECT COUNT(animal_id) AS HeavyAnimals
FROM zoo_animal
WHERE weight_kg > 200;
SELECT SUM(weight_kg) AS BigCatWeight
FROM zoo_animal
WHERE species = 'big cat';
SELECT AVG(weight_kg) AS AverageWeight
FROM zoo_animal;
SELECT COUNT(*) AS BigCatCount
FROM zoo_animal
WHERE species = 'big cat';
SELECT DISTINCT name
FROM zoo_animal;




