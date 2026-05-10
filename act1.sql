-- Create a table
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT,
    Course VARCHAR(50),
    Marks INT
);

-- Insert data into the table
INSERT INTO Students (StudentID, Name, Age, Course, Marks)
VALUES
(1, 'Alice', 20, 'SQL Basics', 85),
(2, 'Bob', 21, 'SQL Basics', 72),
(3, 'Charlie', 19, 'Database Systems', 90),
(4, 'David', 22, 'SQL Basics', 65),
(5, 'Emma', 20, 'Database Systems', 88);

-- Display all records
SELECT * FROM Students;

-- Manipulate data (Update marks)
UPDATE Students
SET Marks = 80
WHERE StudentID = 2;

-- Delete a record
DELETE FROM Students
WHERE StudentID = 4;

-- Sort data by marks (highest to lowest)
SELECT * FROM Students
ORDER BY Marks DESC;

-- Filter data (students scoring above 80)
SELECT * FROM Students
WHERE Marks > 80;

-- Count total students
SELECT COUNT(*) AS TotalStudents
FROM Students;

-- Average marks
SELECT AVG(Marks) AS AverageMarks
FROM Students;