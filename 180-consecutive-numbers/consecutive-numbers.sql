# Write your MySQL query statement below
SELECT DISTINCT num as ConsecutiveNums
FROM(SELECT num,lead1,
LEAD(lead1) OVER () as lead2
FROM(SELECT 
num,
LEAD(num) OVER () as lead1
FROM Logs)a)a
WHERE num = lead1 and lead2 = num and lead1 = lead2

