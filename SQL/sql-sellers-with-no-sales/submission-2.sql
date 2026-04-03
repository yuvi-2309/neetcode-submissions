SELECT seller_name 
FROM seller s
WHERE seller_id NOT IN
(
    SELECT DISTINCT seller_id
    FROM orders
    WHERE EXTRACT(YEAR FROM sale_date) = 2020
)
ORDER BY seller_name ASC