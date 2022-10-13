-- 1. List all customers who live in Texas (use JOINs)
SELECT first_name, last_name, district
FROM customer
INNER JOIN address
ON customer.address_id = address.address_id
WHERE district = 'Texas';

-- 2. Get all payments above $6.99 with the Customer's Full Name
SELECT first_name, last_name, amount
FROM customer
INNER JOIN payment
ON customer.customer_id = payment.customer_id
WHERE amount > 6.99;

-- Same thing but using GROUP BY to avoid seeing the same names over and over. 
-- This gives you the names and how many of their payments are above $6.99. 
SELECT first_name, last_name, COUNT(*)
FROM customer
INNER JOIN payment
ON customer.customer_id = payment.customer_id
WHERE amount > 6.99
GROUP BY first_name, last_name, amount
ORDER BY COUNT(*) DESC;

-- 3. Show all customers names who have made payments over $175(use subqueries)
SELECT first_name, last_name
FROM customer
WHERE customer_id in (
    SELECT customer_id
    FROM payment
    WHERE amount > 175
);

-- 4. List all customers that live in Nepal (use the city table)
SELECT first_name, last_name
FROM customer
WHERE address_id in (
    SELECT address_id
    FROM address
    WHERE city_id in (
        SELECT city_id
        FROM city
        WHERE country_id in(
            SELECT country_id
            FROM country
            WHERE country = 'Nepal'
)));

-- 5. Which staff member had the most transactions?
-- I wasn't sure whether to use payment or rental table. Sometimes an employee who helps you isn't the
-- same one who rings you up at the register. I went with rental.
SELECT first_name, last_name
FROM staff
WHERE staff_id in (
    SELECT staff_id
    FROM rental
    GROUP BY staff_id
    ORDER BY COUNT(*) DESC
    LIMIT 1
);

-- 6. How many movies of each rating are there?
SELECT rating, COUNT(*)
FROM film
GROUP BY 1 ORDER BY COUNT(*) DESC;

-- 7.Show all customers who have made a single payment above $6.99 (Use Subqueries)
SELECT first_name, last_name
FROM customer
WHERE customer_id in (
    select customer_id
    from payment
    where amount > 6.99
    GROUP by customer_id
    ORDER by COUNT(*)
);

-- 8. How many free rentals did our stores give away?
SELECT *
FROM payment
WHERE amount <= 0; -- This will give you 30 results where the payment was negative, lol. I'm going to 
-- consider that free! haha.