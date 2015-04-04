##encoding=UTF-8

"""OFFSET关键字的用法
SQL OFFSET Syntax
-----------------

SELECT *
FROM table_name
LIMIT 5 OFFSET 10

offset 关键字必须配合limit使用。用于跳过前#offset条, 然后再返回#limit条。
不同的数据库系统中可能支持或不支持offset功能。
"""