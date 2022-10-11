SELECT *
FROM actor;

-- Query first and last name
SELECT first_name, last_name
FROM actor;

-- Query actors whos name is NICK
SELECT first_name, last_name
FROM actor
WHERE first_name = 'Nick';

-- use the LIKE clause
SELECT last_name
FROM actor
WHERE first_name LIKE 'Nick';

-- looking for names that START with the letter J
-- % is the wildcard
SELECT first_name
FROM actor
WHERE first_name LIKE 'J%';

-- limit the number of chars
-- single char wildcard
SELECT first_name
FROM actor
WHERE first_name like 'J__';

-- using both wildcards
SELECT first_name
FROM actor
WHERE first_name LIKE 'K__%th';

-- comparing operators
-- >
-- <
-- >=
-- <=
-- <> (Not equal to)

-- explore the payment table
SELECT *
FROM payment;

-- find customers who paid more than $10
SELECT customer_id, amount
FROM payment
WHERE amount >= 10.00;

SELECT first_name
FROM customer
WHERE customer_id = 341;

-- query for customer who paid more than $2 
-- in ascending order ( ASC )
-- by default, it is already in ascending order
SELECT customer_id, amount
FROM payment
WHERE amount >= 2.00
ORDER BY amount DESC;

-- find customers who paid between 4.00 and 7.99. ***Both numbers are inclusive. Will Start at 4.00 and end at 7.99***
SELECT customer_id, amount
FROM payment
WHERE amount BETWEEN 4.00 AND 7.99;

-- SQL Aggregation => SUM(), AVG(), MIN(), MAX(), COUNT()
-- display sum of amount greater than 5.99
SELECT SUM(amount)
FROM payment
WHERE amount > 5.99;

-- display averages
SELECT AVG(amount)
FROM payment;

SELECT COUNT(*)
FROM payment;

SELECT MAX(amount) AS most_expensive_item
FROM payment;

SELECT customer_id, SUM(amount)
FROM payment
GROUP BY customer_id
ORDER BY SUM(amount) DESC;

SELECT amount, COUNT(*)
FROM payment
GROUP BY amount
ORDER BY COUNT(*) DESC;