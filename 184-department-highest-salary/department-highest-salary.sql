# Write your MySQL query statement below
SELECT d.name as Department,e.name as Employee,e.salary as Salary
FROM(SELECT name,salary,departmentId,
MAX(salary) OVER(PARTITION BY departmentId) as max_sal
FROM Employee) e JOIN Department d ON e.departmentId = d.id
WHERE e.salary = e.max_sal
