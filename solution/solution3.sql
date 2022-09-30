SELECT id AS id
    , name
	, salary
	, manager_id, COUNT(*) FROM employees WHERE manager_id
GROUP BY manager_id
ORDER BY 
	id ASC
