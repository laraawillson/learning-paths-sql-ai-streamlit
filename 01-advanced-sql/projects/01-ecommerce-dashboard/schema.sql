/* This SQL script creates the necessary tables for the e-commerce dashboard project.
The tables include products, orders, and customers, each with relevant fields and constraints. 
*/

/* Enable foreign key support in SQLite */

PRAGMA foreign_keys = ON;

/*
The customers table stores information about the customers of the e-commerce platform, including their unique ID, name, email, country, registration date, and customer segment.
Create the customer table */

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    country TEXT NOT NULL,
    registration_date TEXT NOT NULL,
    customer_segment TEXT NOT NULL,
    CHECK (customer_segment IN ('Premium','Standard','Basic'))
    );

/*The product table stores information about the products available for sale on the e-commerce platform, including their unique ID, name, category, price, and stock quantity.
Create the product table */

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    cost REAL NOT NULL,
    stock_quantity INTEGER NOT NULL,
    created_date TEXT NOT NULL
    );

/*The orders table stores information about the orders placed by customers on the e-commerce platform, including their unique ID, customer ID, product ID, order date, quantity, and total price.
Create the orders table */

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date TEXT NOT NULL,
    total_amount REAL NOT NULL,
    status TEXT NOT NULL,
    shipping_country TEXT NOT NULL,
    CHECK (status IN ('Pending', 'Completed', 'Cancelled')),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    );

/* The order_items table stores information about the individual items included in each order, including their unique ID, order ID, product ID, quantity, and price.
Create the order_items table */

CREATE TABLE order_items (
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price REAL NOT NULL,
    discount_percent REAL NOT NULL,
    UNIQUE (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

/* The reviews table stores information about the reviews left by customers for products on the e-commerce platform, including their unique ID, customer ID, product ID, rating, review text, and review date.
Create the reviews table */

CREATE TABLE reviews (
    review_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    rating INTEGER NOT NULL,
    review_text TEXT,
    review_date TEXT NOT NULL,
    CHECK (rating BETWEEN 1 AND 5),
    UNIQUE (customer_id, product_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);