CREATE TABLE "Customer" (
  "customer_id" SERIAL,
  "first_name" VARCHAR(50),
  "last_name" VARCHAR(50),
  "email" VARCHAR(100),
  "phone" VARCHAR(25),
  PRIMARY KEY ("customer_id")
);

CREATE TABLE "Ticket" (
  "ticket_id" SERIAL,
  "customer_id" INTEGER,
  "movie_id" INTEGER,
  "staff_id" INTEGER,
  "date" VARCHAR(10),
  "time" VARCHAR(10),
  "price" INTEGER,
  PRIMARY KEY ("ticket_id")
);

CREATE TABLE "ConcessionStand" (
  "concession_id" SERIAL,
  "concession_name" VARCHAR(50),
  "registers" INTEGER,
  "isOpen" BOOLEAN,
  PRIMARY KEY ("concession_id")
);

CREATE TABLE "Movie" (
  "movie_id" SERIAL,
  "movie_name" VARCHAR(100),
  "movie_genre" VARCHAR(25),
  "movie_rating" VARCHAR(10),
  PRIMARY KEY ("movie_id")
);

CREATE TABLE "Staff" (
  "staff_id" SERIAL,
  "first_name" VARCHAR(50),
  "last_name" VARCHAR(50),
  "email" VARCHAR(100),
  "phone" VARCHAR(25),
  "concession_id" INTEGER,
  PRIMARY KEY ("staff_id"),
  CONSTRAINT "FK_Staff.concession_id"
    FOREIGN KEY ("concession_id")
      REFERENCES "ConcessionStand"("concession_id")
);

CREATE TABLE "Product" (
  "product_id" SERIAL,
  "product_brand" VARCHAR(50),
  "product_name" VARCHAR(50),
  "price" INTEGER,
  "concession_id" INTEGER,
  PRIMARY KEY ("product_id")
);