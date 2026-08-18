use db_enterprise_data_analytics;
USE db_enterprise_data_analytics;

SHOW COLUMNS FROM products;
SHOW COLUMNS FROM customers;

SELECT COUNT(*) FROM customers;
SELECT COUNT(*) FROM orders;
SELECT COUNT(*) FROM products;
SELECT COUNT(*) FROM category_translation;
SELECT COUNT(*) FROM geolocation;
SELECT COUNT(*) FROM order_items;
SELECT COUNT(*) FROM payments;
SELECT COUNT(*) FROM reviews;
SELECT COUNT(*) FROM sellers;

SELECT COUNT(*) AS total_rows, COUNT(DISTINCT customer_id) AS unique_customer_id
FROM customers;

SELECT COUNT(*) AS total_rows, COUNT(DISTINCT order_id) AS unique_order_id
FROM orders;

SELECT COUNT(*) AS total_rows, COUNT(DISTINCT product_id) AS unique_product_id
FROM products;

SELECT COUNT(*) AS total_rows, COUNT(DISTINCT seller_id) AS unique_seller_id
FROM sellers;

SELECT COUNT(*)
FROM order_items
WHERE order_item_id IS NULL;
