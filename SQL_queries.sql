-- ---------------------------------------
-- 1. Create Database
-- ---------------------------------------
CREATE DATABASE student_performance_db;

-- ---------------------------------------
-- 2. Use Database
-- ---------------------------------------
USE student_performance_db;

-- ---------------------------------------
-- 3. Create Table
-- ---------------------------------------
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(10),
    math INT,
    science INT,
    programming INT,
    attendance INT
);

-- ---------------------------------------
-- 4. Insert Data
-- ---------------------------------------
INSERT INTO students VALUES
(1,'Amit','CS',78,85,90,92),
(2,'Riya','CS',88,79,85,90),
(3,'Karan','IT',65,70,72,80),
(4,'Pooja','IT',92,91,95,96),
(5,'Rahul','CS',55,60,58,70),
(6,'Neha','IT',75,80,78,88),
(7,'Rohit','CS',60,65,70,75),
(8,'Sneha','IT',82,85,80,92),
(9,'Arjun','CS',90,88,92,95),
(10,'Kavya','IT',70,72,68,85),
(11,'Vikas','CS',50,55,52,65),
(12,'Anjali','IT',85,87,90,93),
(13,'Deepak','CS',67,70,65,78),
(14,'Meera','IT',91,89,94,97),
(15,'Suresh','CS',72,75,78,82),
(16,'Priya','IT',68,72,70,80),
(17,'Manish','CS',58,60,62,72),
(18,'Divya','IT',88,90,85,94),
(19,'Nitin','CS',77,80,79,88),
(20,'Simran','IT',83,85,82,91);

-- ---------------------------------------
-- 5. Display All Student Records
-- ---------------------------------------
SELECT * FROM students;

-- ---------------------------------------
-- 6. Calculate Average Marks of Each Student
-- ---------------------------------------
SELECT 
    student_id,
    name,
    department,
    (math + science + programming) / 3 AS average_marks
FROM students;

-- ---------------------------------------
-- 7. Identify Top-Performing Student
-- ---------------------------------------
SELECT 
    name,
    (math + science + programming) / 3 AS average_marks
FROM students
ORDER BY average_marks DESC
LIMIT 1;

-- ---------------------------------------
-- 8. Department-wise Average Marks
-- ---------------------------------------
SELECT 
    department,
    AVG((math + science + programming) / 3) AS dept_average
FROM students
GROUP BY department;

-- ---------------------------------------
-- 9. Students Scoring Below 60
-- ---------------------------------------
SELECT 
    name,
    (math + science + programming) / 3 AS average_marks
FROM students
WHERE (math + science + programming) / 3 < 60;

-- ---------------------------------------
-- 10. Overall Class Average
-- ---------------------------------------
SELECT 
    AVG((math + science + programming) / 3) AS overall_average
FROM students;

-- ---------------------------------------
-- 11. At-Risk Students (Extra for High Marks)
-- ---------------------------------------
SELECT 
    name,
    department,
    (math + science + programming) / 3 AS average_marks,
    attendance,
    CASE 
        WHEN (math + science + programming) / 3 < 60 OR attendance < 75 THEN 'At Risk'
        ELSE 'Safe'
    END AS status
FROM students;

-- ---------------------------------------
-- 12. Sort Students by Highest Average Marks
-- ---------------------------------------
SELECT 
    name,
    (math + science + programming) / 3 AS average_marks
FROM students
ORDER BY average_marks DESC;

-- ---------------------------------------
-- 13. Top 5 Students
-- ---------------------------------------
SELECT 
    name,
    (math + science + programming) / 3 AS average_marks
FROM students
ORDER BY average_marks DESC
LIMIT 5;