SELECT manager_id, COUNT(*) FROM employees
  GROUP BY manager_id
  HAVING COUNT(*) > 0;
  