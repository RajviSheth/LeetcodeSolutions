# Write your MySQL query statement below
SELECT class
FROM 
(SELECT class, COUNT(student) AS count_students
FROM Courses
GROUP BY class) AS temp
WHERE count_students >= 5;