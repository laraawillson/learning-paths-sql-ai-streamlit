import random
import sqlite3
from datetime import date as calendar_date, timedelta
from pathlib import Path
from faker import Faker

# Seed both random generators so the same script produces the same dataset
# each time it runs. This makes development and debugging easier.
random.seed(15)
fake = Faker("en_US")
fake.seed_instance(15)

# Recreate the generated database from scratch on every run. This prevents
# old rows from mixing with the newly generated data.
database_path = "ecommerce.db"
database_file = Path(database_path)
if database_file.exists():
    database_file.unlink()

# Open the SQLite database and enable foreign-key checking for this connection.
connection = sqlite3.connect(database_path)
connection.execute("PRAGMA foreign_keys = ON")

# Create all tables by executing the SQL in schema.sql.
schema = Path("schema.sql").read_text()
connection.executescript(schema)

print("Database schema created")

# These lists and dictionaries are generation rules. They are used by Python
# to create values before those values are inserted into the database.

customer_segments = ["Basic","Standard", "Premium"]
product_catalog = [
    ("VertexBook Air 13", "Laptops", 699.99, 1299.99),
    ("OrbitFlex 2-in-1", "Laptops", 799.99, 1499.99),
    ("NovaPhone Ultra", "Smartphones", 799.99, 1399.99),
    ("VertexPhone Lite", "Smartphones", 249.99, 599.99),
    ("OrbitPhone Max", "Smartphones", 599.99, 999.99),
    ("NovaTab 11", "Tablets", 299.99, 799.99),
    ("VertexTab Mini", "Tablets", 199.99, 499.99),
    ("OrbitTab Pro", "Tablets", 499.99, 999.99),
    ("NovaView 27 4K", "Monitors", 249.99, 699.99),
    ("VertexView 34 Ultrawide", "Monitors", 499.99, 999.99),
    ("OrbitView 24", "Monitors", 149.99, 349.99),
    ("NovaSound Wireless", "Headphones", 79.99, 349.99),
    ("VertexBuds Pro", "Headphones", 99.99, 249.99),
    ("OrbitStudio ANC", "Headphones", 149.99, 399.99),
    ("NovaKey Mechanical", "Keyboards", 59.99, 199.99),
    ("VertexKey Compact", "Keyboards", 39.99, 129.99),
    ("OrbitBoard Wireless", "Keyboards", 49.99, 159.99),
    ("NovaGlide Wireless", "Mice", 29.99, 129.99),
    ("VertexTrack Pro", "Mice", 49.99, 149.99),
    ("OrbitMouse Silent", "Mice", 24.99, 79.99),
    ("NovaCam 4K", "Webcams", 69.99, 249.99),
    ("VertexCam Studio", "Webcams", 129.99, 299.99),
    ("OrbitCam HD", "Webcams", 39.99, 99.99),
    ("NovaRouter AX6000", "Networking", 149.99, 399.99),
    ("VertexMesh WiFi 6", "Networking", 199.99, 499.99),
    ("OrbitSwitch 16-Port", "Networking", 89.99, 249.99),
    ("NovaDrive 2TB SSD", "Storage", 89.99, 249.99),
    ("VertexVault 4TB", "Storage", 149.99, 399.99),
    ("OrbitFlash 256GB", "Storage", 19.99, 59.99),
    ("NovaHub USB-C", "Accessories", 39.99, 149.99),
    ("VertexCharge 65W", "Accessories", 29.99, 89.99),
    ("OrbitDock Pro", "Accessories", 99.99, 249.99),
    ("NovaWatch Active", "Wearables", 149.99, 399.99),
    ("VertexFit Band", "Wearables", 39.99, 129.99),
    ("OrbitWatch Pro", "Wearables", 299.99, 599.99),
    ("NovaCamera Mirrorless", "Cameras", 699.99, 1799.99),
    ("VertexCam Lens Kit", "Cameras", 299.99, 999.99),
    ("OrbitAction Cam", "Cameras", 149.99, 499.99),
    ("NovaPrint Color", "Printers", 129.99, 399.99),
    ("VertexLaser Pro", "Printers", 199.99, 599.99),
    ("OrbitPrint Compact", "Printers", 79.99, 199.99),
    ("NovaBeam Projector", "Projectors", 399.99, 1299.99),
    ("VertexCinema 4K", "Projectors", 699.99, 1999.99),
    ("OrbitMini Projector", "Projectors", 149.99, 499.99),
    ("NovaMic USB", "Audio", 59.99, 199.99),
    ("VertexMic Studio", "Audio", 149.99, 499.99),
    ("OrbitSoundbar", "Audio", 99.99, 399.99),
    ("NovaDrone Air", "Drones", 399.99, 999.99),
    ("VertexDrone Pro", "Drones", 799.99, 1999.99),
    ("OrbitMini Drone", "Drones", 99.99, 299.99)
]

