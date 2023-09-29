-- Retrieve the 'id' and 'name' columns from the 'cities' table (aliased as 'a')
SELECT a.id AS id, a.name AS city_name, b.name AS state_name
FROM cities a
INNER JOIN states b
ON a.state_id = b.id
ORDER BY a.id ASC;
