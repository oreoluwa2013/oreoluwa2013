-- Create Products table
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50),
    Category VARCHAR(50),
    Price INT
);

-- Insert sample data
INSERT INTO Products (ProductID, ProductName, Category, Price)
VALUES
(1, 'Laptop', 'Electronics', 70000),
(2, 'Lamp', 'Home Decor', 1500),
(3, 'Mobile Phone', 'Electronics', 30000),
(4, 'Leather Bag', 'Fashion', 4500),
(5, 'Mouse', 'Electronics', 1200),
(6, 'Dining Table', 'Furniture', 15000);

-- Display all products
SELECT * FROM Products;

-- Using LIKE operator
SELECT * FROM Products
WHERE ProductName LIKE 'L%';

-- Using DISTINCT keyword
SELECT DISTINCT Category
FROM Products;

-- Sorting data by price (highest to lowest)
SELECT * FROM Products
ORDER BY Price DESC;

-- Filtering products with price greater than 5000
SELECT * FROM Products
WHERE Price > 5000;

-- Combining LIKE with sorting
SELECT * FROM Products
WHERE ProductName LIKE '%o%'
ORDER BY ProductName ASC;