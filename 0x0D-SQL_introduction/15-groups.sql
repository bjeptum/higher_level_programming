-- Lists records with the same score from the second_table --
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score ORDER BY number DESC
