# Write your MySQL query statement below
SELECT eu.unique_id as unique_id, em.name as name
FROM EmployeeUNI eu RIGHT JOIN Employees em ON eu.id = em.id
