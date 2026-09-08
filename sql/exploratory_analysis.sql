-- checking what order statuses we actually have
SELECT DISTINCT order_status FROM orders;

-- what payment types are used
SELECT DISTINCT payment_type FROM order_payments;

-- which states our customers are from
SELECT DISTINCT customer_state FROM customers;

-- orders that got purchased but never approved, need to check why
SELECT order_id, order_purchase_timestamp
FROM orders
WHERE order_approved_at IS NULL;

-- payments above 1000, just checking high value orders
SELECT order_id, payment_type, payment_value
FROM order_payments
WHERE payment_value > 1000;