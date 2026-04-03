SELECT seller_name 
FROM seller s
WHERE seller_id NOT IN
(
    SELECT DISTINCT seller_id
    FROM orders
    WHERE sale_date BETWEEN '2020-01-01' AND '2020-12-31'
)
ORDER BY seller_name ASC