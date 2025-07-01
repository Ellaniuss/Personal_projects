-- creating database
CREATE DATABASE IF NOT EXISTS HGSM_database


-- selecting database
USE hgsm_database

-- creating tables
CREATE TABLE IF NOT EXISTS groceries (
	item_id INT PRIMARY KEY AUTO_INCREMENT,
	product_id INT,
	quantity INT,
	unit_id INT,
	bought_date DATE,
	expiration_date DATE,
	location_id INT,
	is_consumed BOOLEAN
	)
	
CREATE TABLE IF NOT EXISTS products (
	product_id INT PRIMARY KEY AUTO_INCREMENT,
	product_name VARCHAR(30),
	category_id INT,
	default_unit_id INT,
	default_quantity INT,
	average_price FLOAT,
	notes varchar(255)
)


CREATE TABLE IF NOT EXISTS categories (
	category_id INT PRIMARY KEY AUTO_INCREMENT,
	category_name VARCHAR(30)
)

CREATE TABLE locations (
	location_id INT PRIMARY KEY AUTO_INCREMENT,
	location_name varchar(255),
	location_type VARCHAR(255)
)

CREATE TABLE units (
	unit_id INT PRIMARY KEY AUTO_INCREMENT,
	unit_name VARCHAR(255),
	unit_abbreviation VARCHAR(10)
)	

-- creating relations
ALTER TABLE products
ADD CONSTRAINT fk_groceries_category
FOREIGN KEY (category_id) REFERENCES categories(category_id)

ALTER TABLE products
ADD CONSTRAINT fk_groceries_units
FOREIGN KEY (default_unit_id) REFERENCES units(unit_id)

ALTER TABLE groceries
ADD CONSTRAINT fk_products_groceries
FOREIGN KEY (product_id) REFERENCES products(product_id)

ALTER TABLE products
ADD CONSTRAINT uq_product_name UNIQUE (product_name)

-- inserting basic values
INSERT INTO units(unit_name, unit_abbreviation)
VALUES
	('kus', 'pcs'),
	('litr', 'l'),
	('mililitr', 'ml'),
	('kilogram', 'kg'),
	('gram', 'g')
	
INSERT INTO locations(location_name, location_type)
VALUES
	('lednice-police1', 'chlazene'),
	('lednice-police2', 'chlazene'),
	('lednice-police3', 'chlazene'),
	('lednice-suplik1', 'chlazene'),
	('lednice-suplik2', 'chlazene'),
	('lednice-dvere1', 'chlazene'),
	('lednice-dvere2', 'chlazene'),
	('lednice-dvere3', 'chlazene'),
	('mrazak-suplik1', 'mrazene'),
	('mrazak-suplik2', 'mrazene'),
	('mrazak-suplik3', 'mrazene'),
	('spiz-police1', 'police'),
	('spiz-police2', 'police'),
	('spiz-police3', 'police'),
	('spiz-police4', 'police'),
	('spiz-police5', 'police'),
	('skrinka1-police1', 'police'),
	('skrinka1-police2', 'police'),
	('skrinka1-police3', 'police'),
	('skrinka2-police1', 'police'),
	('skrinka2-police2', 'police'),
	('skrinka2-police3', 'police'),
	('skrinka3-police1', 'police'),
	('skrinka3-police2', 'police'),
	('skrinka3-police3', 'police'),
	('skrinka4-police1', 'police'),
	('skrinka4-police2', 'police'),
	('skrinka4-police3', 'police'),
	('sklep', 'police'),
	('neroztrizeno', 'mimo-kategorie')
	

	
