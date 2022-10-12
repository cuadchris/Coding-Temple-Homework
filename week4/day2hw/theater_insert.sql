INSERT INTO "Customer"(
	"customer_id",
	"first_name",
	"last_name",
	"email",
	"phone"
)VALUES(
	1,
	'Chris',
	'Christopherson',
	'chris@templecoding.com',
	'(555)-555-5555'
);

INSERT INTO "Movie"(
    "movie_id",
    "movie_name",
    "movie_genre",
    "movie_rating"
)VALUES(
    1,
    'The Matrix',
    'suspense',
    'R'
);

INSERT INTO "ConcessionStand"(
    "concession_id",
    "concession_name",
    "registers",
    "isOpen"
)VALUES(
    1,
    'Popcorn, drinks, & candy',
    2,
    true
),(
    2,
    'Hot food',
    1,
    false
);

INSERT INTO "Staff"(
    "staff_id",
    "first_name",
    "last_name",
    "email",
    "phone",
    "concession_id"
)VALUES(
    1,
    'Shoha',
    'Tsuchida',
    'shoha@shoha.com',
    '(646)-646-4646',
    1
);

INSERT INTO "Ticket"(
    "ticket_id",
    "customer_id",
    "movie_id",
    "staff_id",
    "date",
    "time",
    "price"
)VALUES(
    1,
    1,
    1,
    1,
    '01/01/2001',
    '21:03',
    25.99
);

INSERT INTO "Product"(
    "product_id",
    "product_brand",
    "product_name",
    "price",
    "concession_id"
)VALUES(
    1,
    'MoviePops',
    'popcorn',
    67.99,
    1
),(
    2,
    'KFC',
    'chicken',
    12.95,
    2
);