-- Retrieve the 'id' and 'name' columns from the 'cities' table
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name="California")
ORDER BY id ASC;
