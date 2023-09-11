-- Create a database 'hbtn_0d_usa' if it doesn't already exist
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
-- Switch to the 'hbtn_0d_usa' database
USE hbtn_0d_usa;
-- Create a table 'states' if it doesn't already exist
CREATE TABLE IF NOT EXISTS `states`
(
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE,
    name VARCHAR(256)
);
