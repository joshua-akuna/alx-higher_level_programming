-- the scripts creates the table called first_table in
-- the current database in my MySQL server.
-- the script will not fail if the table already exists
CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256))
