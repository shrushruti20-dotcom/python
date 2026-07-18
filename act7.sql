CREATE TABLE salesman(
salesman_id INTEGER PRIMARY KEY,
name TEXT,
city TEXT,
commission REAL
);

CREATE TABLE customer(
customer_id INTEGER PRIMARY KEY,
customer_name TEXT,
city TEXT,
grade INTEGER,
salesman_id INTEGER
);

CREATE TABLE orders(
ord_no INTEGER PRIMARY KEY,
purch_amt REAL,
ord_date TEXT,
customer_id INTEGER,
salesman_id INTEGER
);

INSERT INTO salesman VALUES
(1,'JAMES','PARIS',0.15),
(2,'ADAM','PARIS',0.13),
(3,'PAUL','ROME',0.11),
(4,'NAIL','ITALY',0.15),
(5,'ALEX','LONDON',0.13);

INSERT INTO customer VALUES 
(101,'NICK','NEW YORK',100,1),
(102,'DAVIS','PARIS',200,1),
(103,'JOHN','ITALY',200,3),
(104,'GREEN','LONDON',300,2),
(105,'GRAHAM','ROME',NULL,6);

INSERT INTO orders VALUES 
(201,150.5,'2024-01-10',103,2),
(202,65.56,'2024-01-10',101,1),
(203,2480.5,'2024-04-15',104,2),
(204,110.5,'2024-03-20',102,1);

SELECT customer.customer_name,
salesman.name,
customer.city
FROM customer
JOIN salesman
ON customer.city=salesman.city;
SELECT customer.customer_name,
salesman.name
FROM customer
JOIN customer
ON cutomer.salesman_id=salesman.salesman_id;
SELECT orders.ord_no,
customer.customer_name,
customer.city,
salesman.city
FROM orders
JOIN customer
On orders.customer_id=customer.customer_id
JOIN salesman
ON orders.salesman_id=salesman.salesman_id
WHERE customer.city<>salesman.city;

SELECT orders.ord_no,
order.purch_amt,
customer.customer_name
FROM orders 
JOIN customer
ON orders.customer_id=customer.customer_id;

SELECT customer_name,
grade
FROM customer
WHERE grade IS NOT NULL;

SELECT customer.customer_name,
salesman.name,
salesman.commission
FROM customer
JOIN salesman
ON customer.salesman_id=salesman.salesman_id 
WHERE commission BETWEEN 0.13 AND 0.14;

SELECT customer.customer_name,
orders.purch_amt,
salesman.commission,
orders.purch_amt * salesman.commission AS commissionamount
FROM orders 
JOIN customer
ON orders.customer_id=customer.customer_id
JOIN salesman
ON orders.salesman_id=salesman.salesman_id
WHERE customer.grade>=200;