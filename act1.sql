-- Create table
CREATE TABLE employees (
    id INT,
    name VARCHAR(50),
    salary INT,
    department VARCHAR(50)
);

-- Insert sample data
INSERT INTO employees (id, name, salary, department) VALUES
(1, 'Alice', 40000, 'IT'),
(2, 'Bob', 25000, 'HR'),
(3, 'Ankit', 35000, 'IT'),
(4, 'Sara', 20000, 'Finance'),
(5, 'Amir', 30000, 'IT');

-- Query using different operators
SELECT 
    name,
    salary,
    salary * 12 AS annual_salary   -- Arithmetic operator
FROM employees
WHERE 
    salary >= 30000                -- Comparison operator
    AND department = 'IT'          -- Logical operator
    AND name LIKE 'A%'             -- Special operator (LIKE)
    OR salary IN (20000, 25000);   -- Special operator (IN)