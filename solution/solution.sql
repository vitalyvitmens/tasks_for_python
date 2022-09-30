SELECT -- после слова SELECT мы описываем что конкретно мы выбираем (перечисление колонок, какие то операции над ними)
	id AS id
	, name AS name
	, salary AS salary
	, manager_id AS manager_id
FROM -- после FROM мы описываем откуда мы выбираем конкретное название одной таблицы в данном случае employees, 
     -- можно перечислять несколько таблиц и взаимодействовать между ними
	employees
WHERE -- где (WHERE), условие выборки, что бы выбор попал в финальную выборку это условие должно выполняться
    manager_id is not NULL
ORDER BY -- сортировка: ASC с меньшего на большее, DESC с последнего к первому 
	salary DESC
