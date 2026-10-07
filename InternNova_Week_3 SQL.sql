CREATE DATABASE internnova_db;

USE internnova_db;

-- Departments table
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

INSERT INTO departments VALUES
(1, 'IT'),
(2, 'HR'),
(3, 'Sales'),
(4, 'Finance');

-- Employees table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    department_id INT,
    salary DECIMAL(10,2),
    city VARCHAR(50),
    age INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

INSERT INTO employees VALUES
(101, 'Amit', 1, 60000, 'Pune', 25),
(102, 'Priya', 2, 45000, 'Mumbai', 28),
(103, 'Rahul', 1, 75000, 'Pune', 30),
(104, 'Sneha', 3, 50000, 'Kolhapur', 24),
(105, 'Rohan', 3, 65000, 'Pune', 27),
(106, 'Neha', 4, 55000, 'Mumbai', 26),
(107, 'Kiran', 1, 80000, 'Nashik', 32),
(108, 'Pooja', 2, 48000, 'Pune', 23);

-- Products table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(50),
    price DECIMAL(10,2)
);

INSERT INTO products VALUES
(201, 'Laptop', 'Electronics', 60000),
(202, 'Mouse', 'Electronics', 800),
(203, 'Keyboard', 'Electronics', 1500),
(204, 'Chair', 'Furniture', 5000),
(205, 'Desk', 'Furniture', 10000),
(206, 'Headphones', 'Electronics', 2500);

-- Sales table
CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    employee_id INT,
    product_id INT,
    quantity INT,
    sale_amount DECIMAL(10,2),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO sales VALUES
(1, 101, 201, 2, 120000),
(2, 102, 202, 5, 4000),
(3, 103, 203, 4, 6000),
(4, 104, 204, 3, 15000),
(5, 105, 205, 2, 20000),
(6, 106, 206, 4, 10000),
(7, 101, 202, 10, 8000),
(8, 103, 201, 1, 60000);
SELECT * 
FROM employees;
SELECT employee_id, employee_name, salary
FROM employees;
SELECT 
    employee_name AS Name,
    salary AS Salary
FROM employees;
SELECT 
    employee_name AS Employee_Name,
    city AS Location
FROM employees;
SELECT *
FROM employees
WHERE salary > 50000;
SELECT *
FROM employees
WHERE city = 'Pune';
SELECT *
FROM employees
WHERE age >= 25 AND age <= 30;
SELECT employee_name, salary
FROM employees
ORDER BY salary DESC;
SELECT COUNT(*) AS Total_Employees
FROM employees;
SELECT SUM(salary) AS Total_Salary
FROM employees;
SELECT AVG(salary) AS Average_Salary
FROM employees;
SELECT MIN(salary) AS Minimum_Salary
FROM employees;
SELECT MAX(salary) AS Maximum_Salary
FROM employees;
SELECT 
    department_id,
    COUNT(*) AS Employee_Count
FROM employees
GROUP BY department_id;
SELECT 
    department_id,
    AVG(salary) AS Average_Salary
FROM employees
GROUP BY department_id;
SELECT 
    department_id,
    SUM(salary) AS Total_Salary
FROM employees
GROUP BY department_id;
SELECT 
    department_id,
    COUNT(*) AS Employee_Count
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 1;
SELECT 
    d.department_name,
    COUNT(e.employee_id) AS Employee_Count,
    AVG(e.salary) AS Average_Salary
FROM departments d
JOIN employees e
ON d.department_id = e.department_id
GROUP BY d.department_name
HAVING COUNT(e.employee_id) > 1;
SELECT 
    e.employee_id,
    e.employee_name,
    d.department_name,
    e.salary
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id;
SELECT 
    d.department_name,
    e.employee_name,
    e.salary
FROM departments d
LEFT JOIN employees e
ON d.department_id = e.department_id;
SELECT 
    d.department_name,
    e.employee_name,
    e.salary
FROM employees e
RIGHT JOIN departments d
ON e.department_id = d.department_id;
SELECT 
    employee_name,
    salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
SELECT AVG(salary)
FROM employees
SELECT 
product_name,
    price
FROM products
WHERE price > (
    SELECT AVG(price)
    FROM products
);
    employee_name,
    salary
FROM employees
WHERE salary = (
    SELECT MAX(SELECT 
salary)
    FROM employees
);
SELECT 
    employee_name,
    salary
FROM employees
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
);