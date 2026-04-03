SELECT u.name, 
    CASE WHEN
        SUM(r.distance) > 0 THEN SUM(r.distance) ELSE 0
        END AS travelled_distance
FROM users u
LEFT JOIN rides r
ON r.user_id = u.id
GROUP BY u.id, u.name 
ORDER BY travelled_distance DESC, name ASC