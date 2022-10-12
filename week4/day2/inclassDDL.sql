CREATE TABLE customer(
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(15),
    isPrime BOOLEAN,
    billing_address VARCHAR(100)
);

CREATE TABLE cart(
    cart_id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
    FOREIGN KEY (product_id) REFERENCES product(product_id)
);

CREATE TABLE product(
    product_id SERIAL PRIMARY KEY,
    price NUMERIC(10,2),
    brand VARCHAR(100),
    product_name VARCHAR(50)
);

-- In case cart table was created before product table.
-- ALTER TABLE cart
-- ADD FOREIGN KEY (product_id) REFERENCES product(product_id);

ALTER TABLE customer
DROP COLUMN first_name;

ALTER TABLE customer
ADD first_name VARCHAR(50) NOT NULL;

ALTER TABLE product
ALTER COLUMN product_name SET NOT NULL;