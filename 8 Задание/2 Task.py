"""
Задание-2. Создайте собственный класс-исключение, обрабатывающий
ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве
делителя программа должна корректно обработать эту ситуацию и
не завершиться с ошибкой.
"""


class DivesNull(Exception):
    def __init__(self, text):
        self.text = text


def division():
    try:
        num_x = int(input("Введите делитель: "))
        num_y = int(input("Введите знаменатель: "))
        if num_y == 0:
            raise DivesNull("Делить на ноль нельзя!")
        else:
            total = num_x / num_y
            return total
    except ValueError:
        return "Не верное значение"
    except DivesNull as er:
        return er


print(division())
