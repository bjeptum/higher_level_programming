-- Lsts all the cities of California that can be found in the database --
SLECT id, name
FROM cities
WHERE state_id IN (
    SELECT id
    FROM states
    WHERE name = "California")
ORDER BY id ASC;
