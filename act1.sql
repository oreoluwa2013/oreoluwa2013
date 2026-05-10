-- Create Employee table
CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    Name VARCHAR(50),
    Department VARCHAR(50),
    Salary INT
);

-- Insert sample data
INSERT INTO Employees (EmpID, Name, Department, Salary)
VALUES
(1, 'John', 'HR', 45000),
(2, 'Sara', 'IT', 60000),
(3, 'Mike', 'Finance', 52000),
(4, 'Emma', 'IT', 75000),
(5, 'David', 'HR', 40000);

-- SELECT statement
SELECT * FROM Employees;

-- WHERE clause
SELECT * FROM Employees
WHERE Department = 'IT';

-- MIN function
SELECT MIN(Salary) AS MinimumSalary
FROM Employees;

-- MAX function
SELECT MAX(Salary) AS MaximumSalary
FROM Employees;

-- Employees with salary greater than 50000
SELECT * FROM Employees
WHERE Salary > 50000;