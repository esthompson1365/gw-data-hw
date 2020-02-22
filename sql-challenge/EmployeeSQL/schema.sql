-- Drop table if exists
DROP TABLE employees;
-- employees
CREATE TABLE employees (
	emp_no INT PRIMARY KEY,
	birth_date DATE,
	first_name VARCHAR,
	last_name VARCHAR,
	gender VARCHAR,
	hire_date DATE
);

SELECT * FROM employees

-- departments
DROP TABLE departments;

CREATE TABLE departments (
	dept_no VARCHAR PRIMARY KEY,
	dept_name VARCHAR
);

SELECT * FROM departments

-- dept_emp
DROP TABLE dept_emp;

CREATE TABLE dept_emp (
	emp_no INTEGER REFERENCES employees(emp_no),
	dept_no VARCHAR REFERENCES departments(dept_no),
	from_date DATE,
	to_date DATE
);

SELECT * FROM dept_emp

-- dept_manager
DROP TABLE dept_manager;

CREATE TABLE dept_manager (
	dept_no VARCHAR REFERENCES departments(dept_no),
	emp_no INTEGER REFERENCES employees(emp_no),
	from_date DATE,
	to_date DATE
);

SELECT * FROM dept_manager

-- titles
DROP TABLE titles;

CREATE TABLE titles (
	emp_no INTEGER REFERENCES employees(emp_no),
	title VARCHAR,
	from_date DATE,
	to_date DATE
);

SELECT * FROM titles

-- salaries
DROP TABLE salaries;

CREATE TABLE salaries (
	emp_no INTEGER REFERENCES employees(emp_no),
	salary INTEGER,
	from_date DATE,
	to_date DATE
);

SELECT * FROM salaries

-- List 1: employee number, last name, first name, gender, and salary.
SELECT
		employees.emp_no,
		employees.last_name,
		employees.first_name,
		employees.gender,
		salaries.salary
FROM
		employees
		JOIN salaries
		ON employees.emp_no = salaries.emp_no
		
-- List 2: employees who were hired in 1986.
SELECT last_name,first_name,hire_date
FROM Employees
WHERE 
	hire_date >= '1986-01-01' AND
	hire_date <= '1986-12-31';
	
-- List 3: manager of each department
SELECT
		dept_manager.dept_no,
		departments.dept_name,
		dept_manager.emp_no,
		employees.last_name,
		employees.first_name,
		dept_manager.from_date,
		dept_manager.to_date
FROM
	dept_manager
LEFT JOIN departments
	ON dept_manager.dept_no = departments.dept_no
LEFT JOIN employees
	ON dept_manager.emp_no = employees.emp_no
	
-- List 4: department of each employee
SELECT
	employees.emp_no,
	employees.last_name,
	employees.first_name,
	departments.dept_name
FROM
	dept_emp
RIGHT JOIN employees
	ON dept_emp.emp_no = employees.emp_no
LEFT JOIN departments
	ON dept_emp.dept_no = departments.dept_no	

-- List 5: employees whose first name is "Hercules" and last names begin with "B."
SELECT
	emp_no,
	last_name,
	first_name
FROM
	employees
WHERE
	first_name = 'Hercules'
AND
	last_name LIKE 'B%'
	
-- List 6: employees in the Sales department
SELECT
	employees.emp_no,
	employees.last_name,
	employees.first_name,
	departments.dept_name
FROM
	dept_emp
RIGHT JOIN employees
	ON dept_emp.emp_no = employees.emp_no
LEFT JOIN departments
	ON dept_emp.dept_no = departments.dept_no	
WHERE 
	departments.dept_name = 'Sales'

-- List 7: employees in the Sales or Development department
SELECT
	employees.emp_no,
	employees.last_name,
	employees.first_name,
	departments.dept_name
FROM
	dept_emp
RIGHT JOIN employees
	ON dept_emp.emp_no = employees.emp_no
LEFT JOIN departments
	ON dept_emp.dept_no = departments.dept_no	
WHERE 
	departments.dept_name = 'Sales'
OR
	departments.dept_name = 'Development'
	
-- List 8: frequency count of employee last names
SELECT 
   last_name, COUNT(last_name) 
FROM 
   employees
GROUP BY
	last_name