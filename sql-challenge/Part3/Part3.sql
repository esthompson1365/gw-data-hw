--Cartesian_Joins
--Part 1
SELECT COUNT(*) FROM country
SELECT COUNT(*) FROM city

SELECT COUNT(*)
FROM country, city;

--The command above will create a row for every city, country combination.
--In our example there are 25 rows in one table and 10 in the other. 10 x 25 = 250 rows

--Part 2
CREATE TABLE table_1 (
	id INTEGER);
	
INSERT INTO table_1 (id)
VALUES
   (1),
   (2),
   (3),
   (4);
   
CREATE TABLE table_2 (
	id INTEGER);
	
INSERT INTO table_2 (id)
VALUES
   (10),
   (11),
   (12);

SELECT * FROM table_1, table_2;

--Foreign_Key
SELECT 
	e.employee_id,
 	e.first_name,
	e.last_name,
	e.department_id,
	d.dept_name
FROM employees e
JOIN departments d
ON (e.department_id = d.id)
WHERE e.department_id = 45;

--Alter_Update
--Alter changes the structure of a table (e.g., column names) whereas update changes data in the table
--Change column name
ALTER TABLE table
RENAME COLUMN department_id TO dept_id;

--Add new column
ALTER TABLE table
ADD COLUMN annual_salary INTEGER;

--Case
DROP TABLE animals

CREATE TABLE animals (
	id SERIAL,
	animal_name VARCHAR,
	species VARCHAR
);
	
INSERT INTO animals (animal_name,species)
VALUES
   ('Mickey Mouse','Cat'),
   ('Minie Mouse','Mouse'),
   ('Donald Duck','Bird');

SELECT * FROM animals

UPDATE animals
    SET species = (CASE WHEN animal_name='Mickey Mouse' THEN 'Mouse' 
                          WHEN animal_name='Donald Duck' THEN 'Duck'
                          ELSE species
                     END);

SELECT * FROM animals

--SQL_Joins

--INNER JOIN: Returns records that have matching values in both tables
--LEFT JOIN: Returns all records from the left table, and the matched records from the right table
--RIGHT JOIN: Returns all records from the right table, and the matched records from the left table
--FULL JOIN: Returns all records when there is a match in either left or right table

--A FULL JOIN was used to create the output in the HW because Cascade Yarns is a vendor in 2 rows and Tahki was included despite not having yarn.
