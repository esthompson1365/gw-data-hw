--unite 3 tables and hard code values in one column
CREATE VIEW all_parties AS
SELECT
   first_name,
   last_name,
   'actor' AS record_type
FROM
   actor
UNION
SELECT
   first_name,
   last_name,
   'customer' AS record_type
FROM
   customer
UNION
SELECT
   first_name,
   last_name,
   'staff' AS record_type
FROM
   staff
   

-- all customer in london using junction and union
SELECT
	customer.customer_id,
	city.city
FROM
	customer
LEFT JOIN address
	ON address.address_id = customer.address_id
LEFT JOIN city
	ON address.city_id = city.city_id
WHERE
	city.city = 'London'
UNION
SELECT
   id AS customer_id,
   city
FROM
   customer_list
WHERE
	city = 'London'
	
