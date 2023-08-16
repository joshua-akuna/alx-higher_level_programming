-- creates the database htbn_0d_usa and table states in hbtn_0d_usa
-- creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use the database hbtn_0d_usa
USE hbtn_0d_usa;
-- create the table states
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(256) NOT NULL);
