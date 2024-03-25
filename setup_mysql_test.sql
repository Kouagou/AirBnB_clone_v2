-- A script that prepares a MySQL server for the project (Setup Test).
-- Create the database if not exists.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create a new user hbnb_test with hbnb_test_pwd.
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant all the privileges for hbnb_test user on hbnb_test_db database.
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grant SELECT privilege for hbnb_user on performance_schema.
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
