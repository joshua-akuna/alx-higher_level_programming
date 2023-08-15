-- the script lists all the records in the table second_table
-- of the database hbtn_0c_0 with score >= 10 in my MySQL server.
-- results should display in order score and name
-- records should be ordered by score in descending order
SELECT score, name 
FROM second_table 
WHERE score >= 10 
ORDER BY score DESC;
