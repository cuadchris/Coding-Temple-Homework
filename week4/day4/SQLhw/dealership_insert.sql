INSERT INTO customer (
  customer_id,
  first_name,
  last_name,
  phone,
  email
)VALUES(
    1,
    'Chris',
    'Christopherson',
    '(646)-464-6464',
    'chris@christopherson.com'
),(
    2,
    'Spongebob',
    'Squarepants',
    '(646)-456-5464',
    'bikini@bottom.com'
);

INSERT INTO employees (
  employee_id,
  first_name,
  last_name,
  job_title
)VALUES(
    1,
    'Shoha',
    'Shohason',
    'mechanic'
),(
    2,
    'Brandt',
    'Brandtson',
    'salesman'
);

-- Stored function

CREATE FUNCTION add_car(
    id INTEGER,
    make VARCHAR(25),
    model VARCHAR(25),
    isNew BOOLEAN
)
RETURNS VOID
LANGUAGE plpgsql
AS
$MAIN$
BEGIN
    INSERT INTO car(car_id, make, model, isNew)
    VALUES(id, make, model, isnew);
END
$MAIN$
;
SELECT add_car(1, 'chevy', 'cobalt', false);
SELECT add_car(2, 'honda', 'civic', true);
SELECT add_car(3, 'hyundai', 'sonata', false);
SELECT add_car(4, 'ford', 'escort', false);
SELECT add_car(5, 'acura', 'crv', true);

INSERT INTO service_ticket (
  service_ticket_id,
  employee_id,
  customer_id,
  car_id,
  service_rendered
)VALUES(
    1,
    1,
    1,
    1,
    'tune-up'
),(
    2,
    1,
    1,
    1,
    'wash'
);

INSERT INTO invoice (
  invoice_id,
  employee_id,
  customer_id,
  car_id
)VALUES(
    1,
    2,
    2,
    2
),(
    2,
    2,
    2,
    5
);