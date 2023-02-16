-- Displays the top 3 of cities temperature during July and August--
SELECT city , AVG(value) AS average_temp
FROM temperatures
WHERE month = 7 or month = 8
GROUP BY city
ORDER BY average_temp DESC
LIMIT 3;
