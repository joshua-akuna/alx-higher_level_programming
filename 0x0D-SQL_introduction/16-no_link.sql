-- the script lists all records of the table
-- second table of the database hbtn_0c_0.
-- rows without a name are not listed.
-- records are display in order of score and name.
-- records are listed in descending order of list.
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC
