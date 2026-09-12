import sqlite3
import random
from datetime import date as calendar_date, timedelta
from pathlib import Path

# Create the database and apply the schema 
database_path = "ecommerce.db"
database_file = Path(database_path)
if database_file.exists():
    database_file.unlink()

connection = sqlite3.connect(database_path)
connection.execute("PRAGMA foreign_keys = ON")

schema = Path("schema.sql").read_text()
connection.executescript(schema)

print("Database schema created")

#-----------------Define Record Counts-----------------#
customer_count = 1000
order_count = 5000
product_count = 500
review_count = 3000

#-----------------Data Generation Rules-----------------#

first_names = ["John", "Jane", "Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Jack", "Kathy", "Liam", "Mia", "Noah", "Olivia", "Paul", "Quinn", "Rachel"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"] 
customer_segments = ["Standard", "Premium", "Basic"]
countries = ["USA", "Canada", "UK", "Germany", "France", "Italy", "Spain", "Australia", "Brazil", "India"]
customer_segments = ["Standard", "Premium", "Basic"]
product_names = ["Laptop", "Smartphone", "Tablet", "Headphones", "Smartwatch", "Camera", "Printer", "Monitor", "Keyboard", "Mouse", "Speaker", "Router", "External Hard Drive", "USB Flash Drive", "Webcam", "Microphone", "Projector", "Drone", "VR Headset", "Fitness Tracker"]
product_categories = ["Electronics", "Accessories", "Gadgets", "Wearables", "Peripherals"]
product_prices = [999.99, 699.99, 399.99, 199.99, 299.99, 599.99, 149.99, 249.99, 29.99, 19.99, 79.99, 89.99, 129.99, 14.99, 179.99, 59.99, 349.99, 849.99, 349.99, 79.99, 49.99, 149.99, 199.99, 249.99, 299.99, 399.99, 499.99, 599.99, 699.99, 799.99]
order_statuses = ["Pending", "Completed","Cancelled"]
review_texts = [
    "Great product, highly recommend!",
    "Not satisfied with the quality.",
    "Excellent customer service.",
    "Fast shipping and good packaging.",
    "The product did not meet my expectations.",
    "Very happy with my purchase.",
    "Would buy again.",
    "The product arrived damaged.",
    "Good value for the price.",
    "The product is exactly as described.",
    None
]   

# Define a start and end date for generating random dates
start_date = calendar_date(2026, 1, 1)
end_date = calendar_date(2026, 12, 31)

# Generate a list of dates between start_date and end_date
date_list = []
current_date = start_date

# Loops through dates from start_date to end_date and appends them to the date_list
while current_date <= end_date:
    date_list.append(current_date.isoformat())
    current_date += timedelta(days=1)

#----------------Customer Data Generation----------------#

# Create a function to generate random customer data
def generate_customers(connection, count):

# Create a list to hold the generated customer data
    customer_registration_dates = {}
    customers = []

# Loop through ids from 1 to count and generate random customer data
    for customer_id in range(1, count + 1):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        email = f"{first_name.lower()}.{last_name.lower()}.customer{customer_id}@example.com"
        country = random.choice(countries)
        registration_date = random.choice(date_list)
        customer_registration_dates[customer_id] = registration_date
        customer_segment = random.choice(customer_segments)

# Append the generated customer data to the customers list
        customers.append((
            customer_id,
            first_name,
            last_name,
            email,
            country,
            registration_date,
            customer_segment
            ))

# Insert the generated customer data into the customers table
    connection.executemany(
        """
        INSERT INTO customers (
        customer_id, 
        first_name, 
        last_name, 
        email, 
        country, 
        registration_date, 
        customer_segment
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        customers
    )

    return customer_registration_dates

#----------------Product Data Generation----------------#

# Create a function to generate random product data
def generate_products(connection, count):

# Create a list to hold the generated product data
    products = []
    product_created_dates = {}
    product_prices_by_id = {}

# Loop through ids from 1 to count and generate random product data
    for product_id in range(1, count + 1):
        product_name = random.choice(product_names)
        category = random.choice(product_categories)
        price = random.choice(product_prices)
        product_prices_by_id[product_id] = price
        # Cost is a random percentage of the price
        cost = round(price * random.uniform(0.5, 0.9), 2)
        # Random stock quantity between 10 and 1500 
        stock_quantity = random.randint(10, 1500)
        created_date = random.choice(date_list)
        product_created_dates[product_id] = created_date

# Append the generated product data to the products list
        products.append((
            product_id,
            product_name,
            category,
            price,
            cost,
            stock_quantity,
            created_date
            ))

# Insert the generated product data into the products table
    connection.executemany(
        """
        INSERT INTO products (
        product_id, 
        product_name, 
        category, 
        price, 
        cost, 
        stock_quantity, 
        created_date
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        products
    )      

    return product_created_dates, product_prices_by_id

#----------------Order & Order Items Data Generation----------------#

# Create a function to generate random order & order items data
def generate_orders_and_items(connection, order_count, customer_registration_dates, product_created_dates, product_prices_by_id):
    
# Create a list to hold the generated order & order items data
    orders = []
    order_items = []
    next_order_item_id = 1

# Loop through ids from 1 to count and generate random order data
    for order_id in range(1, order_count + 1):
        # Randomly select a customer and an order date
        customer_id = random.choice(list(customer_registration_dates.keys()))

        # identifies the registration date of the selected customer
        customer_registration_date = customer_registration_dates[customer_id]

        # Randomly select a product
        selected_product_ids = random.sample(list(product_created_dates.keys()), random.randint(1, 5))  

        # identifies the latest product created date among the selected products and the earliest date for the order should be the later of the customer registration date and the latest product created date
        latest_product_created_date = max(product_created_dates[product_id] for product_id in selected_product_ids)
        earliest_order_date = max(customer_registration_date, latest_product_created_date)

        # Generate a random order date between the earliest_order_date and today
        order_date = random.choice([d for d in date_list if d >= earliest_order_date])
        status = random.choice(order_statuses)
        shipping_country = random.choice(countries)

        # Generate the order total amount based on the selected products and their prices

        total_amount = 0

        for product_id in selected_product_ids:
            quantity = random.randint(1, 10)
            unit_price = product_prices_by_id[product_id]
            discount_percentage = random.choice([0, 5, 10, 15])  

            # Calculate the total for this item considering the discount
            item_total = round(
                quantity * unit_price * (1 - discount_percentage / 100),
                2
            )
            total_amount += item_total

            # Append the generated order item data to the order_items list
            order_items.append((
                next_order_item_id,
                order_id,
                product_id,
                quantity,
                unit_price,
                discount_percentage
            ))
            next_order_item_id += 1

# Append the generated order data to the orders list
        orders.append((
            order_id,
            customer_id,
            order_date,
            round(total_amount, 2),
            status,
            shipping_country
        ))

# Insert the generated order data into the orders table
    connection.executemany(
        """
        INSERT INTO orders (
        order_id,
        customer_id,
        order_date,
        total_amount,
        status,
        shipping_country
        ) VALUES (?, ?, ?, ?, ?, ?)
        """,
        orders
    )

# Insert the generated order items into the order_items table
    connection.executemany(
        """
        INSERT INTO order_items (
        order_item_id,
        order_id,
        product_id,
        quantity,
        unit_price,
        discount_percent
        ) VALUES (?, ?, ?, ?, ?, ?)
        """,
        order_items
    )      

#----------------Review Data Generation----------------#

def generate_reviews(connection, review_count):
    reviews = []

    #Identify eligible orders for reviews (only completed orders) and select the latest order date for each customer-product pair
    eligible_pairs = connection.execute(
        """
        SELECT DISTINCT o.customer_id, oi.product_id, max(o.order_date)
        FROM orders o
        JOIN order_items oi 
            ON o.order_id = oi.order_id
        WHERE o.status = 'Completed'
        GROUP BY o.customer_id, oi.product_id
        """
    ).fetchall()    

    # Determine the number of reviews to generate, ensuring it does not exceed the number of eligible pairs
    review_count = min(review_count, len(eligible_pairs))
    selected_pairs = random.sample(eligible_pairs, review_count)

    # Generate reviews for the selected customer-product pairs
    for review_id, (customer_id, product_id, latest_order_date) in enumerate(
        selected_pairs, 
        start=1
        ):
        review_date = random.choice([d for d in date_list if d >= latest_order_date])
        rating = random.randint(1, 5)
        review_text = random.choice(review_texts)

        reviews.append((
            review_id,
            customer_id,
            product_id,
            rating,
            review_text,
            review_date
        ))

    connection.executemany(
        """
        INSERT INTO reviews (
            review_id,
            customer_id,
            product_id,
            rating,
            review_text,
            review_date
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        reviews
    )

# Call the function and generate 1000 customers
customer_registration_dates = generate_customers(
    connection, 
    customer_count
    )

# Call the function and generate 500 products
product_created_dates, product_prices_by_id = generate_products(
    connection, 
    product_count
    )

# Call the orders and order items generation function
generate_orders_and_items(
    connection,
    order_count,
    customer_registration_dates,
    product_created_dates,
    product_prices_by_id
)

generate_reviews(connection, review_count)

# Insert the generated data into the tables& close connection
connection.commit()
connection.close()
