"""
Задание-2. Представлен список чисел. Необходимо вывести элементы
исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в
виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

my_list = [1, 3, 5, 6, 2, 54, 1, 52, 55, 2, 45]
print(my_list)
exc = [a for a in my_list if a > my_list[my_list.index(a) - 1]]
print(exc)
