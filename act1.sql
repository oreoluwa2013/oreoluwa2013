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

-- Use aggregate functions
SELECT 
    COUNT(*) AS total_employees,      -- Count rows
    SUM(salary) AS total_salary,      -- Add salaries
    AVG(salary) AS average_salary,    -- Average salary
    MAX(salary) AS highest_salary,    -- Maximum salary
    MIN(salary) AS lowest_salary      -- Minimum salary
FROM employees;

-- Aggregate with GROUP BY
SELECT 
    department,
    COUNT(*) AS num_employees,
    AVG(salary) AS avg_salary
FROM employees
GROUP BY department;