# Keep inventory ranges realistic by category. For example, expensive drones
# usually have lower stock than inexpensive accessories.
stock_ranges = {
    "Laptops": (10, 100),
    "Smartphones": (20, 200),
    "Tablets": (15, 150),
    "Monitors": (10, 100),
    "Headphones": (30, 300),
    "Keyboards": (20, 200),
    "Mice": (25, 250),
    "Webcams": (25, 250),
    "Networking": (15, 150),
    "Storage": (30, 300),
    "Accessories": (50, 500),
    "Wearables": (20, 200),
    "Cameras": (5, 75),
    "Printers": (10, 100),
    "Projectors": (5, 60),
    "Audio": (15, 150),
    "Drones": (5, 50),
}

order_statuses = ["Completed","Pending","Cancelled"]

positive_review_texts = [
    "Great product, highly recommend!",
    "Excellent quality and performance.",
    "Very happy with my purchase.",
    "Would buy again.",
    "Good value for the price.",
    "Exactly as described."
]

negative_review_texts = [
    "Not satisfied with the quality.",
    "The product did not meet my expectations.",
    "The product arrived damaged.",
    "Poor value for the price.",
    "Would not buy again."
]

# All generated dates stay inside this window. ISO format (YYYY-MM-DD) also
# sorts correctly as text in SQLite.
start_date = calendar_date(2025,1, 1)
end_date = calendar_date.today()

# Build a reusable list of every allowed date.
date_list = []
current_date = start_date

while current_date <= end_date:
    date_list.append(current_date.isoformat())
    current_date += timedelta(days=1)


# These control the size of the generated dataset. The product count is tied
# to the catalog so every catalog entry becomes one product row.
customer_count = 1000
order_count = 5000
product_count = len(product_catalog)
review_count = 3000


#----------------Customer Data Generation----------------#

# Create a function to generate random customer data
def generate_customers(connection, count):
    # These lookups let later functions retrieve customer-specific values
    # without querying the database again.
    customer_registration_dates = {}
    customer_country_by_id = {}
    customers = []
    
    for customer_id in range(1, count + 1):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = (f"{first_name.lower()}.{last_name.lower()}"f".customer{customer_id}@example.com"
        )
        country = fake.country()
        registration_date = random.choice(date_list)
        customer_registration_dates[customer_id] = registration_date
        customer_segment = random.choices(customer_segments, weights = [60,30,10], k=1)[0]
        customer_country_by_id[customer_id] = country

        customers.append((
            customer_id,
            first_name,
            last_name,
            email,
            country,
            registration_date,
            customer_segment
            ))

    # Insert all customer rows in one batch after generating them.
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

    return customer_registration_dates, customer_country_by_id

# Generate products before orders because order items reference product IDs.
def generate_products(connection):
    products = []
    product_created_dates = {}
    product_prices_by_id = {}

    # Each catalog tuple contains a name, category, and price range. The
    # database stores only the generated price, not the range itself.
    for product_id, (product_name, category, minimum_price, maximum_price) in enumerate(product_catalog, start=1):
        price = round(random.uniform(minimum_price, maximum_price), 2)
        cost = round(price * random.uniform(0.5, 0.9), 2)
        minimum_stock, maximum_stock = stock_ranges[category]
        stock_quantity = random.randint(minimum_stock, maximum_stock)
        created_date = random.choice(date_list)

        # Keep these values by product ID so order items can use the exact
        # product price and enforce a valid order date later.
        product_prices_by_id[product_id] = price
        product_created_dates[product_id] = created_date

        products.append((
            product_id,
            product_name,
            category,
            price,
            cost,
            stock_quantity,
            created_date
            ))

    # Insert all products in one batch.
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

