# jobs/00_load_mysql.py

import pandas as pd
import mysql.connector
import os
from dotenv import load_dotenv

# ── LOAD ENVIRONMENT VARIABLES ───────────────────
# This reads your .env file
# Loads all KEY=VALUE pairs into memory
load_dotenv()

# Now read values from environment
MYSQL_HOST     = os.getenv("MYSQL_HOST")
MYSQL_PORT     = int(os.getenv("MYSQL_PORT"))
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_USER     = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

# ── DATABASE CONNECTION ───────────────────────────
conn = mysql.connector.connect(
    host     = MYSQL_HOST,
    port     = MYSQL_PORT,
    database = MYSQL_DATABASE,
    user     = MYSQL_USER,
    password = MYSQL_PASSWORD
)
cursor = conn.cursor()
print("✅ Connected to MySQL!")

# ── FILE PATHS ────────────────────────────────────
DATA_PATH = "data/"

tables = {
    "customers":            "olist_customers_dataset.csv",
    "sellers":              "olist_sellers_dataset.csv",
    "products":             "olist_products_dataset.csv",
    "orders":               "olist_orders_dataset.csv",
    "order_items":          "olist_order_items_dataset.csv",
    "payments":             "olist_order_payments_dataset.csv",
    "reviews":              "olist_order_reviews_dataset.csv",
    "geolocation":          "olist_geolocation_dataset.csv",
    "category_translation": "product_category_name_translation.csv",
}

# ── LOAD EACH TABLE ───────────────────────────────
for table_name, file_name in tables.items():

    file_path = os.path.join(DATA_PATH, file_name)
    print(f"\nLoading {table_name} from {file_name}...")

    df = pd.read_csv(file_path)
    df = df.where(pd.notnull(df), None)

    print(f"  Rows to load: {len(df)}")

    cursor.execute(f"TRUNCATE TABLE {table_name}")

    cols         = ", ".join(df.columns)
    placeholders = ", ".join(["%s"] * len(df.columns))
    sql          = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"

    batch_size = 1000
    rows       = [tuple(row) for row in df.values]

    for i in range(0, len(rows), batch_size):
        batch = rows[i:i + batch_size]
        cursor.executemany(sql, batch)
        conn.commit()
        print(f"  Inserted rows {i} to {i + len(batch)}")

    print(f"✅ {table_name} loaded: {len(df)} rows")

print("\n🎉 All 9 tables loaded into MySQL!")
cursor.close()
conn.close()