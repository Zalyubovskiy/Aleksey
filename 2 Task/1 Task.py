"""
Создать список и заполнить его элементами различных типов
данных. Реализовать скрипт проверки типа данных
каждого элемента. Использовать функцию type()
для проверки типа. Элементы списка можно не
запрашивать у пользователя, а указать явно, в
программе.
"""
my_str = "Добрый день"
my_float = 5.5
my_table = ['x', '6']
my_pool = ('y', '10')
my_dist = 196
my_home = {'Страна': 'Россия', 'Город': 'Москва'}

gen_task = [my_str, my_float, my_table, my_pool, my_dist, my_home]
for i in gen_task:
    print(f'{i} is {type(i)}')