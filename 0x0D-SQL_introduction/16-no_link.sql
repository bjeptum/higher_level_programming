-- Lists all records of the second table --
SELECT score, name FROM second_table
WHERE name is not NULL
ORDER BY score DESC;
