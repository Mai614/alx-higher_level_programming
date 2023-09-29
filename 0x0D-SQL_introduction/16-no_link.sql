--a script that lists all records of the table second_table of the database
-- rows with a name value
SELECT score, name FROM second_table WHERE name!='' OR name IS NOT NULL ORDER BY score DESC;
