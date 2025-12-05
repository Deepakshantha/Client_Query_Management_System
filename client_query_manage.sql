DROP DATABASE IF EXISTS client_query_db;
CREATE DATABASE client_query_db;
USE client_query_db;

DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
  user_id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(150) UNIQUE NOT NULL,
  hashed_password VARCHAR(128) NOT NULL,
  role ENUM('Client','Support') NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS queries (
  query_id INT AUTO_INCREMENT PRIMARY KEY,
  mail_id VARCHAR(255) NOT NULL,
  mobile_number VARCHAR(50),
  query_heading VARCHAR(255) NOT NULL,
  query_description TEXT,
  status ENUM('Open','Closed') DEFAULT 'Open',
  query_created_time DATETIME DEFAULT CURRENT_TIMESTAMP,
  query_closed_time DATETIME NULL
);

select * from queries;

select * from users;

ALTER TABLE queries 
MODIFY status VARCHAR(20) DEFAULT 'Open';



LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/synthetic_client_queries (1).csv"
INTO TABLE queries
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(mail_id, mobile_number, query_heading, query_description, status, query_created_time, query_closed_time);








