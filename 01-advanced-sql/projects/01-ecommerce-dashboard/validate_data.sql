SELECT COUNT(*)
FROM reviews;

SELECT COUNT(*)
FROM reviews
WHERE rating NOT BETWEEN 1 AND 5;

SELECT customer_id, product_id, COUNT(*)
FROM reviews
GROUP BY customer_id, product_id
HAVING COUNT(*) > 1;