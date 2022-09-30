import sqlite3 as sql

db = sql.connect('solution.db')
# TODO: создаем курсор в нашей базе данных и записываем его в переменную cursor
cursor = db.cursor()
# TODO: сюда мы будем вставлять sql инъекцию (команду): выбрать всё * в нашей базе данных
cursor.execute('SELECT * FROM employees')
# TODO: вывести в терминал одну строку базы данных содержащую значение john
# cursor.execute('SELECT * FROM employees WHERE NAME = "john";')
# TODO: вывести в терминал одну строку базы данных содержащую переменную со значение john
# name = "john"
# cursor.execute('SELECT * FROM employees WHERE NAME = ?;', (name,))
# TODO: инъекция добавления в базу данных новых значений
# cursor.execute("INSERT INTO employees VALUES (2, 'Henry', 80000, 4)")
# db.commit()   # TODO: для сохранения инъекций добавления в базу данных новых значений
# TODO: вывести в терминал одну строку базы данных
# print(cursor.fetchone())
# TODO: вывести в терминал все строки базы данных в виде кортежа
print(cursor.fetchall())


# TODO: подключение базы данных через функции, например когда пишется сайт или телеграмм бот
# def start():
#     with sql.connect("data.db") as db:
#         cursor = db.cursor()
#         db.commit()
#
#
# start()
