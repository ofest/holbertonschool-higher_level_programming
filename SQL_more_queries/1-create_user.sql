-- Creates the MySQL server user user_0d_1 (not fail if user exists)
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
SET PASSWORD FOR 'user_0d_1'@'localhost' = 'user_0d_1_pwd';
GRANT ALL ON * . * TO 'user_0d_1'@'localhost'
