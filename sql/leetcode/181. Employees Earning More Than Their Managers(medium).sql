#https://leetcode.com/problems/employees-earning-more-than-their-managers/description/
-- Write your PostgreSQL query statement below
SELECT e.name AS Employee
  FROM Employee e
  JOIN Employee m ON e.managerId = m.id
where e.salary > m.salary