# Generate orders and order items together because each order total depends
# on the items selected for that order.
def generate_orders_and_items(connection, order_count, customer_registration_dates, customer_country_by_id, product_created_dates, product_prices_by_id):
    
    orders = []
    order_items = []
    next_order_item_id = 1

    for order_id in range(1, order_count + 1):
        # Choose an existing customer so the orders.customer_id foreign key is valid.
        customer_id = random.choice(list(customer_registration_dates.keys()))

        customer_registration_date = customer_registration_dates[customer_id]

        # Select unique products because order_items forbids duplicate
        # (order_id, product_id) pairs.
        selected_product_ids = random.sample(list(product_created_dates.keys()), random.randint(1, 5))  

        # An order cannot happen before the customer registered or before any
        # selected product existed.
        latest_product_created_date = max(product_created_dates[product_id] for product_id in selected_product_ids)
        earliest_order_date = max(customer_registration_date, latest_product_created_date)

        order_date = random.choice([d for d in date_list if d >= earliest_order_date])
        status = random.choices(order_statuses, weights=[80,15,5],k=1)[0]
        shipping_country = customer_country_by_id[customer_id]

        # Build each order item first so the order total can be calculated from
        # the same quantities, prices, and discounts that are stored below.
        total_amount = 0

        for product_id in selected_product_ids:
            quantity = random.randint(1, 10)
            unit_price = product_prices_by_id[product_id]
            discount_percentage = random.choice([0, 5, 10, 15])  

            # Round each line item before adding it so monetary values stay at
            # two decimal places throughout the calculation.
            item_total = round(
                quantity * unit_price * (1 - discount_percentage / 100),
                2
            )
            total_amount += item_total

            order_items.append((
                next_order_item_id,
                order_id,
                product_id,
                quantity,
                unit_price,
                discount_percentage
            ))
            next_order_item_id += 1

        orders.append((
            order_id,
            customer_id,
            order_date,
            round(total_amount, 2),
            status,
            shipping_country
        ))

    # Insert orders before order_items because order_items.order_id is a
    # foreign key that references orders.order_id.
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

    # Now that the parent orders exist, insert their item rows.
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

# Reviews are generated last because they reference both customers and
# products through completed orders.

def generate_reviews(connection, review_count):
    reviews = []

    # A customer can review a product only after buying it in a completed
    # order. GROUP BY also gives us one eligible row per customer/product pair.
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

    # Do not request more reviews than the number of unique eligible pairs.
    review_count = min(review_count, len(eligible_pairs))
    selected_pairs = random.sample(eligible_pairs, review_count)

    for review_id, (customer_id, product_id, latest_order_date) in enumerate(
        selected_pairs, 
        start=1
        ):
        review_date = random.choice([d for d in date_list if d >= latest_order_date])
        rating = random.choices(
            [1, 2, 3, 4, 5],
            weights=[3, 5, 12, 35, 45],
            k=1
        )[0]
        if rating > 3:
            review_text = random.choice(positive_review_texts)
        elif rating <=2:
            review_text = random.choice(negative_review_texts)
        else:
            review_text = None

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

# Generate parent tables first, then dependent tables.
customer_registration_dates, customer_country_by_id = generate_customers(
    connection, 
    customer_count
    )

product_created_dates, product_prices_by_id = generate_products(
    connection
    )

generate_orders_and_items(
    connection,
    order_count,
    customer_registration_dates,
    customer_country_by_id,
    product_created_dates,
    product_prices_by_id
)

generate_reviews(connection, review_count)

# Commit all inserts and close the connection cleanly.
connection.commit()
connection.close()
