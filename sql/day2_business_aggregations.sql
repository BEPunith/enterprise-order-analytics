-- total orders in the system
SELECT COUNT(*) AS total_orders FROM orders;

-- total revenue from all payments
SELECT SUM(payment_value) AS total_revenue FROM order_payments;

-- average payment value
SELECT AVG(payment_value) AS avg_payment_value FROM order_payments;

-- how many orders per status
SELECT order_status, COUNT(*) AS order_count
FROM orders
GROUP BY order_status
ORDER BY order_count DESC;

-- states with more than 1000 customers
SELECT customer_state, COUNT(*) AS total_customers
FROM customers
GROUP BY customer_state
HAVING COUNT(*) > 1000
ORDER BY total_customers DESC;

-- revenue split by payment type
SELECT payment_type, SUM(payment_value) AS total_revenue
FROM order_payments
GROUP BY payment_type
ORDER BY total_revenue DESC;