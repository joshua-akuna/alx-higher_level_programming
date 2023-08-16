-- the scripts creates the MySQL server user user_0d_1
--	user_0d_1 should have all privileges on the server
--	password should be set to user_0d_1_pwd
CREATE USER IF NOT EXIST user_0d_1@localhost
IDENTIFIED BY user_0d_1_pwd;
GRANT ALL
PRIVILEGES ON *.*
FOR user_0d_1@localhost;
