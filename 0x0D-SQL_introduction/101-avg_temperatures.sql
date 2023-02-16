-- Imports table and displays average city's temperature in descending order--
SELECT city , AVG(value) AS average_temp
FROM temperatures
GROUP BY city
ORDER BY average_temp DESC;
