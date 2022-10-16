CREATE TABLE customer (
  customer_id SERIAL PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  phone VARCHAR(20),
  email VARCHAR(75)
);

CREATE TABLE car (
  car_id SERIAL PRIMARY KEY,
  make VARCHAR(25),
  model VARCHAR(25),
  isNew BOOLEAN
);

CREATE TABLE employees (
  employee_id SERIAL PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  job_title VARCHAR(50)
);

CREATE TABLE service_ticket (
  service_ticket_id SERIAL PRIMARY KEY,
  employee_id INTEGER,
  customer_id INTEGER,
  car_id INTEGER,
  service_rendered VARCHAR(100),
  FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
  FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
  FOREIGN KEY (car_id) REFERENCES car(car_id)
);

CREATE TABLE invoice (
  invoice_id SERIAL PRIMARY KEY,
  employee_id INTEGER,
  customer_id INTEGER,
  car_id INTEGER,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
    FOREIGN KEY (car_id) REFERENCES car(car_id)
);