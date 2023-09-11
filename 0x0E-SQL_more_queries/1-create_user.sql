-- Create a new user 'user_0d_1' with a password 'user_0d_1_pwd' on the 'localhost' host
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_1'@'localhost';
