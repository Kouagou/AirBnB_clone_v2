-- A script that prepares a MySQL server for the project (Setup Development).
-- Create the database if not exists.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create a new user hbnb_dev with hbnb_dev_pwd.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant all the privileges for hbnb_dev user on hbnb_dev_db database.
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grant SELECT privilege for hbnb_user on performance_schema.
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
