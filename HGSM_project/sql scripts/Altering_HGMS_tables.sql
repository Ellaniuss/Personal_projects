ALTER TABLE groceries 
ADD notes varchar(255)

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

