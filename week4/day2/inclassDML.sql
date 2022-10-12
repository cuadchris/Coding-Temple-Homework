SELECT * FROM customer;

INSERT INTO customer (
    first_name,
    last_name,
    email,
    phone,
    isPrime,
    billing_address
)
VALUES (
    'Shoha',
    'Tsuchida',
    'shoha@shoha.com',
    '(646)626-6262',
    true,
    '123 real St, Boston MA'
);

-- inserting multiple entries with all columns
INSERT INTO customer (
    first_name,
    last_name,
    email,
    phone,
    isPrime,
    billing_address
)
VALUES (
    'Chris',
    'Cuadrado',
    'chris@chris.com',
    '(347)626-6262',
    true,
    '100 real St, Bronx NY'
);

INSERT INTO product(
    price,
    brand,
    product_name
)
VALUES (
    10.99,
    'Apple',
    'iPhone 6'
);

INSERT INTO cart(customer_id, product_id)
VALUES(1,1),(1,1),(2,1);