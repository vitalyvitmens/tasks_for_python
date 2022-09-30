SELECT id, name, salary, manager_id, MAX(salary), COUNT(*) 
  FROM employees
  GROUP BY id, name, salary, manager_id;
  