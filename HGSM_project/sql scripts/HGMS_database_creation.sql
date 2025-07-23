-- creating database
CREATE DATABASE IF NOT EXISTS HGSM_database


-- creating tables

CREATE TABLE IF NOT EXISTS categories (
	id INT PRIMARY KEY AUTO_INCREMENT,
	category_name VARCHAR(30) NOT NULL,
	UNIQUE(category_name)
)
	
CREATE TABLE IF NOT EXISTS units (
	id INT PRIMARY KEY AUTO_INCREMENT,
	unit_name VARCHAR(255) NOT NULL,
	unit_abbreviation VARCHAR(10) NOT NULL,
	UNIQUE(unit_abbreviation)
)
	
CREATE TABLE IF NOT EXISTS locations (
	id INT PRIMARY KEY AUTO_INCREMENT,
	location_name varchar(255) NOT NULL,
	location_type VARCHAR(255) NOT NULL
)

CREATE TABLE IF NOT EXISTS products (
	id INT PRIMARY KEY AUTO_INCREMENT,
	product_name VARCHAR(30) NOT NULL,
	category_id INT,
	default_unit_id INT NOT NULL,
	default_quantity INT NOT NULL,
	average_price DECIMAL(10,2),
	notes varchar(255),
	FOREIGN KEY (category_id) REFERENCES categories(id),
	FOREIGN KEY (default_unit_id) REFERENCES units(id)
)
	
CREATE TABLE IF NOT EXISTS groceries (
	id INT PRIMARY KEY AUTO_INCREMENT,
	product_id INT NOT NULL,
	quantity INT NOT NULL DEFAULT 1,
	unit_id INT NOT NULL,
	bought_date DATE,
	expiration_date DATE,
	location_id INT NOT NULL,
	is_consumed BOOLEAN NOT NULL DEFAULT FALSE,
	FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
	FOREIGN KEY (unit_id) REFERENCES units(id) ON DELETE CASCADE,
	FOREIGN KEY (location_id) REFERENCES locations(id) ON DELETE CASCADE
	)
	
CREATE TABLE IF NOT EXISTS shopping_list (
	id INT PRIMARY KEY AUTO_INCREMENT,
	product_id INT NOT NULL,
	quantity INT NOT NULL DEFAULT 1,
	unit_id INT NOT NULL,
	added_date DATETIME DEFAULT CURRENT_TIMESTAMP,
	purchased BOOLEAN  NOT NULL DEFAULT FALSE,
	purchased_date DATETIME,
	removed BOOLEAN NOT NULL DEFAULT FALSE,
	FOREIGN KEY (product_id) REFERENCES products(id),
	FOREIGN KEY (unit_id) REFERENCES units(id)
)

