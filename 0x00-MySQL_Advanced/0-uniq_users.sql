-- Check if the database exists
CREATE DATABASE IF NOT EXISTS holberton;

-- Use the holberton database
USE holberton;

-- Check if the table exists
DELIMITER //

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
)//

DELIMITER ;
