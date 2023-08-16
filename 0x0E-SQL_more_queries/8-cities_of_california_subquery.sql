-- lists all the cities of california found in the database hbtn_0d_usa
-- the states table contains only one record where name = California
-- results are sorted in ascending order by cities.id
SELECT id, name 
FROM cities 
WHERE state_id = (SELECT id 
	FROM states 
	WHERE name = 'California') 
ORDER BY id ASC;
