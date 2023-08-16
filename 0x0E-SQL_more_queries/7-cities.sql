-- Create a database 'hbtn_0d_usa' if it doesn't already exist
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE hbtn_0d_usa;
-- Create a table 'cities' if it doesn't already exist
CREATE TABLE IF NOT EXISTS `cities`
(
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE,
    state_id INT NOT NULL,
    name VARCHAR(256),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
