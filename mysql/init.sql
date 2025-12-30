CREATE DATABASE IF NOT EXISTS microsservicos;
USE microsservicos;
CREATE TABLE logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    service VARCHAR(50),
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
